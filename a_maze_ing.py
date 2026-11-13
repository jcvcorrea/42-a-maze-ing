import sys
from typing import Tuple, TypeAlias
ConfigValue: TypeAlias = int | str | bool | dict[str, int] | None


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

    print_config(config)

    if None in config.values():
        print("Configuracao incompleta")
    else:
        print("Todos os valores validos")


def reading_config(
        lines: list[str],
        config: dict[str, ConfigValue]
        ) -> Tuple[bool, str]:
    try:
        for line in lines:
            if line[-1] == '\n':
                line = line[:-1]
            if line.find("=") > 0 and not line[-1] == "=":
                key = line[:line.find("=")].lower()
                if key in config.keys():
                    value = line[line.find("=")+1:]
                    config[key] = validate_values(key, value)
        return (True, "")
    except ValueError:
        return (False, "Valor invalido em configuração")


def validate_values(
        key: str,
        value: str
        ) -> ConfigValue:
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
