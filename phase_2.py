from phase_1 import Node, astar
import random


maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

num_list = [i for i in range(10)]
coordinates = [(x, y) for x in num_list for y in num_list]
for item in [(0, 0), (9, 9), (7, 7), (7, 8), (7, 9), (8, 7)]:
    coordinates.remove(item)
additional_obs = random.sample(coordinates, 20)
for item in additional_obs:
    maze[item[0]][item[1]] = 1
print(maze)

start = (0, 0)
end = (9, 9)

path = astar(maze, start, end)
path = [tuple(reversed(coord)) for coord in path]
print(path)
print(len(path))
