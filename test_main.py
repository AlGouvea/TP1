from main import valida_registro, valida_campo

PARAMETHER = [[{"cpf": ""}, 0],
              [{"Nome": {"PrimeiroNome": "João", "NomeMeio": "", "UltimoNome": "Silva"}}, 1], 
              [{"Nome": {"PrimeiroNome": "", "NomeMeio": "", "UltimoNome": ""}}, 0]]

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
    chave = 'Nome'
    valor = {"PrimeiroNome": "João", "NomeMeio": "", "UltimoNome": "Silva"}
    res = valida_campo(chave, valor)

    assert res == 1

def test_valida_campo_nome_vazio():
    chave = 'Nome'
    valor = {"PrimeiroNome": "", "NomeMeio": "", "UltimoNome": ""}
    res = valida_campo(chave, valor)

    assert res == 0

def valida_campo_parametrizado(parametros):
    dictionary_keys = [list(inner_list[0].keys())[0] for inner_list in PARAMETHER if isinstance(inner_list[0], dict)]
    dictionary_values = [list(inner_list[0].values())[0] for inner_list in PARAMETHER if isinstance(inner_list[0], dict)]

    for k, v, p in zip(dictionary_keys, dictionary_values, parametros):
        assert valida_campo(k, v) == p[1]

def test_parametrizado():
    valida_campo_parametrizado(PARAMETHER)
