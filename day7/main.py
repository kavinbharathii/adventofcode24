
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

total_calibration = 0

for line in data:
    total, sequence = line.split(": ")
    total = int(total)
    sequence = list(map(int, sequence.split(" ")))

    # possible answers
    current_possibilities = []
    next_possibilities = []

    for num in sequence:
        if not current_possibilities:
            next_possibilities.append(num)

        else:
            for prev_num in current_possibilities:
                # add result
                add_result = prev_num + num

                # multiplication result
                mul_result = prev_num * num

                # concatenation result
                con_result = int(f"{prev_num}{num}")

                next_possibilities.append(add_result)
                next_possibilities.append(mul_result)
                next_possibilities.append(con_result)

        current_possibilities = next_possibilities
        next_possibilities = []

    if total in current_possibilities:
        total_calibration += total

print(total_calibration)