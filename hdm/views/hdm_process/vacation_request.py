import deform
from dace.util import get_all_business_actions
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from substanced.form import FormView

from hdm.content.root import Root
from hdm.content.vacation import VacationSchema


@view_config(
    context=Root,
    name='vacation_request',
    renderer='substanced.sdi:templates/form.pt',
)
class AddDocumentView(FormView):
    """
    A form view to submit vacation requests
    """
    title = 'Add Document'
    schema = VacationSchema()
    buttons = ('submit',)

    def submit_success(self, appstruct):
        process_actions = get_all_business_actions(
            context=self.request.root,
            request=self.request,
            process_id='vacation_management',
            node_id='request'
        )
        if process_actions:
            action_to_execute = process_actions[0]
            action_to_execute.execute(self.request.root, self.request, appstruct)
        return HTTPFound(self.request.resource_url(self.context, 'pending_vacation_requests'))
