# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL

import colander
import deform
from zope.interface import implementer

from substanced.content import content
from substanced.util import renamer
from substanced.schema import Schema

from dace.model.entity import Entity

from .interface import IVacation


class VacationSchema(Schema):
    """Schema for vacation"""

    details = colander.SchemaNode(
        colander.String(),
        title="Details",
        widget=deform.widget.TextAreaWidget(rows=10, cols=60),
        description="Dtails"
    )


@content(
    'vacation',
    icon='glyphicon glyphicon-home',
    )
@implementer(IVacation)
class Vacation(Entity):
    """Vacation class"""

    def __init__(self, **kwargs):
        super(Vacation, self).__init__(**kwargs)
        self.set_data(kwargs)
