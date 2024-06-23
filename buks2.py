#!/usr/bin/env python

def movs(p):
    return 0 if p.count('B')<2 else 1


def solve(l,u):
    if len(l)>3:
        return sum(solve(l[:len(l)//2]), solve(l[len(l)//2:]))
    else:
        return 0 if p.count('B')<2 else 1

    if len(u)>3:
        return sum(solve(u[:len(u)//2]), solve(u[len(u)//2:]))
    else:
        return 0 if p.count('B')<2 else 1


def check(s):
    n = len(s)

    if n<3:
        return -1
    if s.count('B') < 2:
        return -1
    if s.count('B') > n // 2:
        return -1

    return sum(solve(s[:n//2], s[n//2:]))


if __name__ == '__main__':

    assert check('.') == -1
    assert check('B') == -1
    assert check('..') == -1
    assert check('.B') == -1
    assert check('B.') == -1
    assert check('BB') == -1
    assert check('...') == -1
    assert check('..B') == -1
    assert check('.B.') == -1
    assert check('.BB') == 1
    assert check('B..') == -1
    assert check('B.B') == 0
    assert check('BB.') == 1
    assert check('BBB') == -1
