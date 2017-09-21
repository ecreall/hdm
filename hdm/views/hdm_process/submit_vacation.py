# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL

import deform
from pyramid.view import view_config
from substanced.form import FormView 
# from hdm.content.processes.hdm_management.behaviors import SubmitVacation
from hdm.content.vacation import VacationSchema
from hdm.content.root import Root


@view_config(
    name='submit_vacation',
    context=Root,
    renderer='substanced.sdi:templates/form.pt',
    )
class SubmitVacationForm(FormView):
    title = 'Submit'
    schema = VacationSchema()
    buttons = ('Submit',)

    def __call__(self):
        # TODO find action
        # if action call super else raise error or return error view
        return super(SubmitVacationForm, self).__call__()

    def submit_success(self, appstruct):
        # TODO find and excute the action
        pass
