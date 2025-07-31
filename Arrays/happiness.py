if __name__ == "__main__":
    n, m = map(int, input().strip().split(" "))
    a = set(map(int,input().strip().split(" ")))
    A = set(map(int,input().strip().split(" ")))
    B = set(map(int,input().strip().split(" ")))
    happiness = 0

    for i in a:
        if i in A:
            happiness += 1
        if i in B:
            happiness -= 1

    print(happiness)
