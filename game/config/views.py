from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

# 4.26
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = 'main.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

# import matplotlib # 시각화 패키지
# matplotlib.use('Agg') # canvas에 접근하는 cache
# import matplotlib.pyplot as plt # 출력
# from django.http import HttpResponse
# import numpy as np # 선형대수
# import pandas as pd # Dataframe : 이질적 데이터
# import io # 입출력을 제어
# from matplotlib.backends.backend_agg import FigureCanvasAgg


# def pandasgraph_call(request):
#     return render(request, 'pandasgraph_call.html')
#
#
# # 4.26
def register_request(request):
    if request.method == "POST":  # 입력완료된 데이터를 저장하고 로그인, 루트로 redirect
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()  # 빈 폼 : 입력
    return render(request=request, template_name="registration/login.html", context={"register_form":form})

def login(request): # 첫 페이지
    return render(request, 'registration/login.html')

def logout(request): # 첫 페이지
    return render(request, 'registration/logout.html')