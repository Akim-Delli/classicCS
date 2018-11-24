from __future__ import annotations
from typing import List, Optional
from search.generic_search import bfs, Node, node_to_path

MAX_NUM: int = 3


class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        # west bank missionaries
        self.wm: int = missionaries
        # west bank cannibals
        self.wc: int = cannibals
        # est bank missionaries
        self.em: int = MAX_NUM - self.wm
        # est bank cannibals
        self.ec: int = MAX_NUM - self.wc
        self.boat: bool = boat

    def __str__(self) -> str:
        location = "west" if self.boat else "east"
        return (f"On the west bank there are {self.wm} missionaries and {self.wc} cannibals.\n"
                f"On the east bank there are {self.em} missionaries and {self.ec} cannibals.\n"
                f"The boat is on the {location} bank.")

    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

    @property
    def is_legal(self) -> bool:
        if 0 < self.wm < self.wc:
            return False
        if 0 < self.em < self.ec:
            return False
        return True

    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []
        # boat on west bank
        if self.boat:
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc-2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc-1, not self.boat))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm, self.wc, not self.boat))
        # boat on the east bank
        else:
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))

        return [x for x in sucs if x.is_legal]


def display_solution(path: List[MCState]):
    # sanity check
    if len(path) == 0:
        return
    old_state = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print(f'{old_state.em -current_state.em} missionaries and {old_state.ec - current_state.ec} cannibals'
                  f' moved from the east bank to the west')
        else:
            print(f'{old_state.wm - current_state.wm} missionaries and {old_state.wc - current_state.wc} cannibals'
                  f' moved from the west bank to the east')
        print(current_state)
        old_state = current_state


if __name__ == "__main__":
        start: MCState = MCState(MAX_NUM, MAX_NUM, True)
        solution: Optional[Node[MCState]] = bfs(start, MCState.goal_test, MCState.successors)
        if solution is None:
            print("No solution found!")
        else:
            path: List[MCState] = node_to_path(solution)
            display_solution(path)


