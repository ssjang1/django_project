from django.db import models
from django.contrib.auth.models import User

class Guess(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    # userid = models.IntegerField()
    success_date = models.DateTimeField()
    count = models.IntegerField()
    number = models.CharField(max_length =4)
    result = models.CharField(max_length =20)

        # 클래스 안에 메서드 형태로 입력!!!#
    def __str__(self):
        return f'[{self.pk}] {self.userid}'
        # pk는 각 레코드에 대한 고유의 값 + 플레이한 userid
    @property
    def number(self):
        return self.number

    @property
    def result(self):
        return self.result

    
    class Meta: # 클래스에 대한 정보
        verbose_name = '랭킹'
        verbose_name_plural = '랭킹셋'
        ordering = ['count','-success_date'] # 1순위 : 카운트, 2순위 : 최근날짜

