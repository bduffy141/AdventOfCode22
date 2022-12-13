from __future__ import annotations

import functools as ft
import json
import operator as op
import typing

from problems.base import Problem

Rec = list[typing.Union[list[int], "Rec"]]


class Day(Problem):

    def load(self) -> list[tuple[Rec, Rec]]:
        with self._load() as f:
            out = []
            for block in f.read().split("\n\n"):
                l = json.loads(block.split("\n")[0])
                r = json.loads(block.split("\n")[1])
                out.append((l, r))

            return out

    def cmp(self, left: Rec | int, right: Rec | int) -> int:
        match (isinstance(left, int), isinstance(right, int)):
            case (True, True):
                return left - right
            case (True, False):
                return self.cmp([left], right)
            case (False, True):
                return self.cmp(left, [right])
            case (False, False):
                for l, r in zip(left, right):
                    if (res := self.cmp(l, r)) != 0:
                        return res
                return len(left) - len(right)

    def solution1(self):
        packets = self.load()
        return sum(
            idx + 1
            for idx, packet in enumerate(packets)
            if self.cmp(packet[0], packet[1]) < 0
        )

    def solution2(self):
        packets = self.load()
        sbulk = sorted([
            *ft.reduce(op.iconcat, packets), [[2]], [[6]]
        ], key=ft.cmp_to_key(self.cmp))

        return (sbulk.index([[2]]) + 1) * \
               (sbulk.index([[6]]) + 1)
