from main import valida_registro, valida_campo

def test_valida_registro():
    path = 'files/test_files/registro.json'
    registro = valida_registro(path)
    assert registro == [100, 60, 0]


def test_valida_campo_cpf():
    chave = 'cpf'
    valor = '09999999999'
    res = valida_campo(chave, valor)

    assert res == 1 

def test_valida_campo_nome():
    chave = 'nome'
    valor = {"PrimeiroNome": "João", "NomeMeio": "", "UltimoNome": "Silva"}
    res = valida_campo(chave, valor)

    assert res == 1
