# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Entre com sua altura: "))
print("Qual seu gênero")
print("(1)Homem")
print("(2)Mulher")
op = int(input())
if op == 1:
    peso_ideal = ((72.7 * altura) - 58)
    print("Seu peso ideal é: ", peso_ideal)
elif op == 2:
    peso_ideal = round(((62.1 * altura) - 44.7), 2)
    print("Seu peso ideal é: ", peso_ideal)
else:
    print("Entrada de dados invalida !!")
