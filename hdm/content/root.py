# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL

from zope.interface import implementer

from substanced.content import content
from substanced.util import renamer

from dace.model.application import Application
from dace.model.entity import Entity
from dace.descriptors import (
    CompositeMultipleProperty)

from .interface import IRoot


@content(
    'Root',
    icon='glyphicon glyphicon-home',
    after_create='after_create',
    )
@implementer(IRoot)
class Root(Application):
    """Nova-Ideo class (Root)"""

    name = renamer()
    vations = CompositeMultipleProperty('vations')

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
