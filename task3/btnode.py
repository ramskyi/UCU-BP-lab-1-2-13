from board import Board


class TreeNode:
    def __init__(self, board=Board()):
        self.left = None
        self.right = None
        self.board = board
        self.subsum = 0
        if board.victory() == 'x':
            self.subsum += 1
        if board.victory() == 'o':
            self.subsum -= 1
