import unittest
from packages.core import Engine
from services.orchestrator import Orchestrator


class TestPipeline(unittest.TestCase):
    def test_orchestrate(self):
        engine = Engine()
        orchestrator = Orchestrator(engine)
        agent = Agent('agent1', 'policy1')
        policy = Policy('policy1', 'policy1')
        model = Model('model1', ['input1'])
        engine.register_agent(agent)
        engine.register_policy(policy)
        engine.register_model(model)
        result = engine.orchestrate('agent1', 'policy1', 'model1', ['input1'])
        self.assertEqual(result, 'input1')