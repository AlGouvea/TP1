from main import read_json

def test_hw():
    teste = read_json()
    assert teste == {'hello': 'world!'}
