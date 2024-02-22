def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, 0, -1):
        if q[i] != i+1:
            match q[i-1], q[i-2]:
                case i+1, _:
                    bribes += 1
                    q[i-1], q[i] = q[i], q[i-1]
                case i+1, i+1:
                    bribes += 2
                    q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]
                case _, _:
                    print('Too chaotic')
                    return
    print(bribes)


