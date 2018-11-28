from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

# variable Type
V = TypeVar('V')
# domain type
D = TypeVar('D')


# Base class for all constraints
class Constraints(Generic[V, D], ABC):
    # the variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignement: Dict[V, D]) -> bool:
        pass
