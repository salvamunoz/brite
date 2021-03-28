from backend import api, omdb
from protorpc import remote, messages, message_types


@api.endpoint(path="movie", title="movies")
class Movie(remote.Service):

    def list_movies(remote.Service):
        query = Movie.query()
        query.filter('title')
        return list(query.fetch())
        # after checking about how it works I cant find a way how it works, I am not sure if
        # there is something I should connect to the project you gave me, or should I create
        # a new DB in Google. 
