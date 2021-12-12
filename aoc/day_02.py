from functools import reduce
from typing import List


def plan_route(instructions: List[str]):
    def _plan_route(prev_coordinates, action: str):
        prev_pos, prev_depth = prev_coordinates
        action, amount = action.split(" ")
        amount = int(amount)
        if action == "forward":
            return (prev_pos + amount, prev_depth)
        elif action == "down":
            return (prev_pos, prev_depth + amount)
        elif action == "up":
            return (prev_pos, prev_depth - amount)

    return reduce(_plan_route, instructions, (0, 0))


if __name__ == "__main__":
    instructions = ["forward 2", "down 3", "up 2"]
    print(f"Executing for {instructions=}")
    print(f"Position and depth = {plan_route(instructions)}")