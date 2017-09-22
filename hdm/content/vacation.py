import colander
from dace.model.entity import Entity

from deform.widget import TextInputWidget, TextAreaWidget
from zope.interface import implementer

from hdm.content.interface import IVacation


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


@implementer(IVacation)
class Vacation(Entity):
    """Vacation class"""

    def __init__(self, **kwargs):
        super(Vacation, self).__init__(**kwargs)
        self.set_data(kwargs)
