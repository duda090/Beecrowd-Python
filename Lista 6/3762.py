def busca_binaria(inicio, fim, alvo):
    passo = 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(f"Passo {passo}: Intervalo [{inicio}, {fim}], Meio={meio}")
        if meio == alvo:
            return True
        elif meio < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
        passo += 1
    return False
inicio = int(input())
fim = int(input())
alvo = int(input())
if alvo < inicio or alvo > fim:
    print(f"Número {alvo} não encontrado")
else:
    encontrado = busca_binaria(inicio, fim, alvo)
    
    if encontrado:
        print(f"Número {alvo} encontrado")
    else:
        print(f"Número {alvo} não encontrado")