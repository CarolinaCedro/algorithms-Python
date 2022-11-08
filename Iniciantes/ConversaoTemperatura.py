# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("Entre com a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print("Sua Temperatura de Fahrenheit para Celsius é:", round(celsius, 2))
