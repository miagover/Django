from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

seasonsList = [
    {'title': 'Season One', 'episodes': 13, 'airDate': 'September 19, 2016'},
    {'title': 'Season Two', 'episodes': 13, 'airDate': 'September 20, 2017'},
    {'title': 'Season Three', 'episodes': 13, 'airDate': 'September 27, 2018'},
    {'title': 'Season Four', 'episodes': 14, 'airDate': 'September 26, 2019'}
]

seasonInfo = [
    {'episode': "Episode 13: Michael's Gambit", 'character': 'Shawn', 'relationship': 'Jason + Janet'},
    {'episode': 'Episode 9: Leap to Faith', 'character': 'Shawn', 'relationship': 'Michael + Humans'},
    {'episode': 'Episode 13: Pandemonium', 'character': 'The Judge (Gen)', 'relationship': 'Eleanor + Chidi'},
    {'episode': 'Episode 9: The Answer', 'character': 'Glenn', 'relationship': 'Eleanor + Chidi'}
]

def index(request):
    return render(request, 'seasons/index.html', {
        "seasonsList": seasonsList,
    })

def seasonPage(request, season):
    return render(request, 'seasons/season.html', {
        "seasonNum": season,
        "seasonName": seasonsList[season-1]['title'],
        "info": seasonInfo[season-1]
    })