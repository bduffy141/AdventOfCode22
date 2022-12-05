import inspect

from abc import ABC, abstractmethod
from contextlib import contextmanager
from pathlib import Path
from typing import IO


DATA_DIR = Path(__file__).parent.parent / "data"


def latest() -> int:
    """Return the ID number of the furthest dated python file in the problems module."""
    return max(
        int(path.stem.replace("day", ""))
        for path in (Path.cwd() / "problems").iterdir()
        if "day" in path.stem and path.read_text()
    )


class Problem(ABC):

    @contextmanager
    def _load(self, fallback: int = latest()) -> IO:
        data = open(DATA_DIR / f"day{self.id(fallback)}.txt")
        try:
            yield data
        finally:
            data.close()

    @classmethod
    def id(cls, fallback: int) -> int:
        for frm in inspect.stack():
            mod = inspect.getmodule(frm[0])
            if mod and "problems.day" in mod.__name__:
                return int(mod.__name__.rpartition(".")[2].replace("day", ""))

        return fallback

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def solution1(self):
        pass

    @abstractmethod
    def solution2(self):
        pass


# noinspection PyAbstractClass
class Day(Problem):
    pass


# from problems.base import Problem
#
#
# class Day(Problem):
#
#     def load(self):
#         with self._load() as f:
#             pass
#
#     def solution1(self):
#         pass
#
#     def solution2(self):
#         pass
#
