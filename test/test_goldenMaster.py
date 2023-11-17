import random
import unittest
from random import randrange
from unittest import skip

from ConsoleSpy import ConsoleSpy
from trivia import Game

OUTPUT_DIRECTORY = r"C:\Users\kryza\Documents\Sources\Formations\Captronic - TDD Toulouse 2023\triviaPy\goldenMaster"


class MyTestCase(unittest.TestCase):
    __seeds = [0, 1, 3636]

    @staticmethod
    def generate_player_sets():
        player_sets = [[0]] * 7
        for number_of_players in range(7):
            player_sets[number_of_players] = [0] * number_of_players
            for player in range(number_of_players):
                player_sets[number_of_players][player] = f"Player {player + 1}"
        return player_sets + [['Chet', 'Pat', 'Sue']]

    def cases(self):
        for seed in self.__seeds:
            for player_set in self.generate_player_sets():
                yield seed, player_set

    @skip
    def test_record(self):
        for (seed, players) in self.cases():
            with self.subTest(str(seed) + '_' + '_'.join(players)):
                output = self.play_and_return_output(seed, players)
                path = self.make_file_name(seed, players)

                descriptor = open(path, "w")
                descriptor.write(output)
                descriptor.close()

    def test_replay(self):
        for (seed, players) in self.cases():
            with self.subTest(str(seed) + '_' + '_'.join(players)):
                output = self.play_and_return_output(seed, players)
                path = self.make_file_name(seed, players)

                descriptor = open(path, "r")
                expected = descriptor.read()
                descriptor.close()

                self.assertEqual(expected, output)

    @staticmethod
    def make_file_name(random_seed: int, players: [str]):
        file_name = f"{random_seed}_{'_'.join(players)}.txt"
        return OUTPUT_DIRECTORY + '/' + file_name

    @staticmethod
    def play_and_return_output(random_seed: int, players: [str]):
        console = ConsoleSpy()

        try:
            game = Game(console)

            for player in players:
                game.add(player)

            random.seed(random_seed)

            while True:
                game.roll(randrange(5) + 1)

                if randrange(9) == 7:
                    not_a_winner = game.wrong_answer()
                else:
                    not_a_winner = game.was_correctly_answered()

                if not not_a_winner:
                    break
        except Exception as e:
            console.print(str(e))

        return console.get_output()


if __name__ == '__main__':
    unittest.main()
