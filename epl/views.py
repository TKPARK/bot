from django.shortcuts import render
from django.core import serializers
from epl.models import Team
import json

# Create your views here.

def index(request):
    # load
    # create_team()
    
    # select
    teams = Team.objects.filter(nation = 'EPL')
    
    context = {'content': serializers.serialize('json', teams)}
    return render(request, 'epl/index.html', context)

def examples(request):
    context = {'content': serializers.serialize('json', '')}
    return render(request, 'epl/examples.html', context)

def create_team():
    Team.objects.all().delete()

    json_data = open('epl/static/data/epl_teams.json', 'r', encoding='UTF8')
    teams = json.load(json_data)
    
    for team in teams:
        print(team['TEAM_NAME'])
        t = Team(team_name=team['TEAM_NAME'], team_name_kr=team['TEAM_NAME_KR'], nation=team['NATION'], stadium=team['STADIUM'], stadium_kr=team['STADIUM_KR'])
        t.save()
    
    json_data.close()
    