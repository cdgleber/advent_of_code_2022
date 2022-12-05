with open('5.txt') as f:
    puzzle_input = f.read()
    values = puzzle_input.split('\n\n')

stacks = values[0]
movements = values[1].split('\n')

# print(stacks)

ms = []
for movement in movements:
    m = {}
    split = movement.split(' ')
    m['move'] = int(split[1])
    m['from'] = int(split[3])
    m['to'] = int(split[5])
    ms.append(m)

s = stacks.split('\n')

ss = [list(x) for x in s]
# sss = list(zip(*ss))


c1 = ''
c2 = ''
c3 = ''
c4 = ''
c5 = ''
c6 = ''
c7 = ''
c8 = ''
c9 = ''

for x in ss:
    try:
        c1 += x[1]
        c2 += x[5]
        c3 += x[9]
        c4 += x[13]
        c5 += x[17]
        c6 += x[21]
        c7 += x[25]
        c8 += x[29]
        c9 += x[33]
    except IndexError:
        continue

final_prep = [c1[:-1], c2[:-1], c3[:-1], c4[:-1], c5[:-1], c6[:-1], c7[:-1], c8[:-1], c9[:-1]]
final = [x.strip() for x in final_prep]
part2_final = [x.strip() for x in final_prep]

# print(ss)
# print(ms)
# print(final)

for move in ms:
    from_index = move['from'] - 1
    to_index = move['to'] - 1
    temp_from = final[from_index]
    temp_to = final[to_index]
    for i in range(move['move']):
        temp_from = final[from_index][1:]
        temp_to = final[from_index][:1] + final[to_index]
        final[from_index] = temp_from
        final[to_index] = temp_to

# print(final)

ans = [x[0] for x in final]
print(''.join(ans)) # print answer for part 1

# print(part2_final)

for move in ms:
    from_index = move['from'] - 1
    to_index = move['to'] - 1
    move_index = move['move']
    temp_from = part2_final[from_index][move_index:]
    temp_to = part2_final[from_index][:move_index] + part2_final[to_index]
    part2_final[from_index] = temp_from
    part2_final[to_index] = temp_to
    # print(temp_from, ' : ', temp_to)
    # break

# print(part2_final)

ans = [x[0] for x in part2_final]
print(''.join(ans)) # print part 2 answer
