from django.db import models
from django.contrib.auth.models import User

class Guess(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    # userid = models.IntegerField()
    success_date = models.DateTimeField()
    count = models.IntegerField()
    number = models.CharField(max_length =4)
    result = models.CharField(max_length =20)

    def __str__(self):
        return self.userid
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

