import random
import copy
from btnode import TreeNode as Node


class Tree:
    """
    Tree of possible tic-tac-toe scenaries
    """
    def __init__(self, root_board):
        """(board.Board) -> NoneType
        """
        self.root = Node(root_board)
        self.build_tree(self.root)

    @staticmethod
    def build_tree(vertex):
        """(board.Board) -> NoneType
        """
        board = vertex.board
        winner = board.victory()
        if winner is None or winner == 't':
            return
        elif winner == 'x':
            vertex.subsum += 1
        elif winner == 'o':
            vertex.subsum -= 1

        last_symbol = board.last_symbol()
        new_symbol = 'x' if last_symbol == 'o' else 'o'
        free_positions = board.free_positions()

        position = random.choice(free_positions)
        free_positions.remove(position)
        board1 = copy.deepcopy(board)
        board1.change(position[0], position[1], new_symbol)
        vertex.left = Node(board1)

        if not free_positions:  # if empty
            return

        position = random.choice(free_positions)
        board2 = copy.deepcopy(board)
        board2.change(position[0], position[1], new_symbol)
        vertex.right = Node(board2)

    def choose(self, symbol):
        if self.root.right is None:
            return self.root.left.board

        if symbol == 'x':
            if self.root.left.subsum > self.root.right.subsum:
                return self.root.left.board
            else:
                return self.root.right.board
        else:
            if self.root.left.subsum < self.root.right.subsum:
                return self.root.left.board
            else:
                return self.root.right.board
