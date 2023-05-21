from main import valida_registro

def test_valida_registro():
    path = 'files/test_files/registro.json'
    registro = valida_registro(path)
    assert registro == [100, 60, 0]