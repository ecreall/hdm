from dace.definition.activitydef import ActivityDefinition
from dace.definition.eventdef import StartEventDefinition, EndEventDefinition
from dace.definition.processdef import ProcessDefinition
from dace.definition.transitiondef import TransitionDefinition
from dace.model.services.processdef_container import process_definition

from hdm.content.processes.hdm_process.behaviors import RequestVacation


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
            end=EndEventDefinition()
        )

        self.define_transitions(
            TransitionDefinition('start', 'request'),
            TransitionDefinition('request', 'end'),
        )
