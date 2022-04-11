def fib(nfib):
    "Return `nfib` terms of the Fibonnaci sequence"
    fib_list = [0,1]
    for _ in range(2, nfib):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list