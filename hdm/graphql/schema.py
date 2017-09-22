# -*- coding: utf-8 -*-
import graphene
from graphene import relay

from dace.util import get_obj

from hdm.content.vacation import Vacation as SDVacation

class Node(object):

    @classmethod
    def get_node(cls, id, context, info):  #pylint: disable=W0613,W0622
        oid = int(id)
        return get_obj(oid)


class Vacation(Node, graphene.ObjectType):

    """HDM vacations."""

    class Meta(object):
        interfaces = (relay.Node,)

    start = graphene.String()
    finis = graphene.String()
    
    @classmethod
    def is_type_of(cls, root, context, info):  # pylint: disable=W0613
        if isinstance(root, cls):
            return True

        return isinstance(root, SDVacation)

    def resolve_start(self, args, context, info):
        return self.start.isoformat()

    def resolve_finish(self, args, context, info):
        return self.finish.isoformat()


class Query(graphene.ObjectType):

    node = relay.Node.Field()
    vacations = relay.ConnectionField(
        Vacation,
    )

    def resolve_vacations(self, args, context, info):  # pylint: disable=W0613
        return context.root.vacations



schema = graphene.Schema(query=Query, mutation=Mutations)


if __name__ == '__main__':
    import json
    schema_dict = {'data': schema.introspect()}
    with open('schema.json', 'w') as outfile:
        json.dump(schema_dict, outfile)
