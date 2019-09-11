from hello_world import hello


def test_hello_world():
    assert isinstance(hello(), str)


def test_answer():
    assert hello() == "hello world"
