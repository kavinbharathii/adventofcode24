import sys

if len(sys.argv) == 1:
    with open("data.aoc", "r") as file:
        data = [n for n in file.readline().split(' ')]
        file.close()
else:
    if sys.argv[1] == 'test':
        with open("test.aoc", "r") as file:
            data = [n for n in file.readline().split(' ')]
            file.close()

    else:
        with open("data.aoc", "r") as file:
            data = [n for n in file.readline().split(' ')]
            file.close()

# ------------------------------------------------------------------------------------------------------------------- #

next_blink = []

for blink in range(75):
    print(blink + 1, len(data))
    for num in data:
        if num == '0':
            next_blink.append('1')
        elif len(num) % 2 == 0:
            l, r = num[:len(num) // 2], num[len(num) // 2:]
            next_blink.append(l)
            next_blink.append(r.lstrip('0') or '0')
        else:
            stone = int(num) * 2024
            next_blink.append(str(stone))

    data = next_blink
    next_blink = []

print(len(data))


# ------------------------------------------------------------------------------------------------------------------- #
