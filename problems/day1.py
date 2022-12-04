from problems.base import Problem


class Day(Problem):

    def load(self) -> list[list[int]]:
        with self._load() as f:
            return [
                [int(cal) for cal in elf.split("\n")]
                for elf in f.read().split("\n\n")
            ]

    def solution1(self):
        ecals = self.load()

        # noinspection PyTypeChecker
        return sum(max(ecals, key=sum))

    def solution2(self):
        ecals = self.load()

        s = 0
        for _ in range(3):
            # noinspection PyTypeChecker
            m = max(ecals, key=sum)
            s += sum(m)

            ecals.pop(ecals.index(m))

        return s



