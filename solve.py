#!/usr/bin/env python

import click

from problems import *


@click.command()
@click.option("-d", "--day", type=int, default=latest())
def cli(day: int):
    problem = globals()[f"day{day}"].Day()
    header = lambda n: click.style(f"Solution {n}", fg="red", bold=True, underline=True)

    print(click.style(f"Day {day}", bold=True))

    print(f"{header(1)}:")
    print(problem.solution1())

    print(f"\n{header(2)}:")
    print(problem.solution2())


if __name__ == '__main__':
    cli()
