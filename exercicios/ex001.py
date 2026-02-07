"""
Desenvolva um algoritmo que solicite ao usuário o preço de um produto
e um percentual de desconto a ser aplicado a ele.
Calcule e exiba o valor do desconto e o preço final do produto
"""
preco = float(input('Digite o valor do produto: R$'))
percentual = float(input('Digite o percentual de desconto (0-100%): '))

desconto = preco * (percentual / 100)
final = preco - desconto

print(f'O preço do produto é R${preco:.2f}. Desconto de {percentual:.2f}%')
print(f'Valor calculado de desconto: {desconto:.2f}. Valor final do produto: R${final:.2f}')
