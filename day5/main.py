
with open("data.aoc", "r") as file:
    data = [i.strip() for i in file.readlines()]
    file.close()

space = data.index("")
rules, updates = data[:space], data[space + 1:]

# hacky python parsing
rules = [eval(i.replace('|', ',')) for i in rules]
updates = [list(eval(i)) for i in updates]

middle_sum = 0
corrected_middle_sum = 0

# check to see if the given update sequence is a valid update sequence
def process(update):
    valid_update = True

    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            # if two adjacent page numbers are not in the rules
            if (update[i], update[j]) not in rules:

                # make it an invalid sequence (changes once when there is a invalidity found)
                valid_update = False

                # bubblesort-like sorting to make the update a valid sequence
                # repeatedly reverse couples down the sequence until it is sorted
                update[i], update[j] = update[j], update[i]

    # return the validity and the middle number
    middle = update[len(update) // 2]
    return valid_update, middle

for update in updates:
    valid, middle = process(update)

    if valid:
        middle_sum += middle
    else:
        corrected_middle_sum += middle

print(middle_sum)
print(corrected_middle_sum)
