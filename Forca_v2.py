# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
# -> gerar a palavra de forma aleatória da no banco de palavras
import random

# Board (tabuleiro)
# -> Lista de tabuleiros
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    # -> Obtem palavra e cria duas listas vazias (letras erradas e certas)
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    # Método para adivinhar a letra
    # -> Recebe o parametro de letra;
    # -> Caso a letra esteja na palavra e ainda nao na lista de letras certas, adiciona na lista de letras certas.
    # -> Caso a letra não esteja na palavra e ainda nao na lista de letras erradas, adiciona na lista de letras erradas.
    # -> Se não for nenhum dos casos, retorna falto (assim, letras repetidas não funcionam).
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    # -> OU retorna método hangman_won OU verifica se o comprimento da lista de letras errada = 6
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    # Método para verificar se o jogador venceu
    # -> "_" é o caracter usado para ocultar as letras das palavras
    # -> Se "_" não estiver na "hide word", retorna que venceu o jogo.
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    # -> Para cada letra dentro da palavra:
    # -> Se a letra não estiver na lista de letras certas, preenche com "_"
    # -> Se a letra estiver na lista de letras corretas, preenche com a própria letra
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    # -> Método que interage com o ussuário
    # -> Imprime o board no índice específico do comprimento da lista de letras erradas;
    # -> Imprime "palavra" + a palvra escondida
    # -> Imprime a lista de letras erradas
    # -> Imprime a lista de letras corretas
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ', )
        for letter in self.missed_letters:
            print(letter, )
        print()
        print('Letras corretas: ', )
        for letter in self.guessed_letters:
            print(letter, )
        print()


# Método para ler uma palavra de forma aleatória do banco de palavras
# -> Lê arquivo txt, lê uma linha, e busca de maneira randomica uma linha do texto.
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Método Main - Execução do Programa
# -> Definindo método Main e fazendo chamada de todas as funções de classe construídas;

def main():
    # Objeto
    # -> Criando uma instancia da classe Hangman, passando uma função de forma a escolher a palavra aleatoriamente
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()