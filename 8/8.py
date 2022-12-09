import pandas as pd
from math import prod

with open('8.txt') as f:
    puzzle_input = f.read()
    values = puzzle_input.split('\n')

prep = [map(int, list(x)) for x in values]
df = pd.DataFrame(prep)

length = len(df[0])

seen = 0
for row in range(0, length):
    for column in range(0, length):
        horizontal = df.iloc[row]
        horz = horizontal.apply(lambda x: x < horizontal[column])
        vertical = df[column]
        vert = vertical.apply(lambda x: x < vertical[row])
        horz[column] = True
        vert[row] = True
        if all(vert[:row]) or all(vert[row:]) or all(horz[:column]) or all(horz[column:]):
            seen += 1

print(seen)

ans = []
for row in range(0, length):
    for column in range(0, length):
        height = df.iloc[row][column]
        horizontal = df.iloc[row]
        horz = horizontal.apply(lambda x: x < horizontal[column])
        vertical = df[column]
        vert = vertical.apply(lambda x: x < vertical[row])
        horz[column] = True
        vert[row] = True
        ans.append([0, 0, 0, 0])
        for up_row in range(row - 1, -1, -1):
            ans[-1][0] += 1
            if not vert[up_row]:
                break
        for up_col in range(column - 1, -1, -1):
            ans[-1][1] += 1
            if not horz[up_col]:
                break
        for down_row in range(row + 1, length):
            ans[-1][2] += 1
            if not vert[down_row]:
                break
        for down_col in range(column + 1, length):
            ans[-1][3] += 1
            if not horz[down_col]:
                break

print(max(prod(x) for x in ans))




