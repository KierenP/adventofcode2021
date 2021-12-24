import copy

class bingo_board:
    def __init__(self, board):
        assert len(board) == 5
        assert len(board[0]) == 5

        self.board = copy.deepcopy(board)
        self.marked = [[False for x in range(5)] for y in range(5)]

    def __repr__(self):
        return "Board: " + str(self.board) + " Marked: " + str(self.marked)

    def mark_value(self, value):
        for y, row in enumerate(self.board):
            for x, val in enumerate(row):
                if val == value:
                    self.marked[y][x] = True

    def value(self):
        aggregate = 0

        for y, row in enumerate(self.board):
            for x, val in enumerate(row):
                if not self.marked[y][x]:
                    aggregate = aggregate + self.board[y][x]

        return aggregate

    def has_won(self):
        for y in self.marked:
            if all(y):
                return True
        
        for x in zip(*self.marked):
            if all(x):
                return True
        
        return False

boards = []
bingo_input = []

with open("Input.txt") as file:
    bingo_input = [ int(x) for x in next(file).split(',') ]

    board = []

    for line in file:
        line = line.strip()

        if not line:
            continue

        board.append([ int(x) for x in line.split() ])

        if len(board) == 5:
            boards.append(bingo_board(board))
            board.clear()

for value in bingo_input:
    for board in boards:
        board.mark_value(value)

    if len(boards) == 1 and board.has_won():
        print(boards[0].value() * value)
        break

    boards = [ board for board in boards if not board.has_won() ]    

    