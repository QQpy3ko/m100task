import graphene
from graphene_django import DjangoObjectType

from .models import Car


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        only_fields = [
            'id',
            'name',
            'reg_number',
        ]
