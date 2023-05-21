import json

def valida_registro(path):
    return [100, 60, 0] 

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
    print(valida_registro('files/test_files/hw.json'))
    
    #parte para auxiliar na implementacao
    #ret = valida_registro('files/test_files/registro.json')

    #for i in ret:
        #for chave in ret[i]:
            #print(chave)
