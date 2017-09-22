# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
from dace.interfaces import (
    IEntity, IApplication)


class IRoot(IEntity, IApplication):
    pass


class IVacation(IEntity):
    pass