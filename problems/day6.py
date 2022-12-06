from problems.base import Problem


class Day(Problem):

    def load(self) -> str:
        with self._load() as f:
            return f.read()

    def algorithm(self, target: int) -> int:
        data = self.load()

        for i in range(len(data)):
            if len(set(data[i:i+target])) == target:
                return i+target

    def solution1(self):
        return self.algorithm(4)

    def solution2(self):
        return self.algorithm(14)
