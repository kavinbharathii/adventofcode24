
with open("data.aoc", "r") as file:
    data = file.readlines()
    file.close()

memory = "".join(data)
result_without_conditionals = 0
result_with_conditionals = 0

num = 0
current = ""

insert_mode = False
instructions_enabled = True

pointer = 0

while pointer < len(memory):
    if not insert_mode:
        key = memory[pointer:pointer+7]

        if key[:4] == "do()":
            pointer += 4
            instructions_enabled = True
            continue

        if key[:7] == "don't()":
            pointer += 7
            instructions_enabled = False
            continue

        if key[:4] == "mul(":
            pointer += 4
            insert_mode = True
            continue

        else:
            pointer += 1

    else:
        if memory[pointer].isdigit():
            current += memory[pointer]

        elif memory[pointer] == ",":
            num = int(current)
            current = ""

        elif memory[pointer] == ")":
            if instructions_enabled:
                result_with_conditionals += num * int(current)

            result_without_conditionals += num * int(current)
            current = ""
            num = 0
            insert_mode = False

        else:
            current = ""
            num = 0
            insert_mode = False

        pointer += 1

print(result_without_conditionals)
print(result_with_conditionals)

