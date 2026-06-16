from ..core.engine import Engine
from ..core.exceptions import HarnessException

class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine

    def execute(self, agent_id: str, policy_id: str, model_id: str, inputs: List[str]) -> str:
        try:
            return self.engine.orchestrate(agent_id, policy_id, model_id, inputs)
        except HarnessException as e:
            # Handle the exception or re-raise it with additional context
            raise