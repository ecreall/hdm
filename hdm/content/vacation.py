import colander
from dace.model.entity import Entity

from deform.widget import TextInputWidget, TextAreaWidget


class VacationSchema(colander.Schema):
    start = colander.SchemaNode(
        colander.Date(),
        title='Début'
    )
    finish = colander.SchemaNode(
        colander.Date(),
        title='Fin'
    )
    employee = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(max=100),
        widget=TextInputWidget(),
        description='Employee'
    )
    reason = colander.SchemaNode(
        colander.String(),
        widget=TextAreaWidget(),
        description='Motif'
    )


class Vacation(Entity):
    def __init__(self, start=None, finish=None, employee=None, reason=None):
        super().__init__(start=start, finish=finish, employee=employee, reason=reason)
        self.start = start
        self.finish = finish
        self.employee = employee
        self.reason = reason
