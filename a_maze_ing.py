from using_types import ConfigValue
from using_types import MazeConfig
import sys
from typing import Tuple
import maze_grid


def main() -> None:
    if len(sys.argv) != 2:
        return print("falta arquivo")

    config: dict[str, ConfigValue] = {
        "width": None,
        "height": None,
        "entry": None,
        "exit": None,
        "output_file": None,
        "perfect": None
    }

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError as file_error:
        return print(file_error)
    except PermissionError as perm_error:
        return print(perm_error)

    status, message = reading_config(lines, config)
    if not status:
        return print(message)

    width = config["width"]
    height = config["height"]
    entry = config["entry"]
    exit_point = config["exit"]
    output_file = config["output_file"]
    perfect = config["perfect"]

    try:
        if (
            not isinstance(width, int) or
            not isinstance(height, int) or
            not isinstance(entry, dict) or
            not isinstance(exit_point, dict) or
            not isinstance(output_file, str) or
            not isinstance(perfect, bool)
        ):
            raise TypeError("Erro de Configuração - Configuração inválidas")

        if (
            not 0 <= entry["x"] < width or
            not 0 <= entry["y"] < height
        ):
            raise ValueError("Erro de Configuração - Entrada impossível")

        if (
            not 0 <= exit_point["x"] < width or
            not 0 <= exit_point["y"] < height
        ):
            raise ValueError("Erro de Configuração - Saída impossível")

        if (
            not width > 8 or
            not height > 6
        ):
            raise ValueError("Erro de Configuração - Maze menor que mínimo")

        if entry == exit_point:
            raise ValueError("Erro de Configuração - Entrada e Saída iguais")
    except (ValueError, TypeError) as config_error:
        return print(config_error)

    maze_config = MazeConfig(
            width=width,
            height=height,
            entry=entry,
            exit=exit_point,
            output_file=output_file,
            perfect=perfect
            )

    print_config(config)

    if None in config.values():
        print("Configuracao incompleta")
    else:
        print("Todos os valores validos")
    try:
        maze_grid.maze_generator(maze_config)
    except (ValueError) as maze_generator_error:
        return print(maze_generator_error)


def reading_config(
        lines: list[str],
        config: dict[str, ConfigValue]
        ) -> Tuple[bool, str]:
    try:
        for line in lines:
            if not line or line[0] == '\n' or line[0] == '#':
                continue
            if line[-1] == '\n':
                line = line[:-1]
            if not (line.find("=") > 0 and not line[-1] == "="):
                return (False, "Sintaxe inválida em configuralção")
            key = line[:line.find("=")].lower()
            if key in config.keys():
                value = line[line.find("=")+1:]
                config[key] = validate_values(key, value)
        return (True, "")
    except ValueError:
        return (False, "Valor inválido em configuração")


def validate_values(key: str, value: str) -> ConfigValue:
    if (key == "width" or key == "height") and int(value) > 0:
        return int(value)
    elif key == "perfect" and value == "True":
        return bool(1)
    elif key == "perfect" and value == "False":
        return bool(0)
    elif (key == "entry" or key == "exit") and value is not None:
        return {
            "x": int(value[:value.find(",")]),
            "y": int(value[value.find(",") + 1:])
        }
    elif key == "output_file" and value is not None:
        return value
    else:
        return None


def print_config(config: dict[str, ConfigValue]) -> None:
    for key, value in config.items():
        print(f"{key}: {value} | Tipo: {type(value)}")


if __name__ == "__main__":
    main()
