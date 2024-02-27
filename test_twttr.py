from twttr import shorten

def test_shorten():
    assert shorten("") == ""
    assert shorten(" ") == " "
    assert shorten("1@*'>?er") == "1@*'>?r"
    assert shorten("wert") == "wrt"
    assert shorten("airuorA") == "rr"
    assert shorten("a s d f g h ") == " s d f g h "
    assert shorten("wer!ut") == "wr!t"
    assert shorten("airu orA") == "r r"
    assert shorten("asid fgh") == "sd fgh"
    assert shorten("werta") == "wrt"

test_shorten()