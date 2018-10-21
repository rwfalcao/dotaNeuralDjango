from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .models import *
import dota2api as dota2api
import json
from keras.utils import to_categorical
from keras import models
from keras import layers
from keras.models import load_model
from django.contrib.staticfiles.storage import staticfiles_storage
import tensorflow as tf
from .neural import neuralNetwork




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
    heroListDict = {}
    heroListDict['heroes'] = Hero.objects.all()

    comp = Composition()
    comp.save()

    heroListDict['composition'] = comp

    
    
    return render(request, 'dotaPrediction/heroList.html', heroListDict)

def buildTeamComposition(request, compPk, heroPk):
        currentComp = Composition.objects.get(pk=compPk)
        heroPicked = Hero.objects.get(pk=heroPk)
        
        heroesTeamZero = currentComp.teamZero.all()
        heroesTeamOne = currentComp.teamOne.all()
        
        if len(heroesTeamOne) + len(heroesTeamZero) < 10:
            if len(heroesTeamZero) < 5:
                currentComp.teamZero.add(heroPicked)
            elif len(heroesTeamOne) < 5:
                currentComp.teamOne.add(heroPicked)
        

        teamZeroNames = list()
        teamOneNames = list()
        data = dict()
        for hero in currentComp.teamZero.all():
                teamZeroNames.append(hero.localized_name)
                
        for hero in currentComp.teamOne.all():
                teamOneNames.append(hero.localized_name)
        
        data['teamZero'] = teamZeroNames
        data['teamOne'] = teamOneNames

        contextZero = { 'pickedHeroes': currentComp.teamZero.all() }
        contextOne = { 'pickedHeroes': currentComp.teamOne.all() }

        
        data['html_team_zero'] = render_to_string('dotaPrediction/pickedHeroesLoop.html', contextZero, request=request)
        data['html_team_one'] = render_to_string('dotaPrediction/pickedHeroesLoop.html', contextOne, request=request)

        if len(heroesTeamOne) + len(heroesTeamZero) == 10:
                currentComp.save()

        return JsonResponse(data)


def winnerTeam(request, compPk):
        comp = Composition.objects.get(pk=compPk)
        compArray = [0] * 113

        for hero in comp.teamZero.all():
                compArray[hero.heroApiId-1] = -1
        
        for hero in comp.teamOne.all():
                compArray[hero.heroApiId-1] = 1

        result = neuralNetwork(compArray)

        if result[0][0] > result[0][1]:
                final = 'Time One'
        else:         
                final = 'Time Zero'
                
       
        return HttpResponse(final)

        
'''
        with tf.Session():
                
'''

        

        


        



