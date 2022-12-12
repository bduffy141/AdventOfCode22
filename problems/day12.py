from problems.base import Problem


class Day(Problem):

    def load(self) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
        with self._load() as f:
            hmap = []
            for i, line in enumerate(f):
                row = []
                for j, letter in enumerate(line.strip("\n")):
                    if letter == "S":
                        row.append(ord("a")-97)
                        start = i, j
                    elif letter == "E":
                        row.append(ord("z")-97)
                        end = i, j
                    else:
                        row.append(ord(letter)-97)

                hmap.append(row)

            return hmap, start, end

    @staticmethod
    def next(hmap: list[list[int]], coord: tuple[int, int]) -> list[tuple[int, int]]:
        row, col = coord
        val = hmap[row][col]
        valid = []

        if len(hmap[row]) > col+1 and val - hmap[row][col+1] >= -1:
            valid.append((row, col+1))
        if 0 <= col-1 and val - hmap[row][col-1] >= -1:
            valid.append((row, col-1))
        if len(hmap) > row+1 and val - hmap[row+1][col] >= -1:
            valid.append((row+1, col))
        if 0 <= row-1 and val - hmap[row-1][col] >= -1:
            valid.append((row-1, col))

        return valid

    def bfs(self, hmap: list[list[int]], sc: tuple[int, int], ec: tuple[int, int]) -> list[tuple[int, int]]:
        path = [[sc]]
        idx = 0
        visited = {sc}
        if sc == ec:
            return path[0]

        while idx < len(path):
            curr = path[idx]
            last = curr[-1]

            # noinspection PyShadowingBuiltins
            next = self.next(hmap, last)
            if ec in next:
                curr.append(ec)
                return curr
            for nxt in next:
                if nxt not in visited:
                    new = curr[:]
                    new.append(nxt)
                    path.append(new)
                    visited.add(nxt)
            idx += 1
        return []

    def solution1(self):
        hmap, sc, ec = self.load()

        path = self.bfs(hmap, sc, ec)
        return len(path)-1

    def solution2(self):
        hmap, _, ec = self.load()

        scs = [
            (row, col)
            for row, data in enumerate(hmap)
            for col, val in enumerate(data)
            if val == 0
        ]

        path = min([
            p
            for sc in scs
            if (p := self.bfs(hmap, sc, ec))
        ], key=len)

        return len(path)-1
