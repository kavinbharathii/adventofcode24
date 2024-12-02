
with open("data.aoc") as file:
    data = file.readlines()
    file.close()

safe_count = 0

def check_validity(report):
    inc = None
    dec = None
    safe = True

    for i in range(len(report) - 1):
        a = report[i]
        b = report[i + 1]

        if not inc and not dec:
            if a - b > 0:
                dec = True
            elif a - b < 0:
                inc = True
            else:
                safe = False
                break

        if (a - b > 0) and inc:
            safe = False
            break

        if (a - b < 0) and dec:
            safe = False
            break

        if abs(a - b) > 3 or abs(a - b) < 1:
            safe = False
            break

    return safe


for line in data:
    report = [int(i) for i in line.split()]

    safe = check_validity(report)
    
    if safe:
        safe_count += 1

    else:
        for i in range(len(report)):
            safe = check_validity(report[:i] + report[i + 1:])

            if safe:
                safe_count += 1
                break

print(safe_count)