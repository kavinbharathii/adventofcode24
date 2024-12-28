import sys

if len(sys.argv) == 1:
    with open("data.aoc", "r") as file:
        data = file.readline().strip()
        file.close()
else:
    if sys.argv[1] == 'test':
        with open("test.aoc", "r") as file:
            data = file.readline().strip()
            file.close()

    else:
        with open("data.aoc", "r") as file:
            data = file.readline().strip()
            file.close()

res = []
compact_res = []
file_index = 0
period = '.'

for index, num in enumerate(data):
    if index % 2:
        sub_list = [period] * int(num)
    else:
        sub_list = [str(file_index) for _ in range(int(num))]
        file_index += 1

    if sub_list:
        res.extend(sub_list)
        compact_res.append(sub_list)


# ----------------------------------------------------------- part 1 ----------------------------------------------------------- #

p1 = 0
p2 = len(res) - 1
checksum = 0

while p1 < p2:
    if res[p1] == period:
        while res[p2] == period:
            p2 -= 1

        res[p1], res[p2] = res[p2], res[p1]

    checksum += p1 * int(res[p1])
    p1 += 1


print(f"Part 1: {checksum}")

# ----------------------------------------------------------- part 2 ----------------------------------------------------------- #

current_file_index = len(compact_res) - 1


while current_file_index > 0:
    # checking if the current file is a valid file and not an empty space
    while compact_res[current_file_index][0] == period:
        current_file_index -= 1

    file = compact_res[current_file_index]

    index = 0

    while index < current_file_index:
        seg = compact_res[index]
        if seg[0] == period and len(seg) >= len(file):
            compact_res[current_file_index] = [period] * len(file)
            if len(file) == len(seg):
                new_seg = [file]
            else:
                new_seg = [file]
                periods = [period] * (len(seg) - len(file))
                new_seg.append(periods)

            compact_res = compact_res[:index] + new_seg + compact_res[index + 1:]

            # adding one to compensate for adding two elements
            # [I FINALLY SOLVED IT, GODDAMN IT TOOK SO LOOOONG]
            # So when the lengths of the file and the empty space 
            # did not match up, I was adding two lists (the file replacement
            # and the empty space left over)
            # 
            # But when adding the empty space, I overlooked that it's adding 
            # to compact_res list, which will change the current_file_index as well
            # Such a silly error, lost 2 weeks to this though :(
            current_file_index += 1
            break

        index += 1

    current_file_index -= 1

index = 0
checksum = 0

for sub_list in compact_res:
    if sub_list[0] == period:
        index += len(sub_list)
        continue

    for element in sub_list:
        checksum += int(element) * index
        index += 1

print(f"Part 2: {checksum}")
