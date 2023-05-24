from main import valida_registro, valida_campo
from pytest import raises

PARAMETHER = [[{"title": ""}, 0],
              [{"Nationality": {"nationality": "brasileiro", "birthCity": "", "BirthSate": "Rio de Janeiro"}}, 1], 
              [{"identifier": {"identifier.lattes": "6783234820", "identifier.orcid": "4783927436729W"}}, 0],
              [{"authors": {"nome" : "Luciana Veloso da Costa", "ordemAutoria" : "1", "citationName" : "" }}, 1]]

REG_PARAMETHER = [["files/test_files/registro2.json", [77, 0, 77]],
                  ["files/test_files/registro.json", [84, 83, 85, 81, 82, 87, 83, 76, 76, 77]],
                  ["files/test_files/registroAllNull.json", [0, 0, 0]]]

def valida_campo_parametrizado(parametros):
    dictionary_keys = [list(inner_list[0].keys())[0] for inner_list in PARAMETHER if isinstance(inner_list[0], dict)]
    dictionary_values = [list(inner_list[0].values())[0] for inner_list in PARAMETHER if isinstance(inner_list[0], dict)]

    for k, v, p in zip(dictionary_keys, dictionary_values, parametros):
        print(k, v)
        assert valida_campo(k, v) == p[1]

def valida_registro_paramm(paramm):
    for p in paramm:
        path = p[0]
        registro = valida_registro(path)
        assert registro == p[1]

def test_valida_registro_bad_format():
    path = 'files/test_files/hw.json'
    with raises(ValueError) as exc_info:
        valida_registro(path)
    assert str(exc_info.value) == "Bad format"

def test_valida_registro_null_path():
    path = ''
    with raises(ValueError) as exc_info:
        valida_registro(path)
    assert str(exc_info.value) == "Null path exception"

def test_valida_registro_not_found():
    path = '/foo/barr'
    with raises(ValueError) as exc_info:
        valida_registro(path)
    assert str(exc_info.value) == "File not found"

def test_valida_campo_title():
    chave = 'title'
    valor = 'The first thing beint tested at this time'
    res = valida_campo(chave, valor)

    assert res == 1 

def test_valida_campo_nationality():
    chave = 'Nationality'
    valor = {"nationality": "brasileiro", "birthCity": "", "BirthSate": "Rio de Janeiro"}
    res = valida_campo(chave, valor)

    assert res == 1

def test_valida_campo_nationality_vazio():
    chave = 'Nationality'
    valor = {"nationality": "", "birthCity": "", "BirthSate": ""}
    res = valida_campo(chave, valor)

    assert res == 0

def test_valida_campo_parametrizado():
    valida_campo_parametrizado(PARAMETHER)

def test_valida_campo_authors():
    chave = 'authors'
    valor = {"name": "Luciana Veloso da Costa", "ordemAutoria": "1", "citationName": ""}
    res = valida_campo(chave, valor)

    assert res == 1

def test_valida_campo_authors_vazio():
    chave = 'authors'
    valor = {"name": "", "ordemAutoria": "", "citationNAme": ""}
    res = valida_campo(chave, valor)

    assert res == 0

def test_valida_registro_parametrizado():
    valida_registro_paramm(REG_PARAMETHER)
