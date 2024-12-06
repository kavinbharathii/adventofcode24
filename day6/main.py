
import sys

if len(sys.argv) == 1:
    with open("data.aoc", "r") as file:
        data = [list(i.strip()) for i in file.readlines()]
        file.close()
else:
    if sys.argv[1] == 'test':
        with open("test.aoc", "r") as file:
            data = [list(i.strip()) for i in file.readlines()]
            file.close()

    else:
        with open("data.aoc", "r") as file:
            data = [list(i.strip()) for i in file.readlines()]
            file.close()

# --------------------------------------------- part 1 --------------------------------------------- #

data_guard_r = 0
data_guard_c = 0

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_direction = 0
distinct_positions = set()
positions_with_directions = []
obstacles = []

for i, line in enumerate(data):
    if '^' in line:
        data_guard_r = i
        data_guard_c = line.index('^')

guard = [data_guard_r, data_guard_c]

# while the guard is still inside the mapped area
while (0 <= guard[0] <= len(data[0]) - 1) and (0 <= guard[1] <= len(data) - 1):
    next_r = guard[0] + directions[current_direction][0]
    next_c = guard[1] + directions[current_direction][1]

    try:
        while data[next_r][next_c] == "#":
            current_direction += 1
            current_direction %= 4

            next_r = guard[0] + directions[current_direction][0]
            next_c = guard[1] + directions[current_direction][1]

    except:
        pass

    distinct_positions.add((guard[0], guard[1]))
    positions_with_directions.append((guard[0], guard[1], current_direction))
    guard[0] += directions[current_direction][0]
    guard[1] += directions[current_direction][1]

print(f"distinct positions: {len(distinct_positions)}")

# --------------------------------------------- part 2 --------------------------------------------- #

obstacles = []

for index, guard_position in enumerate(positions_with_directions[1:]):
    guard_r, guard_c, _ = guard_position

    obstacle = (guard_r, guard_c)

    if obstacle in obstacles:
        continue

    current_direction = 0
    guard = [data_guard_r, data_guard_c]
    new_positions_with_directions = set()


    # while the guard is still inside the mapped area
    while (0 <= guard[0] <= len(data[0]) - 1) and (0 <= guard[1] <= len(data) - 1):
        next_r = guard[0] + directions[current_direction][0]
        next_c = guard[1] + directions[current_direction][1]
        new_positions_with_directions.add((guard[0], guard[1], current_direction))

        try:
            while data[next_r][next_c] == "#" or (next_r, next_c) == obstacle:
                current_direction += 1
                current_direction %= 4

                next_r = guard[0] + directions[current_direction][0]
                next_c = guard[1] + directions[current_direction][1]

        except:
            pass

        guard[0] += directions[current_direction][0]
        guard[1] += directions[current_direction][1]

        if (guard[0], guard[1], current_direction) in new_positions_with_directions:
            obstacles.append(obstacle)
            break

print(f"obstacles: {len(set(obstacles))}")

# --------------------------------------------------------------------------------------------------- #
