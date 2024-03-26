from algorithm_KMP import find


def test_KMP():
    text = "ALA MAMAŁEGO KOTA. MAŁEGO"
    string = "MAŁEGO"
    assert find(string, text) == [6, 19]

    text = "ALA MA MAŁEGO KOTA. MAŁEGO"
    string = "MAŁEGO"
    assert find(string, text) == [7, 20]

    text = "ALA MAMAMAGO KOTA. MAMAGO"
    string = "MAMAGO"
    assert find(string, text) == [6, 19]

    text = "BBABBBBBBBBB"
    string = "A"
    assert find(string, text) == [2]


def test_KMP_blank():
    text = "something"
    string = ""
    assert find(string, text) == []

    text = ""
    string = "something"
    assert find(string, text) == []

    text = ""
    string = ""
    assert find(string, text) == []


def test_KMP_equal():
    text = "equal"
    string = "equal"
    assert find(string, text) == [0]


def test_KMP_longer():
    text = "short text"
    string = "very long string"
    assert find(string, text) == []


def test_KMP_no_exist():
    text = "short text"
    string = "long"
    assert find(string, text) == []