from collections import Counter

with open('6.txt') as f:
    puzzle_input = f.readlines()

signal = puzzle_input[0]

for c in range(0, len(signal)):
    search = signal[c:c+4]
    counts = Counter(search)
    if all([x == 1 for x in counts.values()]):
        ans = c+4
        break

print(ans) # part 1

for c in range(0, len(signal)):
    search = signal[c:c+14]
    counts = Counter(search)
    if all([x == 1 for x in counts.values()]):
        ans = c+14
        break

print(ans) # part 2