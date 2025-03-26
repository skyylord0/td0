import pgcd;

def test_pgcd():
    assert pgcd.pgcd_iter(2*3*3*7, 3*5*7*11) == 3*7
    assert pgcd.pgcd_rec(2*3*3*7, 3*5*7*11) == 3*7

    assert pgcd.pgcd_iter(3*5*7*11, 2*3*3*7) == 3*7
    assert pgcd.pgcd_rec(3*5*7*11, 2*3*3*7) == 3*7

    assert pgcd.pgcd_iter(5*11, 3*7) == 1
    assert pgcd.pgcd_rec(5*11, 3*7) == 1

    assert pgcd.pgcd_iter(3*3*11*13, 2*3*3*5*7) == 3*3
    assert pgcd.pgcd_rec(3*3*11*13, 2*3*3*5*7) == 3*3
