from typing import List, Dict

class TrendData:
    def __init__(self, values: List[float], timestamp: int):
        self.values = values
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f'TrendData(values={self.values}, timestamp={self.timestamp})'

class TrendMeta:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f'TrendMeta(name={self.name}, description={self.description})'

