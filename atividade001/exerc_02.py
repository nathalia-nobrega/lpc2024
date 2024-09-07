# Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa.
# Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

def valida_palindromo(frase):
    frase_sem_espaco = frase.replace(" ", "")
    is_palindromo = False

    for index in range(len(frase_sem_espaco)):
        letra = frase_sem_espaco[index]
        letra_oposta = frase_sem_espaco[(len(frase_sem_espaco) - 1) - index]

        if letra is not letra_oposta:
            return is_palindromo
    is_palindromo = True
    return is_palindromo


def main():
    frase = input("Entre com uma frase: ")
    result = valida_palindromo(frase)
    print("É palíndromo? {}".format(result))

if __name__ == "__main__":
    main()
