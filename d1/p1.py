import pytest

def turn(curr,dir):
    #TODO: optimize this instead of hardcoding
    # cardinal = dict(zip(['N','E','S','W',1,2,3,4],[1,2,3,4,'N','E','S','W']))
    if curr == 'N':
        return 'W' if dir == 'L' else 'E'
    if curr == 'W':
        return 'S' if dir == 'L' else 'N'
    if curr == 'S':
        return 'E' if dir == 'L' else 'W'
    if curr == 'E':
        return 'N' if dir == 'L' else 'S'

def calc_total(steps_in_dir):
    #TODO: generalize this instead of hardcoding
    virtical_steps = abs(steps_in_dir['N']-steps_in_dir['S'])
    horizontal_steps = abs(steps_in_dir['E']-steps_in_dir['W'])
    return virtical_steps + horizontal_steps

def solution(steps):
    steps = steps.split(', ')
    curr_dir = 'N'
    steps_in_dir = dict(zip(['N','E','S','W'],[0,0,0,0]))

    for step in steps:
        direction,advance = step[0],int(step[1:])
        curr_dir = turn(curr_dir,direction)
        steps_in_dir[curr_dir] += advance

    return calc_total(steps_in_dir)

def test_answer():
    assert solution('R2, L3') == 5
    assert solution('R2, R2, R2') == 2
    assert solution('R5, L5, R5, R3') == 12
    assert solution('R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4') == 268
    #below is the numerical solution to the question
    assert solution('L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2') == 279
