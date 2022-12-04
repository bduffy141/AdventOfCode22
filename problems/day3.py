from problems.base import Problem


class Day(Problem):

    def load(self) -> list[tuple[str, str]]:
        with self._load() as f:
            return [
                (l[:len(l)//2], l[len(l)//2:])
                for line in f
                if (l := line.strip())
            ]

    def solution1(self):
        s = 0
        data = self.load()

        for l1, l2 in data:
            shared = list(set(l1).intersection(l2))[0]
            val = ord(shared)
            if val >= 97:
                val -= 96
            else:
                val -= 38

            s += val

        return s

    def solution2(self):
        s = 0
        data = self.load()
        data = [data[i:i+3] for i in range(0, len(data), 3)]

        for group in data:
            l1 = group[0][0] + group[0][1]
            l2 = group[1][0] + group[1][1]
            l3 = group[2][0] + group[2][1]

            shared = list(set(l1).intersection(l2, l3))[0]
            val = ord(shared)
            if val >= 97:
                val -= 96
            else:
                val -= 38

            s += val

        return s





