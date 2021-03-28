import requests
import json
from google.appengine.ext import ndb


def fill_db():
    if Movie.query() is None:

        long_sagas_list = ['Fast & Furious', "james bond", "friday the 13th",
                           "THE PINK PANTHER", "STAR TREK", "STAR WARS", "ELM STREET", "SAW"]

        apikey = "11167468"
        url = "http://www.omdbapi.com/?apikey=" + apikey

        for movie in long_sagas_list:
            payload = {'s': movie, 'type': 'movie'}

            response = requests.get(url, params=payload)
            if check_status(response):
                python_dictionary_values = json.loads(response.text)

                for search in python_dictionary_values['Search']:
                    if search:
                        movie = Movie()
                        movie.create_and_save(search)
            else:
                continue

    else:
        print('there are movies in the DB')


def check_status(response):
    if response.status_code == 200:
        return True
    return False

class Movie(ndb.Model):
    year = ndb.StringProperty()
    title = ndb.StringProperty()
    type_movie = ndb.StringProperty()
    poster = ndb.StringProperty()
    saved = ndb.DateTimeProperty(auto_now_add=True)

    def create_and_save(self, search):
        self.create(search)
        self.year = search.get('Year')
        self.title = search.get('Title')
        self.type_movie = search.get('Type')
        self.poster = search.get('Poster')
        self.put()


if __name__ == '__main__':
    fill_db()

