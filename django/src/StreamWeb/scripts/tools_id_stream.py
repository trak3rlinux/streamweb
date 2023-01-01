import requests
import requests as r
from bs4 import BeautifulSoup
import html.parser
import subprocess

"""
{'Title': 'Wednesday', 'Year': '2022–', 'Rated': 'TV-14', 'Released': '23 Nov 2022', 'Runtime': 'N/A', 'Genre': 'Comedy, Crime, Family', 'Director': 'N/A', 'Writer': 'Alfre
d Gough, Miles Millar', 'Actors': 'Jenna Ortega, Gwendoline Christie, Riki Lindhome', 'Plot': "Follows Wednesday Addams' years as a student, when she attempts to master her
 emerging psychic ability, thwart and solve the mystery that embroiled her parents.", 'Language': 'English', 'Country': 'N/A', 'Awards': '3 nominations', 'Poster': 'https:/
/m.media-amazon.com/images/M/MV5BM2ZmMjEyZmYtOGM4YS00YTNhLWE3ZDMtNzQxM2RhNjBlODIyXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Databas
e', 'Value': '8.4/10'}], 'Metascore': 'N/A', 'imdbRating': '8.4', 'imdbVotes': '123,390', 'imdbID': 'tt13443470', 'Type': 'series', 'totalSeasons': 'N/A', 'Response': 'True'}
"""

def get_response_json(query):
    url_imbd_search_id = f"http://www.omdbapi.com/?apikey=a2d34442&t={query}"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}

    req = r.get(url_imbd_search_id, headers=header)
    response_json = req.json()

    return response_json

def get_response_json_with_id(imdb):
    url_imbd_search_id = f"http://www.omdbapi.com/?apikey=a2d34442&i={imdb}"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}

    req = r.get(url_imbd_search_id, headers=header)
    response_json = req.json()

    return response_json

def get_episodes(query):
    url = "https://streaming-availability.p.rapidapi.com/v2/search/title"

    querystring = {"title": query, "country": "us", "type": "series", "output_language": "en"}

    headers = {
        "X-RapidAPI-Key": "db9a44e54emshc23b55eead65efep1293b2jsn77e70c86e625",
        "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()

    data = {}
    for nbr, season in enumerate(response['result'][0]['seasons'], 1):
        data[nbr] = 0
        for episode in season['episodes']:
            data[nbr]+=1

    return data



def get_link_stream(type, imdb, s=0, e=0):
    if type == 'movie':
        link_to_go = f"https://www.2embed.to/embed/imdb/movie?id={imdb}"
    elif type == "series":
        if s != 0 or e != 0:
            link_to_go = f"https://www.2embed.to/embed/imdb/tv?id={imdb}&s={s}&e={e}"
        else:
            link_to_go = f"http://localhost:5500/error"

    return link_to_go


# subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe','-new-tab', link_to_go])

if __name__ == '__main__':
    enter_of_user = input("Name : ")