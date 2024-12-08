import sys

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

antennae = dict()
antinodes = set()

for r in range(len(data)):
    for c in range(len(data[0])):
        antenna = data[r][c]

        if antenna == '.':
            continue

        if antenna not in antennae:
            antennae[antenna] = [(r, c)]
        else:
            antennae[antenna].append((r, c))

# ---------------------------------------------------- part 1 ---------------------------------------------------- # 

for locations in antennae.values():
    for l1_index, l1 in enumerate(locations[:-1]):
        for l2 in locations[l1_index + 1:]:
            l1r, l1c = l1
            l2r, l2c = l2

            r = l1r - l2r
            c = l1c - l2c

            a1r = l1r + r
            a1c = l1c + c

            if 0 <= a1r < len(data) and 0 <= a1c < len(data[0]):
                a1 = (a1r, a1c)
                antinodes.add(a1)
              
            a2r = l2r - r
            a2c = l2c - c

            if 0 <= a2r < len(data) and 0 <= a2c < len(data[0]):
                a2 = (a2r, a2c)
                antinodes.add(a2)

print(len(antinodes))

# ---------------------------------------------------- part 2 ---------------------------------------------------- # 

for locations in antennae.values():
    for l1_index, l1 in enumerate(locations[:-1]):
        for l2 in locations[l1_index + 1:]:
            l1r, l1c = l1
            l2r, l2c = l2

            r = l1r - l2r
            c = l1c - l2c

            a1r = l1r + r
            a1c = l1c + c

            while 0 <= a1r < len(data) and 0 <= a1c < len(data[0]):
                a1 = (a1r, a1c)
                antinodes.add(a1)
                a1r += r
                a1c += c

            a2r = l2r - r
            a2c = l2c - c

            while 0 <= a2r < len(data) and 0 <= a2c < len(data[0]):
                a2 = (a2r, a2c)
                antinodes.add(a2)
                a2r -= r
                a2c -= c

            antinodes.add(l1)
            antinodes.add(l2)

print(len(antinodes))

# ---------------------------------------------------------------------------------------------------------------- # 
