import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .types import CarType
from .models import Car


class CarsResolver(graphene.ObjectType):
    car = graphene.relay.Node.Field(CarType)
    all_cars = DjangoFilterConnectionField(CarType)
    published_cars = DjangoFilterConnectionField(CarType)

    def resolve_all_cars(_, info):
        return Car.objects.all()

    def resolve_published_cars(_, info):
        return Car.objects.filter(is_publish=True)

   


class PublishCar(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    # The class attributes define the response of the mutation
    car = graphene.Field(CarType)

    def mutate(self, info, id):
        car = Car.objects.get(id=id)
        car.is_publish = True
        car.save()

        return PublishCar(car=car)



class UnpublishCar(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    car = graphene.Field(CarType)

    def mutate(self, info, id):
        car = Car.objects.get(id=id)
        car.is_publish = False
        car.save()

        return UnpublishCar(car=car)

