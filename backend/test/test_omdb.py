import requests
from backend.omdb import check_status, fill_db
from google.appengine.datastore import datastore_query


def test_check_status():
    apikey = "11167468"
    url = "http://www.omdbapi.com/?apikey=" + apikey
    payload = {'s': 'Fast & Furious', 'type': 'movie'}
    response = requests.get(url, params=payload)
    assert check_status(response) is True, "url provided is not valid"


def test_fill_db():
    fill_db()
    entity_key = 'ag1lbmdlbG1pbmFzd2VicgoLEgRVc2VyGGIM'
    entities = datastore_query.Get(entity_key)
    assert 'Movie' in entities
