# Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
# e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

# Regras de validação:
# 1. Não deve conter letras
# 2. Deve conter 11 dígitos e 3 símbolos (2 pontos e 1 hífen) = len = 14
#   2.1. [0 -> x] [1 -> x] [2 -> x] [3 -> .] [4 -> x] [5 -> x] [6 -> x] [7 -> .] [8 -> x] [9 -> x] [10 -> x] [11 -> -] [12 -> x] [13 -> x]

def validate_cpf(cpf):
    is_valid = False

    # Verificar tamanho
    if len(cpf) > 14 or len(cpf) < 14:
        print("CPF INVÁLIDO: deve possuir 14 caracteres no total.")
        return is_valid

    # Verificar se contém os símbolos nas posições corretas
    if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
        print("CPF INVÁLIDO: os símbolos não se encontram nas posições devidas.")
        return is_valid

    # Verificar se todos os caracteres são numéricos, excluindo os símbolos
    copy_cpf = cpf.replace(".", "").replace("-", "")

    for index in range(len(copy_cpf)):
        if not(copy_cpf[index].isnumeric()):
            print("CPF INVÁLIDO: os dígitos devem ser numéricos!")
            return is_valid

    # Após todas as verificações, se chegar até aqui, quer dizer que é válido
    is_valid = True
    return is_valid

def main():
    cpf = input("Digite um CPF (formato xxx.xxx.xxx-xx): ")
    result = validate_cpf(cpf)
    print("É um CPF válido? {}".format(result))

if __name__ == "__main__":
    main()



