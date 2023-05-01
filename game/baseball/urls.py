from baseball import views
from django.urls import path
app_name = 'baseball'
urlpatterns = [
    path('game/baseball', views.game, name='game'),
    path('rank/baseball', views.rank, name='rank'),
    path('play_baseball/baseball', views.play_baseball, name='play_baseball'),
    path('', views.rankList.as_view(), name='rank'),
]



