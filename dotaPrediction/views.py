from django.shortcuts import render
from .models import *
import dota2api as dota2api
import json



# Create your views here.

def heroList(request):
    if not Hero.objects.all():
        api = dota2api.Initialise('FCEE1CD700BDB6325239D78360CC40C5')
        heroList = api.get_heroes()['heroes']

        for hero in heroList:
            newHero = Hero()

            newHero.heroApiId = hero['id']
            newHero.name = hero['name']
            newHero.localized_name = hero['localized_name']
            newHero.url_full_portrait = hero['url_full_portrait']
            newHero.url_large_portrait = hero['url_large_portrait']
            newHero.url_small_portrait = hero['url_small_portrait']
            newHero.url_vertical_portrait = hero['url_vertical_portrait']

            newHero.save()
    heroesDict = {}
    heroesDict['heroes'] = Hero.objects.all()

    

    return render(request, 'dotaPrediction/heroList.html', heroesDict)