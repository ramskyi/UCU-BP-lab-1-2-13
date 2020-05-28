class Board:
    """
    Contains info about current state of the playing board

    Attributes:
    + state: list(str)

    Methods:
    + change(int, int, bool): NoneType
    """

    def __init__(self, lst=None):
        """(list(str)) -> NoneType
        Takes list which describes current state on the board
        """
        if lst is None:
            lst = [[' ']*3, [' ']*3, [' ']*3]
        self._state = lst

    def __str__(self):
        lst = ['|'.join(item) for item in self._state]
        return '\n'.join(lst)

    def change(self, row, col, symbol):
        """(int, int, bool) -> NoneType
        Adds the symbol to the board
        """
        if not isinstance(row, int):
            raise TypeError('row must be integer')
        if not 1 <= row <= 3:
            raise KeyError('row must be int between 1 and 3 inclusively')

        if not isinstance(col, int):
            raise TypeError('col must be integer')
        if not 1 <= col <= 3:
            raise KeyError('col must be int between 1 and 3 inclusively')

        if not isinstance(symbol, str):
            raise TypeError('symbol must be str')
        if symbol != 'o' and symbol != 'x':
            raise ValueError('symbol must be "o" or "x"')
        if self._state[row - 1][col - 1] != ' ':
            raise KeyError('this position is already taken')
        self._state[row - 1][col - 1] = symbol

    def victory(self):
        """() -> str
        Returns 'o' if 'o' won, 'x' if 'x' won, 't' if tie and 'n' if
        game continues and None if state is impossible
        """
        def victory_of_symbol(symbol):
            """(str) -> bool
            Checks if given symbol won
            """
            lst = self._state
            return (symbol == lst[0][0] == lst[0][1] == lst[0][2] or
                    symbol == lst[1][0] == lst[1][1] == lst[1][2] or
                    symbol == lst[2][0] == lst[2][1] == lst[2][2] or

                    symbol == lst[0][0] == lst[1][0] == lst[2][0] or
                    symbol == lst[0][1] == lst[1][1] == lst[2][1] or
                    symbol == lst[0][2] == lst[1][2] == lst[2][2] or

                    symbol == lst[0][0] == lst[1][1] == lst[2][2] or
                    symbol == lst[2][0] == lst[1][1] == lst[0][2])

        x_won = victory_of_symbol('x')
        o_won = victory_of_symbol('o')
        if x_won and o_won:
            return None
        if x_won:
            return 'x'
        if o_won:
            return 'o'

        # Checks if in string representation is at least one space to check
        # if game is finished or there are place for another symbol
        return 'n' if ' ' in str(self) else 't'
        
    def last_symbol(self):
        """() -> str
        Returns last set symbol, considering that first is 'x' which
        also means that is board is empty method would return 'o'
        """
        cnt_x = self._state[0].count('x') + self._state[1].count('x') + \
            self._state[2].count('x')
        cnt_o = self._state[0].count('o') + self._state[0].count('o') + \
            self._state[0].count('o')
        return 'x' if cnt_x > cnt_o else 'o'

    def free_positions(self):
        """() -> list(tuple(int, int))
        Returns list of positions of free cells
        """
        result = []
        for i in range(3):
            for j in range(3):
                if self._state[i][j] == ' ':
                    result.append((i + 1, j + 1))
        return result
