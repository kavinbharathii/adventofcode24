import sys

if len(sys.argv) == 1:
    with open("data.aoc", "r") as file:
        data = [n for n in file.readline().strip().split(' ')]
        file.close()
else:
    if sys.argv[1] == 'test':
        with open("test.aoc", "r") as file:
            data = [n for n in file.readline().strip().split(' ')]
            file.close()

    else:
        with open("data.aoc", "r") as file:
            data = [n for n in file.readline().strip().split(' ')]
            file.close()

# ------------------------------------------------------------------------------------------------------------------- #

next_blink = ""
lookup = dict()

for blink in range(75):
    print(blink, len(data), " ".join(data[:5]))
    for num in data:
        if num in lookup.keys():
            next_blink += lookup[num] + " "
        else:
            if num == '0':
                result = '1'
            elif len(num) % 2 == 0:
                l, r = num[:len(num) // 2], num[len(num) // 2:]
                result = l
                result += " " + (r.lstrip('0') or '0')
            else:
                stone = int(num) * 2024
                result = str(stone)
    
            lookup[num] = result
            next_blink += result + " "

    next_blink = next_blink.strip(" ")
    data = next_blink.split(" ")
    next_blink = ""

print(len(data))


# ------------------------------------------------------------------------------------------------------------------- #
