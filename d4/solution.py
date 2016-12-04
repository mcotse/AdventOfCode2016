import pytest
import re
def parse_input(inp):
    inp = inp.split('\n')
    parsed = []
    for line in inp:
        checksum = re.search(r'\[(.*)\]',line).group(1)
        s_id = int(re.search(r'-(\d*)\[',line).group(1))
        letters = re.search(r'(.*)-\d+',line).group(1)
        letters = re.sub(r'-','',letters)
        parsed.append((letters,s_id,checksum))
    return parsed
    
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
