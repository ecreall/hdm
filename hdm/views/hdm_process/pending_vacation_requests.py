from pyramid.view import view_config


@view_config(name='pending_vacation_requests', renderer='hdm:views/hdm_process/templates/vacations.pt', )
def pending_vacations_view(request):
    """ A view to list all pending vacations """
    pending_vacations = [vacation for vacation in request.root.vacations if 'pending' in vacation.state]
    return {'vacations': pending_vacations}


