from collections import deque
import re
from math import prod


def run_operation(old_num, op_string, op_num):
    if op_num == 'old':
        return old_num * old_num
    else:
        match op_string:
            case '*':
                return old_num * op_num
            case '+':
                return old_num + op_num


with open('11.txt') as f:
    puzzle_input = f.read()
    monkeys = puzzle_input.split('\n\n')

for i, m in enumerate(monkeys):
    monkey = {}
    mm = m.split('\n')
    monkey['index'] = int(re.findall(r'\d+', mm[0])[0])
    monkey['items'] = deque(re.findall(r'\d+', mm[1]))
    monkey['operation'] = re.findall(r'[\*\+]', mm[2])[0]
    if re.search(r'\d+', mm[2]):
        monkey['op_num'] = int(re.findall(r'\d+', mm[2])[0])
    else:
        monkey['op_num'] = 'old'
    monkey['test'] = int(re.findall(r'\d+', mm[3])[0])
    monkey['throw_true'] = int(re.findall(r'\d+', mm[4])[0])
    monkey['throw_false'] = int(re.findall(r'\d+', mm[5])[0])
    monkey['num_inspections'] = 0
    monkeys[i] = monkey

# PART I

for iteration in range(20):
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            item = int(monkey['items'].popleft())
            worry = run_operation(item, monkey['operation'], monkey['op_num'])
            worry = worry // 3
            if worry % monkey['test'] == 0:
                monkeys[monkey['throw_true']]['items'].append(worry)
            else:
                monkeys[monkey['throw_false']]['items'].append(worry)
            monkey['num_inspections'] += 1

insp_counts = []
for monkey in monkeys:
    insp_counts.append(monkey['num_inspections'])
insp_counts.sort(reverse=True)

print(insp_counts[0]*insp_counts[1])

# PART II

with open('11.txt') as f:
    puzzle_input = f.read()
    monkeys = puzzle_input.split('\n\n')

for i, m in enumerate(monkeys):
    monkey = {}
    mm = m.split('\n')
    monkey['index'] = int(re.findall(r'\d+', mm[0])[0])
    monkey['items'] = deque(re.findall(r'\d+', mm[1]))
    monkey['operation'] = re.findall(r'[\*\+]', mm[2])[0]
    if re.search(r'\d+', mm[2]):
        monkey['op_num'] = int(re.findall(r'\d+', mm[2])[0])
    else:
        monkey['op_num'] = 'old'
    monkey['test'] = int(re.findall(r'\d+', mm[3])[0])
    monkey['throw_true'] = int(re.findall(r'\d+', mm[4])[0])
    monkey['throw_false'] = int(re.findall(r'\d+', mm[5])[0])
    monkey['num_inspections'] = 0
    monkeys[i] = monkey

mod = prod(m["test"] for m in monkeys)

for iteration in range(10000):
    for monkey in monkeys:
        while len(monkey['items']) > 0:
            item = int(monkey['items'].popleft())
            worry = run_operation(item, monkey['operation'], monkey['op_num']) % mod
            if worry % monkey['test'] == 0:
                monkeys[monkey['throw_true']]['items'].append(worry)
            else:
                monkeys[monkey['throw_false']]['items'].append(worry)
            monkey['num_inspections'] += 1

insp_counts = []
for monkey in monkeys:
    insp_counts.append(monkey['num_inspections'])
insp_counts.sort(reverse=True)

print(insp_counts[0]*insp_counts[1])