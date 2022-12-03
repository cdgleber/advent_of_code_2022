with open('3.txt') as f:
    puzzle_input = f.read()
    values = puzzle_input.split('\n')

# START PART 1

items = []
for value in values:
    first = value[:int(len(value)/2)]
    second = value[int(len(value)/2):]
    items.append([first, second])

matches = []

for item in items:
    found = False
    for letter1 in item[0]:
        for letter2 in item[1]:
            if letter1 == letter2:
                matches.append(letter1)
                found = True
                break
        if found:
            break

alphabet = [chr(value) for value in range(ord('a'), ord('a') + 26)]
alphabet = alphabet + [chr(value) for value in range(ord('A'), ord('A') + 26)]

i = list(range(1, 53))
priorities = list(zip(alphabet, i))

scores = []
for match in matches:
    for priority in priorities:
        if match == priority[0]:
            scores.append(priority[1])

print('part 1: ', sum(scores))

# START PART 2

group_size = 3
groups = [values[value:value+group_size] for value in range(0, len(values), group_size)]

badges = []

for group in groups:
    match_1_2 = []
    match_1_3 = []
    match_2_3 = []
    for letter1 in group[0]:
        if group[1].find(letter1) >= 0:
            match_1_2.append(letter1)
        if group[2].find(letter1) >= 0:
            match_1_3.append(letter1)
        if match_1_2 and match_1_3:
            for letter2 in group[1]:
                if letter1 == letter2:
                    if group[2].find(letter2) >= 0:
                        match_2_3.append(letter2)
    match_2_3 = [*set(match_2_3)]
    badges.append(match_2_3)

scores = []
for badge in badges:
    for priority in priorities:
        if badge[0] == priority[0]:
            scores.append(priority[1])

print('part 2: ', sum(scores))