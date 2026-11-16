PYTHON = python3

NAME = a_maze_ing.py 

CONFIG = config.txt

run:
	$(PYTHON) $(NAME) $(CONFIG)

debug:
	python3 -m pdb a_maze_ing.py config.txt