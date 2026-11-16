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


def insert_ft(maze: list[list[int]], width: int, height: int) -> None:
	between_ft = int(width / 2)
	print(width)
	print(between_ft)
	center_ft = int(height / 2)
	print(height)
	print(center_ft)
	draw_four(maze, center_ft, between_ft)
	draw_two(maze, center_ft, between_ft)


	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	BOLD = '\033[1m'
	RESET = '\033[0m'

	#print 2D da matriz
	for y in range(height):
		for x in range(width):
			if maze[y][x] == 99:
				print(f"{BLUE}", end="")
			print(maze[y][x], end=" ")
			if maze[y][x] == 99:
				print(f"{RESET}", end="")
		print()

def maze_generator(width: int, height: int) -> list[list[int]]:
	maze = []
	for y in range(height):
		row = []
		for x in range(width):
			row.append(15)
		maze.append(row)
		
	##print 2D da matriz
	#for y in range(height):
	#	for x in range(width):
	#		print(maze[y][x], end=" ")
	#	print()
	#print("---------------------------")

	insert_ft(maze, width, height)
	return maze
