from random import randrange

from SystemConsole import SystemConsole
from trivia import Game

if __name__ == '__main__':
    not_a_winner = False

    console = SystemConsole()
    game = Game(console)

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break
