from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Genome:
    token_name: str
    genes: Dict[str, Any]

@dataclass
class GeneDefinition:
    key: str
    category: str
    description: str
