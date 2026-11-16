PYTHON = python3

NAME = a_maze_ing.py 

CONFIG = config.txt

REMOVE = __pycache__ .mypy_cache

run:
	$(PYTHON) $(NAME) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(NAME) $(CONFIG)

clean:
	rm -rf $(REMOVE)

lint:


install:

.PHONY: run debug clean