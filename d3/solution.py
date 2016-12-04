import pytest
import re

def solution1(instr):
    instr = parse_input(instr)
    n_possible = 0
    for sides in instr:
        if valid_triangle(sides):
            n_possible += 1
    return n_possible

def parse_input(inp):
    inp = inp.split('\n')
    inp = [[line[:3],line[5:8],line[10:13]] for line in inp]
    for line in inp:
        for i in range(len(line)):
            try:
                line[i] = int(re.sub('\s+','',line[i]))
            except:
                print line[i], 'failed to parse'
    return inp

def valid_triangle(sides):
    for i in range(-1,len(sides)-1):
        if sides[i]+sides[i+1] <= sides[i-1]:
            return False
    return True

def test():
    assert solution1('  5   10   25') == 0
    assert solution1('  3    4    5') == 1
    assert solution1('  3    4    5\n  5   10   25') == 1
    assert solution1('541  588  421\n827  272  126\n660  514  367\n 39  703  839') == 2

with open('input.txt','r') as f:
    print solution1(f.read()[:-1])
