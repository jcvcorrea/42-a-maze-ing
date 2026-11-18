*This project has been created as part of the 42 curriculum by hequeiro, jcorrea.*

# A-Maze-ing

## Description

A-Maze-ing is a Python project developed as part of the 42 Common Core curriculum.

The goal is to create a maze generator capable of producing valid mazes from a configuration file, finding a path between the entrance and exit, and displaying the result visually.

The project explores algorithms, graph theory, recursion, data structures, file handling, and modular programming.

### Project Requirements

The completed program must support:

- Random maze generation with reproducibility through a seed.
- Perfect mazes with a unique path and non-perfect mazes with multiple routes.
- Connected corridors and consistent walls.
- A visible "42" pattern made of fully closed cells, when dimensions allow.
- Shortest-path calculation between entrance and exit.
- Hexadecimal representation of maze walls.
- Interactive visualization using MiniLibX.
- A reusable maze-generation module.

## Instructions

### Requirements

- Python 3.10 or later
- Project dependencies specified in the repository
- Make
- flake8 and mypy for code validation

### Running the project

The program accepts a configuration file as its argument.

`python3 a_maze_ing.py config.txt`

Alternatively, use the Makefile:

`make run`

### Development commands

- `make install` — Install project dependencies.
- `make run` — Execute the program.
- `make debug` — Run the program in debug mode.
- `make lint` — Check code style and typing.
- `make lint-strict` — Run stricter checks.
- `make clean` — Remove temporary files.

## Configuration File

The configuration uses one `KEY=VALUE` pair per line.

Example:

```ini
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=False
```

### Parameters

| Parameter | Description |
|---|---|
| `WIDTH` | Maze width in cells |
| `HEIGHT` | Maze height in cells |
| `ENTRY` | Entrance coordinates (x,y) |
| `EXIT` | Exit coordinates (x,y) |
| `OUTPUT_FILE` | Generated maze output filename |
| `PERFECT` | Enables or disables perfect-maze generation |

All six parameters are mandatory. Lines beginning with `#` are treated as comments.

Additional parameters, such as a random seed, may be supported.

## Maze Representation

Each cell uses four bits to represent its walls:

| Bit | Direction | Value |
|---|---|---|
| 0 | North | 1 |
| 1 | East | 2 |
| 2 | South | 4 |
| 3 | West | 8 |

A value of `1` indicates a closed wall; `0` indicates an open wall.

For example, hexadecimal `F` represents a cell with all four walls closed.

The final output file will contain the hexadecimal maze representation, entrance and exit coordinates, and a shortest valid path using the directions N, E, S and W.

## Maze Generation Algorithm

**Status: Under development.**

The generation algorithm and its selection rationale will be documented here after implementation and validation.

The final implementation must preserve maze connectivity, prevent inconsistent shared walls, and respect the selected generation mode.

## Code Reusability

The project will provide a reusable `MazeGenerator` class in a standalone Python module.

The reusable module must allow another project to generate mazes using custom parameters, access the generated structure, and retrieve a solution.

**Pending:** Add the actual class usage example, custom parameter instructions, and package installation details after the reusable module is implemented.

## Team and Project Management

### Team Members

**jcorrea**
- Configuration file parsing.
- Input validation and error handling.
- Initial maze grid implementation.
- Documentation and integration.

**hequeiro**
- Graphical interface using MiniLibX.
- Maze visualization.
- Visual interaction development.

Both members participate in project design, integration, testing, and technical decisions.

### Development Plan

The development is organized into stages:

1. Repository setup and configuration handling.
2. Initial grid representation and validation.
3. Maze generation algorithms and connectivity.
4. Graphical interface and user interactions.
5. Reusable module and package creation.
6. Integration, testing, and documentation.

### Project Evolution

The first development stage focused on configuration parsing, type validation, exception handling, and creating the initial grid.

The graphical interface is being developed in parallel to support integration with the maze generator.

**To be updated before submission:** Changes to the original plan, challenges encountered, successful approaches, and possible improvements.

### Tools

- Python
- Git and GitHub
- Make
- flake8
- mypy
- MiniLibX (graphical interface)

## Resources

### References

- [Python Documentation](https://docs.python.org/3/)
- [Python typing documentation](https://docs.python.org/3/library/typing.html)
- [Python exceptions documentation](https://docs.python.org/3/tutorial/errors.html)
- A-Maze-ing official subject, version 2.3

Additional references for the selected maze-generation algorithm will be included when the algorithm is finalized.

### AI Usage

AI was used as a learning and development support tool for:

- Understanding Python concepts and control flow.
- Reviewing configuration parsing and exception handling.
- Discussing input validation and edge cases.

The team remains responsible for understanding, implementing, testing, and validating the submitted code.

## Project Status

**Work in progress.**

Configuration parsing, initial validation, and grid representation are under development and testing. Maze generation, graphical integration, packaging, and final validation remain to be completed.