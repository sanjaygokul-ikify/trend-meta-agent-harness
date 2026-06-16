import unittest
from packages.core import Engine, Agent, Policy, Model


class TestCore(unittest.TestCase):
    def test_register_agent(self):
        engine = Engine()
        agent = Agent('agent1', 'policy1')
        engine.register_agent(agent)
        self.assertIn('agent1', engine.agents)

    def test_register_policy(self):
        engine = Engine()
        policy = Policy('policy1', 'content1')
        engine.register_policy(policy)
        self.assertIn('policy1', engine.policies)

    def test_register_model(self):
        engine = Engine()
        model = Model('model1', ['input1'])
        engine.register_model(model)
        self.assertIn('model1', engine.models)

    def test_validate_policy(self):
        engine = Engine()
        agent = Agent('agent1', 'policy1')
        policy = Policy('policy1', 'policy1')
        engine.register_agent(agent)
        engine.register_policy(policy)
        self.assertTrue(engine.validate_policy('policy1', 'agent1'))

    def test_execute_model(self):
        engine = Engine()
        model = Model('model1', ['input1'])
        engine.register_model(model)
        result = engine.execute_model('model1', ['input1'])
        self.assertEqual(result, 'input1')