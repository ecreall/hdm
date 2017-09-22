import datetime
from dace.definition.activitydef import ActivityDefinition
from dace.definition.eventdef import (
    StartEventDefinition,
    EndEventDefinition,
    IntermediateCatchEventDefinition,
    TimerEventDefinition)
from dace.definition.gatewaydef import ExclusiveGatewayDefinition
from dace.definition.processdef import ProcessDefinition
from dace.definition.transitiondef import TransitionDefinition
from dace.model.services.processdef_container import process_definition

from hdm.content.processes.hdm_process.behaviors import (
    RequestVacation,
    Accept,
    Refuse,
    Alert)


def accept_condition(process):
    vacation = process.execution_context.created_entity('vacation')
    return 'accepted' in vacation.state


def refuse_condition(process):
    vacation = process.execution_context.created_entity('vacation')
    return 'refused' in vacation.state


def time_date(process):
    # Recuperate the vacation instance related to this process
    # vacation = process.execution_context.created_entity('vacation')
    # date = vacation.finish - datetime.timedelta(days=1)
    # Test
    date = datetime.timedelta(minutes=1) +\
        datetime.datetime.now()
    return date


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
            eg2=ExclusiveGatewayDefinition(),
            timer = IntermediateCatchEventDefinition(
                           TimerEventDefinition(time_date=time_date)),
            alert=ActivityDefinition(
                behaviors=[Alert],
                description='Alert the user',
                title='Alert'
            ),
            eg3=ExclusiveGatewayDefinition(),
            end=EndEventDefinition()
        )

        self.define_transitions(
            TransitionDefinition('start', 'request'),
            TransitionDefinition('request', 'eg'),
            TransitionDefinition('eg', 'refuse'),
            TransitionDefinition('eg', 'accept'),
            TransitionDefinition('refuse', 'eg1'),
            TransitionDefinition('accept', 'eg1'),
            TransitionDefinition('eg1', 'eg2'),
            TransitionDefinition('eg2', 'timer', accept_condition),
            TransitionDefinition('timer', 'alert'),
            TransitionDefinition('alert', 'eg3'),
            TransitionDefinition('eg2', 'eg3', refuse_condition),
            TransitionDefinition('eg3', 'end')
        )
