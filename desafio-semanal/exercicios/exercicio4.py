# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.


def cont_frutas(lista_frutas):
    
    contagem_frutas = {}

   
    for fruta in lista_frutas:
        contagem_frutas[fruta] = contagem_frutas.get(fruta, 0) + 1

    return contagem_frutas


frutas = ['morango', 'banana', 'uva', 'laranja', 'morango',  'uva', 'uva']

# Chama a função contar_frutas e imprime o dicionário resultante
resultado = cont_frutas(frutas)
print(resultado)