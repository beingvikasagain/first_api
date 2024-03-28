import graphene
from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType


class MyModelType(DjangoObjectType):
    class Meta:
        model=User

class Query(graphene.ObjectType):
    mymodels = graphene.List(MyModelType)

    def resolve_my_model(self,info, **kwargs):
        return User.objects.first()
    
schema = graphene.Schema(query=Query)
