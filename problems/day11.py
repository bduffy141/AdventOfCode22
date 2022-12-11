from __future__ import annotations

import math
import re

import collections.abc as cabc

from operator import add, mul
from problems.base import Problem


OPS = {"+": add, "*": mul}


class Monkey:

    def __init__(self, mid: int, starting: list[int], op: cabc.Callable, test: tuple[int, int, int]):
        self.id = mid
        self.items = starting.copy()
        self.op = op

        divis, mtrue, mfalse = test
        self.divis = divis
        self.test = lambda i: mtrue if i % self.divis == 0 else mfalse

        self.inspected = 0

    @classmethod
    def from_str(cls, monkey: str) -> Monkey:
        for line in monkey.split("\n"):
            line = line.strip()
            if "Monkey" in line:
                mid = int(line.replace("Monkey ", "").replace(":", ""))
            elif "Starting" in line:
                starting = [int(x) for x in line.partition(": ")[2].split(", ")]
            elif "Operation" in line:
                opp, num = line.partition("old ")[2].split(" ")
                if num.isdecimal():
                    op = lambda old: OPS[opp](old, int(num))
                else:
                    op = lambda old: OPS[opp](old, old)
            elif "Test" in line:
                cond = int(line.rpartition(" ")[2])
            elif "If true" in line:
                ctrue = int(line.rpartition(" ")[2])
            elif "If false" in line:
                cfalse = int(line.rpartition(" ")[2])

        # noinspection PyUnboundLocalVariable
        return cls(mid, starting, op, (cond, ctrue, cfalse))

    def inspect(self) -> None:
        item = self.items[0]
        self.items[0] = self.op(item)
        self.inspected += 1

    def bored1(self) -> None:
        item = self.items[0]
        self.items[0] = item // 3

    def bored2(self, lcm: int) -> None:
        item = self.items[0]
        self.items[0] = item % lcm

    def toss(self) -> tuple[int, int]:
        item = self.items.pop(0)
        return item, self.test(item)

    def recv(self, item: int) -> None:
        self.items.append(item)


class Day(Problem):

    def load(self) -> dict[int, Monkey]:
        with self._load() as f:
            monkeys = {}
            for mstr in f.read().split("\n\n"):
                monkey = Monkey.from_str(mstr)
                monkeys[monkey.id] = monkey

            return monkeys

    def solution1(self):
        monkeys = self.load()

        rounds = 20
        for _ in range(rounds):
            for monkey in monkeys.values():
                while monkey.items:
                    monkey.inspect()
                    monkey.bored1()
                    item, dest = monkey.toss()
                    monkeys[dest].recv(item)

        top_shit = sorted([monkey.inspected for monkey in monkeys.values()])
        return top_shit[-1] * top_shit[-2]

    def solution2(self):
        monkeys = self.load()

        rounds = 10000
        for r in range(rounds):
            lcm = math.lcm(*[monkey.divis for monkey in monkeys.values()])
            for monkey in monkeys.values():
                while monkey.items:
                    monkey.inspect()
                    monkey.bored2(lcm)
                    item, dest = monkey.toss()
                    monkeys[dest].recv(item)

        top_shit = sorted([monkey.inspected for monkey in monkeys.values()])
        return top_shit[-1] * top_shit[-2]
