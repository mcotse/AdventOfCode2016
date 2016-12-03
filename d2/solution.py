import pytest

class coordinates:
    def __init__(self,x=1,y=1,numpad=[[1,2,3],[4,5,6],[7,8,9]]):
        self.x = x
        self.y = y
        self.numpad = numpad
        self.size = len(numpad)

    def move(self,d,step):
        if d == 'U' or d == 'D':
            if self.in_bounds(self.y+step,self.y):
                self.y += step
        elif d == 'L' or d == 'R':
            if self.in_bounds(self.x+step,self.x):
                self.x += step

    def in_bounds(self,index,axis):
        if (-1 < index < self.size):
            if axis == self.y and self.numpad[index][self.x]:
                return True
            elif axis == self.x and self.numpad[self.y][index]:
                return True
        return False

    def get_curr(self):
        return self.numpad[self.y][self.x]

def solution1(instr):
    code = []
    coord = coordinates()
    move_map = {'U':-1,'D':1,'L':-1,'R':1}

    for instr_row in instr.split('\n'):
        for move in instr_row:
            coord.move(move,move_map[move])
        code.append(coord.get_curr())

    return int(''.join(str(x) for x in code))

def test_answer():
    input1 = '''ULL
RRDDD
LURDL
UUUUD'''
    assert solution1(input1) == 1985
