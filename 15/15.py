import re

with open('14.txt') as f:
    puzzle_input = f.readlines()


Y = 2000000

beacons = set()
intervals = []

for line in puzzle_input:
    signal_x, signal_y, beacon_x, beacon_y = map(int, re.findall(r'\d+', line))

    distance = abs(signal_x - beacon_x) + abs(signal_y - beacon_y)
    offset = distance - abs(signal_y - Y)

    if offset < 0:
        continue

    left_x = signal_x - offset
    right_x = signal_x + offset

    intervals.append((left_x, right_x))

    if beacon_y == Y:
        beacons.add(beacon_x)

cannot = set()
for low, high in intervals:
    for i in range(low, high + 1):
        cannot.add(i)

print(len(cannot) - len(beacons)) # part 1
#
# max = 20
#
# signal_beacon_locations = []
# for line in puzzle_input:
#     signal_x, signal_y, beacon_x, beacon_y = map(int, re.findall(r'\d+', line))
#     signal_beacon_locations.append([signal_x, signal_y, beacon_x, beacon_y])
#
#
# for Y in range(max + 1):
#     cannot = set()
#     intervals = []
#
#     for signal_x, signal_y, beacon_x, beacon_y in signal_beacon_locations:
#
#         distance = abs(signal_x - beacon_x) + abs(signal_y - beacon_y)
#         offset = distance - abs(signal_y - Y)
#
#         if offset < 0:
#             continue
#
#         left_x = signal_x - offset
#         right_x = signal_x + offset
#
#         intervals.append((left_x, right_x))
#
#         if beacon_y == Y:
#             cannot.add(beacon_x)
#
#     for low, high in intervals:
#         for i in range(low, high + 1):
#             cannot.add(i)

