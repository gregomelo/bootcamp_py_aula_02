"""Exercício 25: Conversão de Tipo com Validação."""

"""
Crie um script que solicite ao usuário uma lista de números separados
por vírgula. O programa deve converter a string de entrada em uma lista
de números inteiros. Utilize try-except para tratar a conversão de cada
número e validar que cada elemento da lista convertida é um inteiro. Se
a conversão falhar ou um elemento não for um inteiro, imprima uma
mensagem de erro. Se a conversão for bem-sucedida para todos os
elementos, imprima a lista de inteiros.
"""
try:
    lista_numeros_entrada = input(
        "Digite uma lista de números inteiros separados por vírgula: "
    )
    if lista_numeros_entrada.isspace():
        print("Cadeia digitada formada somente por espaço(s).")
        exit()

    if "," not in lista_numeros_entrada:
        print("Somente uma posição foi digitada.")
        exit()

    lista_numeros_string = lista_numeros_entrada.split(sep=",")

    lista_numeros_inteiro = [int(numero) for numero in lista_numeros_string]

    print(f"A lista de números após conversão é {lista_numeros_inteiro}.")
except ValueError:
    print("Uma ou mais posições não puderam ser convertidas.")
