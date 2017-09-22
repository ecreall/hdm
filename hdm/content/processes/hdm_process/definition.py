from dace.definition.activitydef import ActivityDefinition
from dace.definition.eventdef import StartEventDefinition, EndEventDefinition
from dace.definition.gatewaydef import ExclusiveGatewayDefinition
from dace.definition.processdef import ProcessDefinition
from dace.definition.transitiondef import TransitionDefinition
from dace.model.services.processdef_container import process_definition

from hdm.content.processes.hdm_process.behaviors import (
    RequestVacation,
    Accept,
    Refuse)


@process_definition(id='vacation_management', title='Request vacation')
class VacationManagement(ProcessDefinition):
    is_unique = False
    is_volatile = True

    def init_definition(self):
        self.define_nodes(
            start=StartEventDefinition(),
            request=ActivityDefinition(
                behaviors=[RequestVacation],
                description='Employee requests vacation',
                title='Request vacation'
            ),
            eg=ExclusiveGatewayDefinition(),
            accept=ActivityDefinition(
                behaviors=[Accept],
                description='Accept vacation',
                title='Accept'
            ),
            refuse=ActivityDefinition(
                behaviors=[Refuse],
                description='Refuse vacation',
                title='Refuse'
            ),
            eg1=ExclusiveGatewayDefinition(),
            end=EndEventDefinition()
        )

        self.define_transitions(
            TransitionDefinition('start', 'request'),
            TransitionDefinition('request', 'eg'),
            TransitionDefinition('eg', 'refuse'),
            TransitionDefinition('eg', 'accept'),
            TransitionDefinition('refuse', 'eg1'),
            TransitionDefinition('accept', 'eg1'),
            TransitionDefinition('eg1', 'end'),
        )
