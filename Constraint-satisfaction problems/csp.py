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
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

    # Check if the value assignement is consistent by checking all constraints
    # for the given variable against it
    def consistent(self, variable: V, assignement: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignement):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is complete if every variable is assigned (our base case)
        if len(assignment) == len(self.variables):
            return assignment

        # get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # get the every possible domain value of the first unassigned variable
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignement = assignment.copy()
            local_assignement[first] = value
            # if we're still consistent, we recurse
            if self.consistent(first, local_assignement):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignement)
                # if we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None






