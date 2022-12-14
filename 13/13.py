with open('13.txt') as f:
    puzzle_input = f.read()
    pairs_raw = puzzle_input.split('\n\n')

pairs = [[eval(x) for x in pair.splitlines()] for pair in pairs_raw]


def recursive_compare(left, right):
    # if integers, compare and add index if Left side is smaller
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    # if left and right are both lists, zip to connect comparable lists
    # then recursively apply through all occurrences until top conditional
    # is met
    if isinstance(left, list) and isinstance(right, list):
        for next_left, next_right in zip(left, right):
            if result := recursive_compare(next_left, next_right):
                return result
        return len(left) - len(right)

    # Mixed types; convert right to list and retry comparison
    if isinstance(left, list):
        return recursive_compare(left, [right])

    # Mixed types; convert right to list and retry comparison
    if isinstance(right, list):
        return recursive_compare([left], right)

    assert False


ans = 0

for i, (left, right) in enumerate(pairs):
    if recursive_compare(left, right) < 0:
        ans += i + 1

print(ans)

with open('13.txt') as f:
    puzzle_input = f.read()

pairs = [eval(x) for x in puzzle_input.splitlines() if len(x) > 0]

index_of_2 = 1 # earliest index that is possible for 2
index_of_6 = 2 # earliest index that is possible for 6

# find the index for 2 and 6 using recursive search
for pair in pairs:
    if recursive_compare(pair, [[2]]) < 0:
        index_of_2 += 1
        index_of_6 += 1
    elif recursive_compare(pair, [[6]]) < 0:
        index_of_6 += 1

decoder_key = index_of_2 * index_of_6

print(decoder_key)