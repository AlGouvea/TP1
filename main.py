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
    for registro in reg_list:
        val = 0
        for item in registro.items():
            #Fora de info dos autores
            if item[0] == 'title' or item[0] == 'publicationDate' or item[0] == 'language':
                val += valida_campo(item[0], item[1])

            #Info dos autores
            completude_autores = 0
            total_autores = 0
            if item[0] == 'authors':
                for author in item[1]:
                    total_autores += 1
                    val_author = 0
                    identifier = {}
                    nationality = {}
                    for it in author.items():
                        if it[0] == 'identifier.lattes' or it[0] == 'identifier.orcid':
                            identifier.update({it[0]: it[1]})
                        if it[0] == 'nationality' or it[0] == 'birthState' or it[0] == 'birthCity' or it[0] == 'birthCountry':
                            nationality.update({it[0]: it[1]})

                    val_author += valida_campo('identifier', identifier)
                    val_author += valida_campo('Nationality', nationality)
                    completude_autores += val_author

                val += (completude_autores/total_autores)

        res.append(100*(val/5))

    return res

def valida_campo(chave, valor):
    #Regra OR Inclusivo
    res = 0
    if chave == 'Nationality' and valor:
            for n in valor:
                res = valida_campo(n, valor[n])
                if res == 1:
                    return 1    
            return 0
    # Regra OR Exclusivo
    elif chave == 'identifier' and valor:
        for n in valor:
            res += valida_campo(n, valor[n]) 
        if res == 1:
            return 1
        else:
            return 0
    # Se valor atomico ou dicionario forem vazios
    elif valor == '' or not valor:
        return 0
    
    return 1


if __name__ == '__main__':
    print(valida_registro('files/test_files/registro.json'))
    
    #parte para auxiliar na implementacao
    #ret = valida_registro('files/test_files/registro.json')

    #for i in ret:
        #for chave in ret[i]:
            #print(chave)
