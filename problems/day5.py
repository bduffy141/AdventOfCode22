import re

from problems.base import Problem
from collections import deque


class Day(Problem):

    def load(self) -> tuple[list[deque], list[tuple[int, int, int]]]:
        with self._load() as f:
            order, moves = [], []
            crate_pat = re.compile(r"(\s{3}) |\[([A-Z])]")
            move_pat = re.compile(r"(\d+)")
            for line in f:
                line = line.strip("\n")
                if "[" in line:
                    crates = "".join([
                        "-" if not l else l
                        for s, l in crate_pat.findall(line)
                    ])
                    order.append(crates)
                elif "move" in line:
                    move = move_pat.findall(line)
                    num, src, dst = [int(m) for m in move]
                    moves.append((num, src-1, dst-1))

            stacks = [deque() for _ in range(len(order[0]))]
            for crates in reversed(order):
                for idx, crate in list(enumerate(crates)):
                    if crate != "-":
                        stacks[idx].append(crate)

            return stacks, moves

    def solution1(self) -> str:
        stacks, moves = self.load()

        for move in moves:
            num, src, dst = move
            for _ in range(num):
                crate = stacks[src].pop()
                stacks[dst].append(crate)

        return "".join([
            stack.pop()
            for stack in stacks
        ])

    def solution2(self) -> str:
        stacks, moves = self.load()

        for move in moves:
            num, src, dst = move
            crates = [
                stacks[src].pop()
                for _ in range(num)
            ]
            for crate in reversed(crates):
                stacks[dst].append(crate)

        return "".join([
            stack.pop()
            for stack in stacks
        ])
