from django.shortcuts import render

from .models import Guess
import random
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required


@login_required
def game(request): # 첫 페이지
    global count
    global target
    count = 0
    # numbers = list(range(10))
    # random.shuffle(numbers)x
    # target = ''.join(map(str, numbers[:4]))
    # global guess_results
    # guess_results = []
    return render(request, 'baseball/game.html')

def rank(request): # 첫 페이지
    return render(request, 'baseball/rank.html')

class rankList(ListView):
    model = Guess
    template_name = 'baseball/rank.html'


numbers = list(range(10))
random.shuffle(numbers)
target = ''.join(map(str, numbers[:4]))
count = 0
guess_results=[]


@login_required
def play_baseball(request):
    global count
    global target
    if request.method == 'POST':
        guess = request.POST['guess']
        result = check_guess(request,guess)
        guess_results.append(result) # result로 매개변수 받으니, 온갖정보가 다 들어옴.
        # guess로 수정된 상태
        return render(request, 'baseball/game.html', {'result': result, 'guess_results': guess_results})
    else:
        return render(request, 'baseball/game.html')


def check_guess(request, number):
    global count, target, guess_results

    strike = 0
    ball = 0
    out = 0
    user = request.user

    if count == 0:
        numbers = list(range(10))
        random.shuffle(numbers)
        target = ''.join(map(str, numbers[:4]))
        guess_results = []

    for check in number:
        if check in target:
            if number.index(check) == target.index(check):
                strike += 1
            else:
                ball += 1
        else:
            out += 1

    count += 1

    if strike == 4:
        result = {
            "result": "홈런!",
            "count": count,
            "target": target,
            "number": number,
            "strike": strike,
            "ball": ball,
            "out": out
        }

        guess = Guess.objects.create(userid=user, success_date=datetime.now(), count=count)
        guess.save()

        count = 0
        numbers = list(range(10))
        random.shuffle(numbers)
        target = ''.join(map(str, numbers[:4]))
        guess_results.clear()  # guess_results 리스트 초기화

    else:
        result = {
            "result": f"{count}회:",
            "count": count,
            "target": target,
            "number": number,
            "strike": strike,
            "ball": ball,
            "out": out
        }
    return result


# @login_required
# def play_baseball(request):
#     global target
#     if request.method == 'POST':
#         guess = request.POST['guess']
#         result = check_guess(request,guess)
#         guess_results.append(guess) # result로 매개변수 받으니, 온갖정보가 다 들어옴.
#         # guess로 수정된 상태
#         return render(request, 'baseball/game.html', {'result': result, 'guess_results': guess_results})
#     else:
#         return render(request, 'baseball/game.html')
#
#
# def check_guess(request,number):
#     global count
#     global target
#     strike = 0
#     ball = 0
#     out = 0
#     user = request.user
#     for check in number:
#         if check in target:
#             if number.index(check) == target.index(check):
#                 strike += 1
#             else:
#                 ball += 1
#         else:
#             out += 1
#     count += 1
#     if strike == 4:
#         result = {
#             "result": "홈런!",
#             "count": count,
#             "target": target,
#             "number": number,
#             "strike": strike,
#             "ball": ball,
#             "out": out
#         }
#
#         guess = Guess.objects.create(userid=user, success_date=datetime.now(), count=count)
#         guess.save()
#         count = 0
#         numbers = list(range(10))
#         random.shuffle(numbers)
#         target = ''.join(map(str, numbers[:4]))
#         global guess_results
#         guess_results = []
#
#     else:
#         result = {
#             "result": f"{count}회:",
#             "count": count,
#             "target": target,
#             "number": number,
#             "strike": strike,
#             "ball": ball,
#             "out": out
#         }
#     guess_results = []  # guess_results 리스트 초기화
#     return result

