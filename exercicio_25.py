"""Exercício 25: Verificador de Palíndromo."""

"""
Crie um programa que verifica se uma palavra ou frase é um palíndromo
(lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função
isinstance() para verificar o tipo da entrada.
"""

cadeia_caracteres = input("Digite uma cadeia de caracteres para verificar: ")
if cadeia_caracteres.isdigit():
    print("A cadeia informada é somente formada por digitos.")
elif cadeia_caracteres.isspace():
    print("A cadeia informada é somente formada por espaços.")
elif isinstance(cadeia_caracteres, str):
    if cadeia_caracteres == cadeia_caracteres[::-1]:
        print("A cadeia informada é Palíndromo.")
    elif cadeia_caracteres.lower() == cadeia_caracteres.lower()[::-1]:
        print(
            "A cadeia informada é Palíndromo, porém, com diferenças entre letras maiúsculas e minúsculas."
        )
    else:
        print("A cadeia informada não é Palíndromo.")
        exit()
