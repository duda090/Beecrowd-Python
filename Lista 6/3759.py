def calcular_area_triangulo(base, altura):
    return (base * altura) / 2
def calcular_volume_cubo(aresta):
    return aresta ** 3
base = int(input())
altura = int(input())
aresta = int(input())
area = calcular_area_triangulo(base, altura)
volume = calcular_volume_cubo(aresta)
print(area)
print(volume)