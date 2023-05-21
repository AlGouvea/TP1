import json

def valida_registro(path):
    if(path == ''):
        raise ValueError("Null path exception")
    
    try:
        with open(path, encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError as e:
        raise ValueError("File not found") from e
    
    reg_list = []
    for _, inner_dict in data.items():
        if not isinstance(inner_dict, dict):
            print("Bad format!")
            raise ValueError("Bad format")
        else:
            reg_list.append(inner_dict)

    res = []
    for r in reg_list:
        val = 0
        for i in r.items():
            val += valida_campo(i[0], i[1])

        res.append(100*(val/5))

    return res 

def valida_campo(chave, valor):
    if chave == 'Nome':
        for n in valor:
            res = valida_campo(n, valor[n])
            if res == 1:
                return 1    
        return 0
    
    elif valor == '':
        return 0

    return 1


if __name__ == '__main__':
    print(valida_registro('files/test_files/registro.json'))
    
    #parte para auxiliar na implementacao
    #ret = valida_registro('files/test_files/registro.json')

    #for i in ret:
        #for chave in ret[i]:
            #print(chave)
