# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

preco_total = 0

while True:
    nome_fruta = input("Digite o nome da fruta (ou digite 'terminei' para encerrar): ")
    
    
    if nome_fruta.lower() == 'terminei':

     break


    preco_novo = int(input(f"Digite o valor em reais da fruta {nome_fruta}: "))

    preco_total += preco_novo

print(f"O preço total das frutas é de: R${preco_total:.2f}")