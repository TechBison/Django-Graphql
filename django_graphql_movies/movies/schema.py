import graphene 

from graphene_django.types import DjangoObjectType, ObjectType

from django_graphql_movies.movies.models import Actor, Movie

class ActorType(DjangoObjectType):
    class Meta:
        model = Actor

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

class Query(ObjectType):
    actor = graphene.Field(ActorType,id=graphene.Int())
    movie = graphene.Field(MovieType,id=graphene.Int())
    actors = graphene.List(ActorType)
    movies = graphene.List(MovieType)

    

    