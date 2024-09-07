import sys
from random import randint

# Caminho contendo todas as palavras da língua portuguesa
# URL = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"

"""Busca todas as palavras provenientes de um caminho específico e armazena o resultado em um vetor"""


def retrieve_words_from_file():
    all_words = []

    print("Buscando palavras do arquivo... ")
    with open("palavras.txt", "r") as file:
        words = file.readlines()
        for word in words:
            all_words.append(word.split('\n')[0])
    print("Busca finalizada!")

    return all_words


""" Seleciona uma palavra aleatória a partir de uma lista """


def get_random_word(words):
    index_random = randint(0, len(words) - 1)
    random_word = words[index_random]

    return random_word


"""Começa o jogo"""


def play_game(random_word, length_word):
    print("\nJOGO DA FORCA ---- PALAVRA DE {} LETRAS".format(length_word))

    # Criando os espaços em branco
    blank_spaces = "_" * length_word
    list_spaces = list(blank_spaces)

    num_tries = 0
    letters_tried = []

    while num_tries < 6 and not (list_spaces.count("_") == 0):
        print("\n")
        print("\t".join(list_spaces))
        letter = str.lower(input("Digite uma letra: "))

        # Verificando se o usuário já não tentou aquela letra antes
        while letter in letters_tried:
            letter = str.lower(input("Você já entrou com essa letra antes! Entre com outra: "))
        letters_tried.append(letter)

        # Verifica se a letra se encontra ou não na palavra secreta
        if letter not in random_word:
            num_tries += 1
            print("\nVocê errou! Tentativas restantes: {} ".format(6 - num_tries))
            if num_tries == 6:
                print("A palavra secreta era {}".format(random_word))
        else:
            # Encontrar em quais posições está aquela letra e substituir nos espaços em branco
            for index in range(length_word):
                if letter == random_word[index]:
                    list_spaces[index] = letter
            if list_spaces.count("_") == 0:
                print("\nVocê venceu! A palavra era {}".format(random_word))
                break


def main():
    all_words = retrieve_words_from_file()
    random_word = get_random_word(all_words)
    play_game(random_word, len(random_word))


if __name__ == "__main__":
    main()
