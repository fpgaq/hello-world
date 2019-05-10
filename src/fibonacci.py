FibMem = {}

def fib_mem(n):
    if n < 2:
        return n

    if FibMem.get(n) is None:
        FibMem[n] = fib_mem(n-1) + fib_mem(n-2)

    return FibMem[n]

FibTab = {0: 0, 1: 1}

def fib_tab(n):

    if FibTab.get(n) is None:
        for n in range(2, n+1):
            # print(n)
            FibTab[n] = FibTab[n-1] + FibTab[n-2]

    return FibTab[n]

if __name__ == '__main__':
    print(fib_mem(4))
    print(fib_mem(6))
    print(fib_mem(16))

    print(fib_tab(16))
    print(fib_tab(6))
    print(fib_tab(4))



