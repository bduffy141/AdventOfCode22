from problems.base import *


class Day(Problem):

    def load(self) -> list[tuple[set[int], set[int]]]:
        with self._load() as f:
            out = []
            for line in f:
                nums = line.strip().replace(",", " ").replace("-", " ")
                s1, e1, s2, e2 = [int(x) for x in nums.split()]

                out.append((
                    set(range(s1, e1+1)), set(range(s2, e2+1))
                ))

            return out

    def solution1(self):
        data = self.load()
        return sum([
            1
            for e1, e2 in data
            if e1.issubset(e2) or e2.issubset(e1)
        ])

    def solution2(self):
        data = self.load()
        return sum([
            1
            for e1, e2 in data
            if e1.intersection(e2) or e2.intersection(e1)
        ])
