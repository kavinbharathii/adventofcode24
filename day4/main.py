
with open("data.aoc", "r") as file:
    data = [i.strip() for i in file.readlines()]
    file.close()

xmas = "XMAS"
mas = "MAS"

# ---------------------------------------- part 1 ---------------------------------------- # 
xmas_count = 0

# horizontal "-"
for line in data:
    for i in range(len(line) - 3):
        slug = line[i:i + 4]

        if (slug == xmas) or (slug[::-1] == xmas):
            xmas_count += 1

# vertical "|"
for k in range(len(data[0])):
    line = "".join([data[j][k] for j in range(len(data))])
    
    for i in range(len(line) - 3):
        slug = line[i:i + 4]

        if (slug == xmas) or (slug[::-1] == xmas):
            xmas_count += 1

row = 0
col = 0

# positive diagonal "/"
# square matrix | row = col
while (row <= len(data) - 1) or (col <= len(data) - 1):
    start = [row, col]
    r = row
    c = col
    line = ""

    # getting all the elements in the positive diagonal "/"
    while [r, c] != start[::-1]:
        line += data[r][c]
        r -= 1
        c += 1

    line += data[r][c]

    for i in range(len(line) - 3):
        slug = line[i:i + 4]

        if (slug == xmas) or (slug[::-1] == xmas):
            xmas_count += 1

    if row == len(data) - 1 and col == len(data) - 1:
        break
    elif row == len(data) - 1:
        col += 1
    else:
        row += 1

# negative diagonal "\"
row = len(data) - 1
col = 0

while (row >= 0) or (col <= len(data) - 1):
    r = row
    c = col
    line = ""

    while (r < len(data) - 1) and (c < len(data) - 1):
        line += data[r][c]
        r += 1
        c += 1

    line += data[r][c]

    for i in range(len(line) - 3):
        slug = line[i:i + 4]

        if (slug == xmas) or (slug[::-1] == xmas):
            xmas_count += 1

    if row == 0 and col == len(data) - 1:
        break
    elif row == 0:
        col += 1
    else:
        row -= 1

# ---------------------------------------- part 2 ---------------------------------------- # 

mas_count = 0

for i in range(1, len(data) - 1):
    for j in range(1, len(data) - 1):
        if data[i][j] == 'A':
            pos_diagonal = "".join([data[i - 1][j - 1], data[i][j], data[i + 1][j + 1]])
            neg_diagonal = "".join([data[i + 1][j - 1], data[i][j], data[i - 1][j + 1]])

            if (pos_diagonal == mas or pos_diagonal[::-1] == mas) and (neg_diagonal == mas or neg_diagonal[::-1] == mas):
                mas_count += 1


# ---------------------------------------------------------------------------------------- # 

# solution
print(f"Part 1: {xmas_count}")
print(f"Part 2: {mas_count}")

# ---------------------------------------------------------------------------------------- # 
