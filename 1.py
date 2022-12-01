import os

f = '1.txt'
f_file = open(f, encoding='utf-8-sig')
puzzle_input = f_file.read()

values = puzzle_input.split('\n')
