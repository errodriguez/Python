#!/usr/bin/env python

def solve(s):
    n = len(s)
    pos = set([i for i in range(n) if s[i] == 'B'])
    c = len(pos)  # balls count
    
    if c < 2:
        return -1

    if n < 4 and c<2:
        return -1

    if c > (n+1)//2 :  # not possible
        return -1
    
    ans = n 
    for start in range(n - 2*c + 2):
        curr = 0
        for j in range(start, start + 2*c, 2):
            if j not in pos:
                curr += 1
        ans = min(ans, curr)
    return ans

if __name__ == '__main__':

    assert solve('B.BB.B..B') == 2
    assert solve('..B....B.BB') == 2
    assert solve('BB.B.BBB...') == 4
    assert solve('.BBB.B') == -1
    assert solve('....B.B..') == 0
    assert solve('.') == -1
    assert solve('B') == -1
    assert solve('..') == -1
    assert solve('.B') == -1
    assert solve('B.') == -1
    assert solve('BB') == -1
    assert solve('...') == -1
    assert solve('..B') == -1
    assert solve('.B.') == -1
    assert solve('.BB') == 1
    assert solve('B..') == -1
    assert solve('B.B') == 0
    assert solve('BB.') == 1
    assert solve('BBB') == -1
    assert solve('....') == -1
    assert solve('..B.') == -1
    assert solve('...B') == -1
    assert solve('..BB') == 1
    assert solve('.B..') == -1
    assert solve('.B.B') == 0
    assert solve('.BB.') == 1
    assert solve('.BBB') == -1
    assert solve('B...') == -1
    assert solve('B..B') == 1
    assert solve('B.B.') == 0
    assert solve('B.BB') == -1
    assert solve('BB..') == 1
    assert solve('BB.B') == -1
    assert solve('BBB.') == -1
    assert solve('BBBB') == -1
    assert solve('.....') == -1
    assert solve('....B') == -1
    assert solve('...B.') == -1
    assert solve('...BB') == 1
    assert solve('..B..') == -1
    assert solve('..B.B') == 0
    assert solve('..BB.') == 1
    assert solve('..BBB') == 1
    assert solve('.B...') == -1
    assert solve('.B..B') == 1
    assert solve('.B.B.') == 0
    assert solve('.B.BB') == 2
    assert solve('.BB..') == 1
    assert solve('.BB.B') == 1
    assert solve('.BBB.') == 2
    assert solve('.BBBB') == -1
    assert solve('B....') == -1
    assert solve('B...B') == 1
    assert solve('B..B.') == 1
    assert solve('B..BB') == 1
    assert solve('B.B..') == 0
    assert solve('B.B.B') == 0
    assert solve('B.BB.') == 1
    assert solve('B.BBB') == -1
    assert solve('BB...') == 1
    assert solve('BB..B') == 1
    assert solve('BB.B.') == 2
    assert solve('BB.BB') == -1
    assert solve('BBB..') == 1
    assert solve('BBB.B') == -1
    assert solve('BBBB.') == -1
    assert solve('BBBBB') == -1
