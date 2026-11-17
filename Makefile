PYTHON = python3
NAME = a_maze_ing.py 
EXTRA_FILES = maze_grid.py using_types.py
CONFIG = config.txt
REMOVE = __pycache__ .mypy_cache
VENV = .venv/bin/

run:
	$(PYTHON) $(NAME) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(NAME) $(CONFIG)

clean:
	rm -rf $(REMOVE)

lint:
	$(VENV)flake8 $(NAME) $(EXTRA_FILES)
	$(VENV)mypy $(NAME) $(EXTRA_FILES) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(VENV)flake8 $(NAME) $(EXTRA_FILES)
	$(VENV)mypy $(NAME) $(EXTRA_FILES) --strict

install:
	python3 -m venv .venv
	$(VENV)python -m pip install mypy
	$(VENV)python -m pip install flake8

.PHONY: run debug clean lint lint-strict install