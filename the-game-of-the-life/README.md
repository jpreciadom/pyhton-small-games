# Conway's Game of Life

This is a project to emulate the game [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), a zero-player game where the evolution is determined by its initial state, requiring no further inputs.

The universe of the game is an infinite, two-dimensional orthogonal grid of square cells, each of which is one of two possible states: live or death. For this design, we opted for a 200x200 grid size connected at the limits.

## Project Requisites
* Install [poetry](https://python-poetry.org/docs/).

## Setup

### Install dependencies
```
poetry install
```

## Run the project
```
poetry run python src/main.py
```
