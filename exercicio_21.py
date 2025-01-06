"""Exercício 21: Conversor de Temperatura."""

"""
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa
deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir
que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em
Fahrenheit ou uma mensagem de erro se a entrada não for válida
"""

try:
    temperatura_celsius = float(
        input("Digite somente a parte numérica da temperatura em graus Celsius: ")
    )
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
    print(
        f"A temperatura de {temperatura_celsius:.2f}°C "
        f"é igual a {temperatura_fahrenheit:.2f}°F."
    )
except ValueError:
    print("O valor de tempertura digitado não é um número.")
except TypeError as e:
    print(f"Foi encontrado o seguinte erro: {e}")
