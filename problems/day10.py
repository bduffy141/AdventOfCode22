from problems.base import Problem


class Instr:

    def __init__(self, name: str, num: int = None):
        self.name = name
        self.num = num
        self.proc = False

    def execute(self, reg: int, cycle: int) -> tuple[int, int]:
        """Returns new reg value and the new cycle."""
        if self.name == "noop":
            return reg, cycle + 1
        elif self.name == "addx":
            if self.proc:
                self.proc = False
                return reg + self.num, cycle + 1
            else:
                self.proc = True
                return reg, cycle + 1

    def cycles(self) -> int:
        if self.name == "noop":
            return 1
        elif self.name == "addx":
            return 2

        return 0


class CRT:

    def __init__(self):
        self.picture = [
            [
                "X" for _ in range(40)
            ] for _ in range(6)
        ]

    def draw(self, cycle: int, sprite: list[int]) -> None:
        row = ((cycle-2) % 240) // 40
        col = (cycle-2) % 40

        if (cycle-2) % 40 in sprite:
            self.picture[row][col] = "#"
        else:
            self.picture[row][col] = "."


class Day(Problem):

    def load(self) -> list[Instr]:
        with self._load() as f:
            res = []
            for line in f:
                line = line.strip("\n")

                if line == "noop":
                    instr = Instr("noop")
                else:
                    name, num = line.split(" ")
                    instr = Instr(name, int(num))

                res.append(instr)

        return res

    def solution1(self):
        instructions = self.load()
        sig = []

        reg = cycle = 1
        for instr in instructions:
            reg, cycle = instr.execute(reg, cycle)
            if (cycle - 20) % 40 == 0:
                sig.append(reg * cycle)

            while instr.proc:
                reg, cycle = instr.execute(reg, cycle)
                if (cycle - 20) % 40 == 0:
                    sig.append(reg * cycle)

        return sum(sig)

    def solution2(self):
        crt = CRT()
        instructions = self.load()

        reg = cycle = 1
        sprite = lambda: [reg-1, reg, reg+1]

        for instr in instructions:
            reg, cycle = instr.execute(reg, cycle)
            crt.draw(cycle, sprite())

            while instr.proc:
                nxt, cycle = instr.execute(reg, cycle)
                crt.draw(cycle, sprite())
                reg = nxt

        output = ""
        for i in range(len(crt.picture)):
            for j in range(len(crt.picture[i])):
                output += crt.picture[i][j]
            output += "\n"

        return output
