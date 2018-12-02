from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

# variable Type
V = TypeVar('V')
# domain type
D = TypeVar('D')


# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    # the variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        pass


# A constraint satisfaction problem consists of variables of type V
# that have ranges of values known as domains of type D and contraints
# that determines wether a particular variable's domain selection is valid
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        # variables to be constrained
        self.variables: List[V] = variables
        # domain for each variable
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a doamin assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    # Check if the value assignement is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignement: Dict[V, D]) -> bool:
        for constraint in self.contraints[variable]:
            if not constraint.satistfied(assignement):
                return False
        return True

