# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.


preço_origin = float(input("Olá, digite o preço original do produto, por favor R$: "))
desc = float(input("Insira o valor do desconto desejado: "))


preço_des = preço_origin - (preço_origin * (desc / 100))


print(f"O valor com o desconto aplicado ficou R$:{preço_des:2f}")