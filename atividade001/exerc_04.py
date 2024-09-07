# Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

digits = {
    '1': ['UM'],
    '2': ['DOIS', 'VINTE'],
    '3': ['TRÊS', 'TRINTA'],
    '4': ['QUATRO', 'QUARENTA'],
    '5': ['CINCO', 'CINQUENTA'],
    '6': ['SEIS', 'SESSENTA'],
    '7': ['SETE', 'SETENTA'],
    '8': ['OITO', 'OINTENTA'],
    '9': ['NOVE', 'NOVENTA']
}

casa_dez = {
    '10': 'DEZ',
    '11': 'ONZE',
    '12': 'DOZE',
    '13': 'TREZE',
    '14': 'CATORZE',
    '15': 'QUINZE',
    '16': 'DEZESSEIS',
    '17': 'DEZESSETE',
    '18': 'DEZOITO',
    '19': 'DEZENOVE',
}

number = input('Entre com um número (máx. 99): ')
while int(number) > 99:
    number = input('O número é inválido! Tente novamente (máx. 99): ')

qtd_digits = len(number)

if qtd_digits == 1:
    print('{} por extenso: {}'.format(number, digits[number][0]))
else:
    first_number = number[0]
    second_number = number[1]

    # Se tem 2 dígitos e o 1° dígito é 1 -> está em casa_dez
    if first_number == '1':
        print('{} por extenso: {}'.format(number, casa_dez[number]))
    elif second_number == '0':
        print('{} por extenso: {}'.format(number, digits[first_number][1]))
    else:
        frase_parte_um = digits[first_number][1]
        frase_parte_dois = digits[second_number][0]
        concat = frase_parte_um + " E " + frase_parte_dois
        print(concat)