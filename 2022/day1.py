import fileinput


def calories():
    elves
    top = 0
    current = 0
    for line in fileinput.input():
        line = line.strip()
        if not line:
            if current > top:
                top = current

            current = 0
            continue
        current += int(line)
    print(f'Part 1: {top}')
    return top


top = part_1()
