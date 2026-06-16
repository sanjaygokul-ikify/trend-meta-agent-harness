from packages.core import Engine

class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine

    def register_agent(self, agent_id, policy_id):
        self.engine.register_agent(agent_id)
        self.engine.register_policy(policy_id)