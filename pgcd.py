
def pgcd_iter(a, b):
    while a!=b :
        if a>b :
            a = a-b
        else:
            b = b-a
    return a


def pgcd_rec(a, b):
    if b == 0:
        return a
    else:
        return pgcd_rec(b, a % b)


# Run Tests using assert to check validity of implementations


assert pgcd_iter(2*3*3*7, 3*5*7*11) == 3*7
assert pgcd_rec(2*3*3*7, 3*5*7*11) == 3*7

assert pgcd_iter(3*5*7*11, 2*3*3*7) == 3*7
assert pgcd_rec(3*5*7*11, 2*3*3*7) == 3*7

assert pgcd_iter(5*11, 3*7) == 1
assert pgcd_rec(5*11, 3*7) == 1

assert pgcd_iter(3*3*11*13, 2*3*3*5*7) == 3*3
assert pgcd_rec(3*3*11*13, 2*3*3*5*7) == 3*3


if __name__ == '__main__':
    # Minimalistic interactive program to compute PGCD
    print("Launching PGCD calculator...")
    while True:
        val0 = int(input("Enter an integer:\n"))
        val1 = int(input("Enter an integer:\n"))
        print("PGCD of %d and %d is %d" % (val0, val1, pgcd_iter(val0,val1)))
