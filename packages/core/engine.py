import logging
from typing import List, Dict
from .types import Agent, Policy, Model
from .exceptions import HarnessException, PolicyException

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.policies: Dict[str, Policy] = {}
        self.models: Dict[str, Model] = {}

    def register_agent(self, agent: Agent):
        if agent.id in self.agents:
            raise HarnessException('Agent already registered')
        self.agents[agent.id] = agent

    def register_policy(self, policy: Policy):
        if policy.id in self.policies:
            raise PolicyException('Policy already registered')
        self.policies[policy.id] = policy

    def register_model(self, model: Model):
        if model.id in self.models:
            raise HarnessException('Model already registered')
        self.models[model.id] = model

    def validate_policy(self, policy_id: str, agent_id: str) -> bool:
        policy = self.policies.get(policy_id)
        agent = self.agents.get(agent_id)
        if not policy or not agent:
            logger.error('Policy or agent not found')
            return False
        # Perform policy validation logic here
        # For demonstration purposes, we'll assume a simple string matching
        return policy.content == agent.policy

    def execute_model(self, model_id: str, inputs: List[str]) -> str:
        model = self.models.get(model_id)
        if not model:
            logger.error('Model not found')
            return ''
        # Perform model execution logic here
        # For demonstration purposes, we'll assume a simple string concatenation
        return ''.join(inputs)

    def orchestrate(self, agent_id: str, policy_id: str, model_id: str, inputs: List[str]) -> str:
        if not self.validate_policy(policy_id, agent_id):
            raise HarnessException('Policy validation failed')
        result = self.execute_model(model_id, inputs)
        # Additional error handling
        if not result:
            raise HarnessException('Model execution failed')
        return result