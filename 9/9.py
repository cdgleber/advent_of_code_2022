import itertools

with open('9.txt') as f:
    puzzle_input = f.read()
    values = puzzle_input.split('\n')

steps = [x.split(' ') for x in values]

H = [0, 0]
T = [0, 0]

H_locs = []
T_locs = []
all_moves = set((0,0))

for move in steps:
    step = int(move[1])
    steps = []
    x, y = H
    previous_loc = [x, y]
    tx, ty = T
    match move[0]:
        case 'U':
            y += step
            previous_loc = [x, y - 1]
        case 'D':
            y -= step
            previous_loc = [x, y + 1]
        case 'L':
            x -= step
            previous_loc = [x + 1, y]
        case 'R':
            x += step
            previous_loc = [x - 1, y]

    H = [x, y]

    check = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1]
            , [x - 1, y],    [x, y],      [x + 1, y]
            , [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]

    # print(tx, ty, check)

    if [tx, ty] not in check:
        T = previous_loc
        match move[0]:
            case 'U':
                for i in range(step):
                    all_moves.add((previous_loc[0], ty + i))
            case 'D':
                for i in range(step):
                    all_moves.add((previous_loc[0], ty - i))
            case 'L':
                for i in range(step):
                    all_moves.add((tx - i, previous_loc[1]))
            case 'R':
                for i in range(step):
                    all_moves.add((tx + i, previous_loc[1]))


    H_locs.append(H)
    T_locs.append(T)
    # print(H, " : ", T, " : ", all_moves)
    # if len(H_locs) > 10:
    #     break

ulocs = []
for loc in T_locs:
    if loc not in ulocs:
        ulocs.append(loc)

# print(H_locs)
# print(T_locs)
# print(ulocs)
print(len(all_moves))
