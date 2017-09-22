from persistent.list import PersistentList

from dace.instance.activity import ElementaryAction

from hdm.content.interface import IRoot, IVacation
from hdm.content.vacation import Vacation


class RequestVacation(ElementaryAction):
    context = IRoot

    def start(self, context, request, appstruct, **kw):
        # create a vacation instance
        vacation = Vacation(**appstruct)
        # set its state to "pending"
        vacation.state.append('pending')
        # add it to context
        context.addtoproperty('vacations', vacation)
        # add relation between the process instance and the prodused vacation
        self.process.execution_context.add_created_entity(
            'vacation', vacation)
        return {'message': 'vacation request added'}


def process_relation_validation(process, context):
    # test if the vacation has relation with the process
    return process.execution_context.has_relation(
        context, 'vacation')


class Accept(ElementaryAction):
    context = IVacation
    processs_relation_id = 'vacation'
    relation_validation = process_relation_validation
    view_name = 'accept'

    def start(self, context, request, appstruct, **kw):
        context.state = PersistentList(['accepted'])
        return {'message': 'vacation accepted'}


class Refuse(ElementaryAction):
    context = IVacation
    processs_relation_id = 'vacation'
    relation_validation = process_relation_validation
    view_name = 'refuse'

    def start(self, context, request, appstruct, **kw):
        context.state = PersistentList(['refused'])
        return {'message': 'vacation refused'}
