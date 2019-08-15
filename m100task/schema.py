import graphene
from graphene_django.filter import DjangoFilterConnectionField

from cars.resolver import CarsResolver, PublishCar, UnpublishCar
from cars.types import CarType


class Query(CarsResolver):
    """Parent query class inherited from all real query classes
    """
    pass 


class CarMutation(CarUnpub):
    unpublish_car = UnpublishCar.Field()
    publish_car = PublishCar.Field()



schema = graphene.Schema(
    query=Query,
    mutation=CarMutation
)
