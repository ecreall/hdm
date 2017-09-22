from pyramid.view import view_config

#
#   Index view
#
@view_config(
    renderer='templates/index.pt',
    )
def index_view(request):
    return {}
