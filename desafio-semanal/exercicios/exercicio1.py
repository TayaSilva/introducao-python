# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.


lista = [2, 2, 7, 4, 5, 7, 9, 6, 1, 9, 7]


conjunto_certo = set(lista)

# Converter o conjunto de volta para uma lista
lista_certa = list(conjunto_certo)

# Imprimir a lista resultante sem duplicatas
print(lista_certa)