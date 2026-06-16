class HarnessException(Exception):
    pass

class PolicyException(HarnessException):
    pass

class AgentException(HarnessException):
    pass

class ModelException(HarnessException):
    pass