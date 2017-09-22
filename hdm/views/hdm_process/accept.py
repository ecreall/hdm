
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from dace.util import get_all_business_actions


@view_config(name='accept')
def accept(context, request):
    process_actions = get_all_business_actions(
        context=context,
        request=request,
        process_id='vacation_management',
        node_id='accept'
    )
    if process_actions:
        action_to_execute = process_actions[0]
        action_to_execute.execute(context, request, {})
        
    return HTTPFound(
    	request.resource_url(
    		context, 'pending_vacation_requests'))
