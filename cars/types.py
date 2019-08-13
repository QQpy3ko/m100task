import graphene
from graphene_django import DjangoObjectType
import django_filters

from .models import Car


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        filter_fields = [
            'id',
            'name',
            'reg_number',
            'is_publish',
        ]
        interfaces = (graphene.relay.Node,)



