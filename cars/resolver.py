import graphene

from .types import CarType
from .models import Car


class CarsResolver(graphene.ObjectType):
    cars = graphene.List(CarType)

    def resolve_cars(_, info):
        return Car.objects.all()