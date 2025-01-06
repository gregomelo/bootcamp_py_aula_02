"""Desafio da Aula 02."""

# Coletando o nome do usuario
try:
    nome_do_usuario = input("Digite o nome do usuário: ")

    if len(nome_do_usuario) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif nome_do_usuario.isspace():
        raise ValueError(
            "Nome inválido contendo somente caracteres espaço. Tente novamente."
        )
    elif any(letra.isdigit() for letra in nome_do_usuario):
        raise ValueError("Nome inválido contendo um ou mais números. Tente novamente.")

except ValueError as e:
    print(e)

# Coletando o valor do salário
try:
    valor_salario = float(input("Digite o valor do salário: "))
    if valor_salario >= 0:
        print("Salário negativo ou zero. Tente novamente.")
        exit()

except ValueError:
    print("Salário inválido. Tente novamente.")

# Calculando o bônus do usuário
valor_bonus = 1000 + valor_salario * 1.5

# Retornando o resultado
print(f"Olá {nome_do_usuario}, o seu bônus foi de {valor_bonus}.")
