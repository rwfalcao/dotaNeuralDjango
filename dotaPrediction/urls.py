from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.heroList, name="heroList"),
    path('pickHero/<int:compPk>/<int:heroPk>', views.buildTeamComposition, name='pickHero'),
    path('winnerTeam/<int:compPk>', views.winnerTeam, name='winnerTeam')
]
