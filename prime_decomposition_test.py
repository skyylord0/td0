import prime_decomposition as dec;

def test_decomposition():
    assert dec.decomposition(7*11) == [(7, 1), (11, 1)]
    assert dec.decomposition(11*11) == [(11, 2)]
    assert dec.decomposition(11*11*13) == [(11, 2), (13, 1)]


