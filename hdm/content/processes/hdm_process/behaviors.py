from dace.instance.activity import ElementaryAction

from hdm.content.interface import IRoot
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

        return {'message': 'vacation request added'}
