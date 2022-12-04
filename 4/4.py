with open('4.txt') as f:
    puzzle_input = f.read()
    values = puzzle_input.split('\n')

prep1 = [x.split(',') for x in values]

first_elves = [x[0].split('-') for x in prep1]
second_elves = [x[1].split('-') for x in prep1]

pairs = list(zip(first_elves, second_elves))

pairs_contained = 0
for pair in pairs:
    elf_1_start = int(pair[0][0])
    elf_1_end = int(pair[0][1])
    elf_2_start = int(pair[1][0])
    elf_2_end = int(pair[1][1])

    if (elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) \
            or (elf_1_start >= elf_2_start and elf_1_end <= elf_2_end):
        pairs_contained += 1

print(pairs_contained) # part 1 result

overlaps_contained = 0
for pair in pairs:
    elf_1_start = int(pair[0][0])
    elf_1_end = int(pair[0][1])
    elf_2_start = int(pair[1][0])
    elf_2_end = int(pair[1][1])

    elf_1_range = list(range(elf_1_start, elf_1_end+1))
    elf_2_range = list(range(elf_2_start, elf_2_end+1))

    overlaps = list(range(max(elf_1_range[0], elf_2_range[0]), min(elf_1_range[-1], elf_2_range[-1])+1))

    if len(overlaps) > 0:
        overlaps_contained += 1

print(overlaps_contained) # part 2 result




