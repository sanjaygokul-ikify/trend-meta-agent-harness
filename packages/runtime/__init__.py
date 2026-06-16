from .executor import Executor
from ..core.engine import Engine

class Runtime:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.executor = Executor(engine)

    def execute(self, agent_id: str, policy_id: str, model_id: str, inputs: List[str]) -> str:
        return self.executor.execute(agent_id, policy_id, model_id, inputs)