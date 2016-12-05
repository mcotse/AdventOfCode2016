import pytest
import re
import string

def solution1(inp):
    id_sum = 0
    parsed = parse_input(inp)
    for line in parsed:
        letters,s_id,checksum = line
        if check_sum(letters,checksum):
            id_sum += s_id
    return id_sum

def solution2(inp):
    parsed = parse_input(inp,no_dash=False)
    rooms = []
    for line in parsed:
        cipher,s_id,checksum = line
        rooms.append((shift_cipher(cipher,s_id),s_id))
    for room in rooms:
        if 'north' in room[0]:
            return room
    raise Exception('404 Room Not found')

def parse_input(inp,no_dash=True):
    inp = inp.split('\n')
    parsed = []
    for line in inp:
        checksum = re.search(r'\[(.*)\]',line).group(1)
        s_id = int(re.search(r'-(\d*)\[',line).group(1))
        letters = re.search(r'(.*)-\d+',line).group(1)
        if no_dash:
            letters = re.sub(r'-','',letters)
        parsed.append((letters,s_id,checksum))
    return parsed

def check_sum(letters,checksum):
    count = {}
    for letter in letters:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    #first sort by key alphabetically then sort by value in reverse
    sorted_alpha = sorted(count.items(),key=lambda x:x[0])
    sorted_value = sorted(sorted_alpha,key=lambda x:x[1],reverse=True)
    return ''.join([x[0] for x in sorted_value][:5]) == checksum

def shift_cipher(cipher,shift_index):
    shift_index = shift_index % 26
    alphabet = string.lowercase
    shift_map = dict(zip(alphabet,alphabet[shift_index:]+alphabet[:shift_index]))
    shift_map['-']=' '
    return ''.join([shift_map[i] for i in cipher])

def test_checksum():
    assert check_sum('aaaaabbbzyx','abxyz') == True
    assert check_sum('notarealroom','oarel') == True

def test_parsed():
    parsed = parse_input('aaaaa-bbb-z-y-x-123[abxyz]')
    letters,s_id,checksum = parsed[0]
    assert letters == 'aaaaabbbzyx'
    assert s_id == 123
    assert checksum == 'abxyz'
    parsed = parse_input('not-a-real-room-404[oarel]')
    letters,s_id,checksum = parsed[0]
    assert letters == 'notarealroom'
    assert s_id == 404
    assert checksum == 'oarel'
    parsed = parse_input('not-a-real-room-404[oarel]',no_dash=False)
    letters,s_id,checksum = parsed[0]
    assert letters == 'not-a-real-room'
    assert s_id == 404
    assert checksum == 'oarel'

def test_solution1():
    assert solution1('aaaaa-bbb-z-y-x-123[abxyz]') == 123
    assert solution1('aaaaa-bbb-z-y-x-123[abxyz]\nnot-a-real-room-404[oarel]') == 527
    assert solution1('totally-real-room-200[decoy]') == 0
    assert solution1('aaaaa-bbb-z-y-x-123[abxyz]\nnot-a-real-room-404[oarel]\ntotally-real-room-200[decoy]') == 527
    assert solution1('aaaaa-bbb-z-y-x-123[abxyz]\nnot-a-real-room-404[oarel]\ntotally-real-room-200[decoy]\na-b-c-d-e-f-g-h-987[abcde]') == 1514

with open('input.txt','r') as f:
    print solution2(f.read()[:-1])
