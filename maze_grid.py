from using_types import MazeConfig


def draw_four(maze: list[list[int]], center_ft: int, between_ft: int) -> None:
    maze[center_ft-2][between_ft-3] = 99
    maze[center_ft-1][between_ft-3] = 99
    maze[center_ft-2][between_ft-1] = 99
    maze[center_ft-1][between_ft-1] = 99
    maze[center_ft][between_ft-1] = 99
    maze[center_ft][between_ft-2] = 99
    maze[center_ft][between_ft-3] = 99
    maze[center_ft+1][between_ft-1] = 99
    maze[center_ft+2][between_ft-1] = 99


def draw_two(maze: list[list[int]], center_ft: int, between_ft: int) -> None:
    maze[center_ft][between_ft+1] = 99
    maze[center_ft][between_ft+2] = 99
    maze[center_ft][between_ft+3] = 99
    maze[center_ft-2][between_ft+1] = 99
    maze[center_ft-2][between_ft+2] = 99
    maze[center_ft-2][between_ft+3] = 99
    maze[center_ft-1][between_ft+3] = 99
    maze[center_ft+1][between_ft+1] = 99
    maze[center_ft+2][between_ft+1] = 99
    maze[center_ft+2][between_ft+2] = 99
    maze[center_ft+2][between_ft+3] = 99


def insert_ft_entry_exit(
        maze: list[list[int]],
        config: MazeConfig
        ) -> None:

    between_ft = (config.width // 2)
    print(config.width)
    print(between_ft)
    center_ft = (config.height // 2)
    print(config.height)
    print(center_ft)
    draw_four(maze, center_ft, between_ft)
    draw_two(maze, center_ft, between_ft)
    if (maze[config.entry["y"]][config.entry["x"]] == 99 or
            maze[config.exit["y"]][config.exit["x"]] == 99):
        raise ValueError("Erro: Entrada ou Saída coincide com 42")
    else:
        maze[config.entry["y"]][config.entry["x"]] = 77
        maze[config.exit["y"]][config.exit["x"]] = 88


def print_maze(maze: list[list[int]]) -> None:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'

    for line in maze:
        for num in line:
            if num == 99:
                print(f"{BLUE}{num}{RESET} ", end="")
            elif num == 77:
                print(f"{GREEN}{num}{RESET} ", end="")
            elif num == 88:
                print(f"{RED}{num}{RESET} ", end="")
            else:
                print(f"{num} ", end="")
        print()


def maze_generator(config: MazeConfig) -> list[list[int]]:
    maze = []
    for y in range(config.height):
        row = []
        for x in range(config.width):
            row.append(15)
        maze.append(row)

    insert_ft_entry_exit(maze, config)
    print_maze(maze)
    return maze
