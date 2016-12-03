import pytest

class coordinates():
    def __init__(self,x=0,y=0,direction='N'):
        self.x = x
        self.y = y
        self.dir = direction

    def move(self,axis,increment):
        if axis == 'x':
            self.x += increment
        elif axis == 'y':
            self.y += increment

    def dist_from_origin(self):
        return abs(self.x)+abs(self.y)

    def turn(self,direction):
        #Can be done mapping all this to a dictionary to improve speed, but kept this format for the sake of readability
        if self.dir == 'N':
            self.dir = 'W' if direction == 'L' else 'E'
        elif self.dir == 'W':
            self.dir = 'S' if direction == 'L' else 'N'
        elif self.dir == 'S':
            self.dir = 'E' if direction == 'L' else 'W'
        elif self.dir == 'E':
            self.dir = 'N' if direction == 'L' else 'S'

def p1_solution(instr):
    instr = instr.split(', ')
    coord = coordinates()
    dir_to_axis = {'N':('y',1),'S':('y',-1),'E':('x',1),'W':('x',-1)}

    for line in instr:
        direction,advance = line[0],int(line[1:])
        coord.turn(direction)
        axis, prefex = dir_to_axis[coord.dir]
        coord.move(axis,prefex*advance)

    return coord.dist_from_origin()


def test_answer():
    assert p1_solution('R2, L3') == 5
    assert p1_solution('R2, R2, R2') == 2
    assert p1_solution('R5, L5, R5, R3') == 12
    assert p1_solution('R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4') == 268
    #below is the numerical p1_solution to the question
    assert p1_solution('L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2') == 279

    assert p2_solution('R8, R4, R4, R8') == 4
    assert p2_solution('R8, R5, R4, R8') == 4
    assert p2_solution('R8, R4, R5, R8') == 3
    assert p2_solution('R1, R1, R1, R1') == 0
