import graphene

from cars.resolver import CarsResolver

class Query(
    CarsResolver
):
    """Parent query class inherited from all real query classes
    """
    pass


class Mutation(graphene.ObjectType):
    """Parent Mutation class containing all mutations
    """
    pass


schema = graphene.Schema(
    query=Query,
    # mutation=Mutation,
)
