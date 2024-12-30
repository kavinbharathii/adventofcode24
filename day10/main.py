import sys
import typing

if len(sys.argv) == 1:
    with open("data.aoc", "r") as file:
        data = [i.strip() for i in file.readlines()]
        file.close()
else:
    if sys.argv[1] == 'test':
        with open("test.aoc", "r") as file:
            data = [i.strip() for i in file.readlines()]
            file.close()

    else:
        with open("data.aoc", "r") as file:
            data = [i.strip() for i in file.readlines()]
            file.close()

data = [list(map(int, row)) for row in data]
trail_steps = set()

# --------------------------------------------------------------------------------------------------------------------- #

def get_neighbors(row, col):
    neighbors = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc

        if (nr < 0) or (nr > len(data) - 1) or (nc < 0) or (nc > len(data[0]) - 1):
            pass
        else:
            neighbors.append((nr, nc))

    return neighbors

def get_neighbors_with_condition(row, col):
    neighbors = get_neighbors(row, col)
    valid_neighbors = []

    for nr, nc in neighbors:
        # if the value is strictly greater by 1
        if (data[nr][nc] - data[row][col]) == 1:
            valid_neighbors.append((nr, nc))

    return valid_neighbors

# --------------------------------------------------------------------------------------------------------------------- #

def dfs(row, col, trail, score, rating) -> tuple:
    if data[row][col] == 9:

        # if the end is already visited, then this is not new position
        # hence the score is not added, however this it is a distinct path
        # so, the rating is incremented
        if (row, col) in trail_steps:
            rating += 1
            return trail, score, rating

        for step in trail:
            trail_steps.add(step)

        # this is when it a new end position
        rating += 1
        score += 1

    neighbors = get_neighbors_with_condition(row, col)

    for nr, nc in neighbors:
        trail.add((nr, nc))
        trail, score, rating = dfs(nr, nc, trail, score, rating)
        trail.remove((nr, nc))

    return trail, score, rating

# --------------------------------------------------------------------------------------------------------------------- #

total_score = 0
total_rating = 0

for r, row in enumerate(data):
    for c, ele in enumerate(data[r]):
        if ele == 0:
            _, score, rating = dfs(r, c, set(), 0, 0)
            trail_steps = set()
            total_score += score
            total_rating += rating

print(f"Part 1: {total_score}")
print(f"Part 2: {total_rating}")

# --------------------------------------------------------------------------------------------------------------------- #
