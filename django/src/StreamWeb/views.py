
from django.http import HttpResponse
from .scripts.tools_id_stream import *
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def search(request, search_query):
    json = get_response_json(search_query)

    return render(request, 'search.html', {'query': search_query,
                                           'type': json['Type'],
                                           'poster': json['Poster'],
                                           'imdb': json['imdbID'],
                                           'plot': json['Plot']})

def movie(request, imdb):
    #print(str(request).split('/')[2])
    json = get_response_json_with_id(imdb)
    return render(request, 'movie.html', {'imdb': imdb,
                                          'link': get_link_stream(json['Type'], imdb),
                                          'movie_name': json['Title'],
                                          'type': json['Type'],
                                          'poster': json['Poster'],
                                          'plot': json['Plot']})

def series(request, imdb):
    json = get_response_json_with_id(imdb)
    links = {}
    data = get_episodes(json['Title'])
    nbr_season = len(data.keys())
    for season in range(1, nbr_season+1):
        links[season] = []
        nbr_episode = data[season]
        for episode in range(1, nbr_episode+1):
            links[season].append(get_link_stream(json['Type'], imdb, s=season, e=episode))

    return render(request, 'series.html', { 'imdb': imdb,
                                            'links': links,
                                            'series_name': json['Title'],
                                            'type': json['Type'],
                                            'poster': json['Poster'],
                                            'plot': json['Plot']})