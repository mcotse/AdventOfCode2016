import pytest

class coordinates:
    def __init__(self):
        self.x = 1
        self.y = 1

    def move(self,d,step):
        # print 'd:',d
        # print 'step:',step
        if d == 'U' or d == 'D':
            if self.in_bounds(self.y+step):
                self.y += step
        elif d == 'L' or d == 'R':
            if self.in_bounds(self.x+step):
                self.x += step
        # print 'coords:', self.x, self.y

    def in_bounds(self,index):
        if -1 < index < 3:
            return True
        else: return False

def solution1(instr):
    code = []
    coord = coordinates()
    numpad = [[1,2,3],[4,5,6],[7,8,9]]
    move_map = {'U':-1,'D':1,'L':-1,'R':1}
    # dir_map = {'U':coord.y,'D':coord.y,'L':coord.x,'R':coord.x}

    # x,y = 1,1
    for instr_row in instr.split('\n'):
        for move in instr_row:
            coord.move(move,move_map[move])
        code.append(numpad[coord.y][coord.x])

    return int(''.join(str(x) for x in code))

def test_answer():
    input1 = '''ULL
RRDDD
LURDL
UUUUD'''
    assert solution1(input1) == 1985
