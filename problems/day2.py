from problems.base import Problem


CNV = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S"
}

RPS = {
    "R": 1,
    "P": 2,
    "S": 3
}

WL = {
    "RR": 3,
    "RP": 6,
    "RS": 0,
    "PR": 0,
    "PP": 3,
    "PS": 6,
    "SR": 6,
    "SP": 0,
    "SS": 3
}

REV = {
    "X": lambda op: "R" if op == "P" else "P" if op == "S" else "S",
    "Y": lambda op: "R" if op == "R" else "P" if op == "P" else "S",
    "Z": lambda op: "R" if op == "S" else "P" if op == "R" else "S"
}


class Day(Problem):

    def load(self) -> list[tuple[str, str]]:
        with self._load(2) as f:
            out = []
            for line in f:
                o, m = line.strip().split(" ")
                out.append((o, m))

            return out

    def solution1(self):
        s = 0
        for op, me in self.load():
            o, m = CNV[op], CNV[me]

            base = RPS[m]
            wl = WL[f"{o}{m}"]

            s += base + wl

        return s

    def solution2(self):
        s = 0
        for opp, res in self.load():
            det = REV[res]
            o, m = CNV[opp], det(CNV[opp])

            base = RPS[m]
            wl = WL[f"{o}{m}"]

            s += base + wl

        return s
