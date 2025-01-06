"""Exercício 23: Calculadora Simples."""

"""
Desenvolva uma calculadora simples que aceite duas entradas numéricas e
um operador (+, -, *, /) do usuário. Use try-except para lidar com
divisões por zero e entradas não numéricas. Utilize if-elif-else para
realizar a operação matemática baseada no operador fornecido. Imprima o
resultado ou uma mensagem de erro apropriada.
"""

try:
    primeiro_numero = float(input("Digite o primeiro número: "))

    operacao_necessaria = input("Digite a operação a ser realizada: ")

    if operacao_necessaria not in ["+", "-", "/", "*"]:
        print("Digite uma das operações padrões com um caracter especial.")

    segundo_numero = float(input("Digite o segundo número:"))

    if operacao_necessaria == "+":
        resultado = primeiro_numero + segundo_numero
    elif operacao_necessaria == "-":
        resultado = primeiro_numero - segundo_numero
    elif operacao_necessaria == "*":
        resultado = primeiro_numero * segundo_numero
    else:
        resultado = primeiro_numero / segundo_numero

    print(f"O resultado da operação é: {resultado:.2f}")

except ValueError:
    print("Entrada numérica inválida.")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero.")
