from btree import Tree
from board import Board
import sys


class ChoosingSideError(Exception):
    pass


class Interface:
    """
    Interface of the tic-tac-toe game

    Attributes:
    + play_tree: btree.Tree
    + board: board.Board
    + side: str

    Methods:
    + __init__(): NoneType
    + choose_side(): NoneType
    + computer_turn(): NoneType
    + make_turn(): NoneType
    + check_victory(): NoneType
    + main(): NoneType
    """
    def __init__(self):
        self.play_tree = None
        self.board = Board()
        self.side = None

    def choose_side(self):
        """() -> NoneType
        Allows a player to choose 'x' or 'o'
        """
        while True:
            try:
                self.side = input('Enter your side ("x" or "o"): ')
                if self.side != 'x' and self.side != 'o':
                    raise ChoosingSideError
                break
            except ChoosingSideError:
                print('Wrong string to choose side')

    def computer_turn(self):
        """() -> NoneType
        Generates computer's turn
        """
        self.play_tree = Tree(self.board)
        self.board = self.play_tree.choose('x' if self.side == 'o' else 'o')

    def make_turn(self):
        """() -> NoneType
        Allows player to draw his symbol
        """
        while True:
            try:
                row = int(input('Enter row: '))
                col = int(input('Enter column: '))
                self.board.change(row, col, self.side)
                break
            except (ValueError, TypeError, KeyError) as e:
                if str(e) == "'this position is already taken'":
                    print('This position is already taken')
                else:
                    print('You should enter two (one per line) integers ' +
                          'between 1 and 3 inclusively')

        winner = self.board.victory()
        if winner == 'n':
            self.computer_turn()

    def check_victory(self):
        """() -> NoneType
        If here is victory on the board, prints message and stops the
        game
        """
        winner = self.board.victory()
        if winner != 'n':
            if winner == 't':
                print("It's a tie!")
            else:
                print(self.board)
                print('"{0}" won!'.format(winner))
            sys.exit(0)

    def main(self):
        self.choose_side()
        if self.side == 'o':
            self.computer_turn()
        while True:
            print(self.board)
            self.check_victory()
            self.make_turn()


def main():
    game = Interface()
    game.main()


if __name__ == '__main__':
    main()
