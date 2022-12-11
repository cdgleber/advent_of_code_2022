import re

with open('10.txt') as f:
    puzzle_input = f.read()
    values = puzzle_input.split('\n')

# values = ['noop', 'addx 3', 'addx -5']

X = 1
addx = 1
cycle = 0
num_cycles = 220
instructions = [x.split(' ') for x in values]
instruction_num = 0
instruction_complete = 2
signals = []
signal_strengths = []
CRT = ''
while instruction_num < len(instructions):
    if instruction_complete == cycle:
        if not instruction_num == (len(instructions) - 1):
            instruction_num += 1
        else:
            break
        if not re.search('noop', instructions[instruction_num][0]):
            X = X + addx
            addx = int(instructions[instruction_num][1])
            executing = 'addx'
            instruction_complete = cycle + 2
        else:
            executing = 'noop'
            instruction_complete = cycle + 1
    # print(cycle, instruction_num, instruction_complete, addx, X)

    signals.append(X * cycle)

    if cycle % 40 in (X - 1, X, X + 1):
        print("#", end="")
        CRT += '#'
    else:
        print(".", end="")
        CRT += '.'

    cycle += 1
    
    if cycle % 40 == 0:
        print()
        CRT += '\n'

    print(CRT, X, cycle, instructions[instruction_num][0], addx, cycle % 40 in (X - 1, X, X + 1))

for i, signal in enumerate(signals):
    if ((i+1) / 20) % 2 == 1:
        signal_strengths.append(signal)

# print(instructions, len(instructions))
# print(signal_strengths)
# print(sum(signal_strengths))
print(CRT)

def p2(f):
    X = 1
    t = 0

    print()

    def tick():
        nonlocal t
        if t % 40 in (X - 1, X, X + 1):
            print("#", end="")
        else:
            print(".", end="")
        t += 1
        if t % 40 == 0:
            print()

    for line in f:
        match line.split():
            case ["addx", num]:
                tick()
                tick()
                X += int(num)
            case ["noop"]:
                tick()

p2(values)