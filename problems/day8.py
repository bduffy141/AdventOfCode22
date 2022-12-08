from problems.base import Problem


class Day(Problem):

    @staticmethod
    def out_visible(data: list[list[int]], i: int, j: int) -> int:
        target = data[i][j]
        row, col = data[i], list(zip(*data))[j]
        l = r = u = d = 0

        for idx in reversed(range(len(row[:j]))):
            if idx != j:
                if row[idx] >= target:
                    l += 1
                    break
                l += 1
            
        for idx in range(len(row[:j]), len(row)):
            if idx != j:
                if row[idx] >= target:
                    r += 1
                    break
                r += 1

        for idx in reversed(range(len(col[:i]))):
            if idx != i:
                if col[idx] >= target:
                    u += 1
                    break
                u += 1
            
        for idx in range(len(col[:i]), len(col)):
            if idx != i:
                if col[idx] >= target:
                    d += 1
                    break
                d += 1

        return l * r * u * d

    @staticmethod
    def in_visible(data: list[list[int]], i: int, j: int) -> bool:
        target = data[i][j]
        if i in [0, len(data)] or j in [0, len(data[i])]:
            return True

        l = r = u = d = True

        for idx, tree in enumerate(data[i]):
            if idx < j and tree >= target:
                l = False
            elif idx > j and tree >= target:
                r = False

        for idx, tree in enumerate(list(zip(*data))[j]):
            if idx < i and tree >= target:
                u = False
            elif idx > i and tree >= target:
                d = False

        return l or r or u or d

    def load(self) -> list[list[int]]:
        with self._load() as f:
            return [
                [
                    int(num)
                    for num in line.strip("\n")
                ] for line in f
            ]

    def solution1(self):
        trees = self.load()

        return sum(
            self.in_visible(trees, i, j)
            for i, row in enumerate(trees)
            for j in range(len(row))
        )

    def solution2(self):
        trees = self.load()

        return max(
            self.out_visible(trees, i, j)
            for i, row in enumerate(trees)
            for j in range(len(row))
        )


