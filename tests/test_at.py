from pyfunctools.at import at

def test_at():

    obj = { 'a': 1, 'b': { 'a': 1, 'b': [ 'a' ] } }

    assert at(obj, 'a') == 1
    assert at(obj, 'b.a') == 1
    assert at(obj, 'b.b') == [ 'a' ]
    assert at(obj, 'b.b.0') == 'a'
    assert at(obj, 'b.b[0]') == 'a'
