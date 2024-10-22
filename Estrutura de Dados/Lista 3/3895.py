def processar_conjuntos():
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    C = set(map(int, input().split()))
    uniao_ab = A | B
    intersecao_bc = B & C
    diff_simetrica_ca = C ^ A
    diff_ab = A - B
    print(" ".join(map(str, uniao_ab)))
    print(" ".join(map(str, intersecao_bc)))
    print(" ".join(map(str, diff_simetrica_ca)))
    print(" ".join(map(str, diff_ab)))
processar_conjuntos()
