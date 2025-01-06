"""Exercício 24: Classificador de Número."""

"""
Escreva um programa que solicite ao usuário para digitar um número.
Utilize try-except para assegurar que a entrada seja numérica e utilize
if-elif-else para classificar o número como "positivo", "negativo" ou
"zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
"""

try:
    numero_para_avaliar = int(
        input("Digite um número interiro para ser classificado: ")
    )
    if numero_para_avaliar > 0:
        print(f"O número {numero_para_avaliar} é positivo.")
    elif numero_para_avaliar < 0:
        print(f"O número {numero_para_avaliar} é negativo.")
    else:
        print(f"O número {numero_para_avaliar} é zero.")

    if numero_para_avaliar % 2 == 0:
        print(f"O número {numero_para_avaliar} é par.")
    else:
        print(f"O número {numero_para_avaliar} é ímpar.")

except ValueError:
    print("Número digitado não interio.")
