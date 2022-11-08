# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

numero1 = int(input("Entre com o primeiro numero:"))
numero2 = int(input("Entre com o segundo numero:"))
numero3 = float(input("Entre com o terceiro numero:"))

produto_dobro = ((numero1 * 2) * (numero2 % 2))
soma_triplo = ((numero1 * 3) + numero3)
elevado_cubo = (numero3 ** 3)

print("O produto do dobro:", produto_dobro)
print("A soma do triplo:", soma_triplo)
print("O terceiro elevado ao cubo:", round(elevado_cubo))
