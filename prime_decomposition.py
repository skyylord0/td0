

def decomposition(value):
    factors = []
    n = value
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append((i, 0))
        while n % i == 0:
            factors[-1] = (i, factors[-1][1]+1)
            n = n//i
        i += 1
    return factors


# Tests
assert decomposition(7*11) == [(7, 1), (11, 1)]
assert decomposition(11*11) == [(11, 2)]
assert decomposition(11*11*13) == [(11, 2), (13, 1)]

# Main
if __name__ == '__main__':
    print(decomposition(600851475143))

    while True:
        val = int(input("Enter an integer:\n"))
        print("Decomposition of %d is %r" % (val, decomposition(val)))
