from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from problems.base import Problem


@dataclass
class File:
    name: str
    size: int

    def __eq__(self, other: File):
        return self.name == other.name

    def __hash__(self):
        return hash((self.name, self.size))


class Dir:

    def __init__(self, name: str, parent: Dir | None):
        self.name = name
        self.parent = parent
        self.children: set[Dir | File] = set()

    def __eq__(self, other):
        return self.name == other.name and \
               self.parent == other.parent

    def __hash__(self):
        return hash((self.name, self.parent))

    def child(self, name: str) -> Dir | File | None:
        for child in self.children:
            if child.name == name:
                return child

    def child_dirs(self) -> set[Dir]:
        res = set()
        for child in self.children:
            if isinstance(child, Dir):
                res.add(child)
                res |= child.child_dirs()

        return res

    def size(self) -> int:
        s = 0
        for child in self.children:
            if isinstance(child, File):
                s += child.size
            elif isinstance(child, Dir):
                s += child.size()

        return s


class Day(Problem):

    def load(self) -> Dir:
        root = Dir("/", None)
        curr = root
        with self._load() as f:
            for line in f:
                line: str = line.strip("\n")

                if line == "$ cd /":
                    continue
                elif line.startswith("$ cd "):
                    if ".." in line:
                        curr = curr.parent
                    else:
                        name = line.replace("$ cd ", "")
                        curr = curr.child(name)
                elif line.startswith("$ ls"):
                    continue
                elif line.startswith("dir "):
                    name = line.replace("dir ", "")
                    curr.children.add(Dir(name, curr))
                else:
                    size, name = line.split(" ")
                    curr.children.add(File(name, int(size)))

        return root

        # fs = {}
        # dirs = {"/": {}}
        # path = []
        # ldirs = []
        # # cdir = []
        # # curr
        # with self._load() as f:
        #     for line in f:
        #         line = line.strip("\n")
        #
        #         if line.startswith("$ cd"):
        #             if ".." not in line:
        #                 path.append(line.replace("$ cd ", ""))
        #             else:
        #                 path.pop()
        #             ldirs.clear()
        #             self.init(fs, dirs, ldirs, path)
        #         elif line.startswith("$ ls"):
        #             continue
        #         elif line.startswith("dir"):
        #             dirs[line.replace("dir ", "")] = {}
        #             ldirs.append(line.replace("dir ", ""))
        #             self.init(fs, dirs, ldirs, path)
        #         else:
        #             curr = self.get(fs, path)
        #             size, name = line.split(" ")
        #             curr[name] = int(size)
        #
        # return fs

    def root_size(self, limit: int | None) -> int:
        root = self.load()

        s = 0
        for child in root.child_dirs():
            sz = child.size()
            if limit and sz <= limit:
                s += sz
            elif limit is None:
                s += sz

        return s

    def solution1(self):
        root = self.load()

        s = 0
        for child in root.child_dirs():
            sz = child.size()
            if sz <= 100000:
                s += sz

        return s

    def solution2(self):
        total = 70000000
        needed = 30000000

        root = self.load()
        actual = root.size()
        free = total - actual

        res = set()
        for child in root.child_dirs():
            sz = child.size()
            if sz >= needed - free:
                res.add(child.size())

        return min(res)
