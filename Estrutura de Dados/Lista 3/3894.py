def contar_palavras():
    from collections import defaultdict
    contagem = defaultdict(int)
    while True:
        linha = input().strip()
        if linha == "FIM":
            break
        palavras = linha.lower().split()
        for palavra in palavras:
            contagem[palavra] += 1
    for palavra in sorted(contagem.keys()):
        print(f"{palavra} {contagem[palavra]}")
contar_palavras()
