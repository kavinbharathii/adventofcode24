
with open("data.aoc") as file:
    data = file.readlines()
    file.close()

historian = []
remake = []

for line in data:
    h, r = [int(i) for i in line.split()]
    historian.append(h)
    remake.append(r)

historian.sort()
remake.sort()

total_distance = 0
similarity_score = 0

for h, r in zip(historian, remake):
    total_distance += abs(h - r)

for h in historian:
    similarity_score += h * remake.count(h)

print(total_distance)
print(similarity_score)
