class bingoboard:
    def __init__(self, board, size):
        self.size = size
        self.board = []
        for i in range(size):
            self.board.append(list(map(int,board[i*5:(i+1)*5])))
        self.marked = [[False for i in range(size)] for j in range(size)]

    def check(self):
        return self.check_rows_for_win() or self.check_columns_for_win()
    
    def find(self, target):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == target:
                    return i, j
        return -1, -1

    def mark(self, target):
        x, y = self.find(target)
        if x == -1 or y == -1:
            return False
        else:
            self.marked[x][y] = True
            return True
        

    def is_marked(self, x, y):
        return self.marked[x][y]
    
    def check_rows_for_win(self):
        for row in range(self.size):
            if sum(self.marked[row]) == self.size:
                return True

    def check_columns_for_win(self):
        for column in range(self.size):
            if sum([self.marked[i][column] for i in range(self.size)]) == self.size:
                return True
    
    def print_board(self):
        for line in self.board:
            for item in line:
                print(item, end=' ')
            print()

    def print_marked(self):
        for i in range(self.size):
            for j in range(self.size):
                print(1 if self.marked[i][j] else 0, end=' ')
            print()

    def print_marked_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.marked[i][j]:
                    print("\033[1m",self.board[i][j], end=' ')
                else:
                    print("\033[0m",self.board[i][j], end=' ')
            print()
    def unmarked_sum(self):
        boardsum = 0
        for i in range(self.size):
            for j in range(self.size):
                if not self.is_marked(i, j):
                    boardsum += self.board[i][j]
        return boardsum
    

with open("input.txt", 'r') as f:
    pullorder = list(map(int, f.readline().split(',')))
    body = f.read()
    body = body.split('\n\n')
    body = list(map(str.split, body))
    # print(body)

bboards = []
for board in body:
    bboards.append(bingoboard(board, 5))

# for board in bboards:
#     board.printboard()
#     board.printmarked()
def pulls(pullorder, bboards):
    for pull in pullorder:
        for board in bboards:
            if board.mark(pull):
                print("Marked:", pull)
                board.print_marked_board()
                if board.check():
                    print("Pull:", int(pull))
                    print("unmarked_sum:", board.unmarked_sum())
                    return board.unmarked_sum() * pull


print(pullorder)
print(pulls(pullorder, bboards))
            

                    