class Queens(object):
    """docstring for Queens."""

    def __init__(self, size):
        super(Queens, self).__init__()
        self.x = 1
        self.size = size
        self.board = [-1] * size

    def nQueens(self):
        #board = [-1] * size
        done = self.rQueens( 0)
        if done:
            print(board)

    def rQueens(self, current):
        if self.size == current:
            print(self.board)
            print('------> %d'%(self.x))
            self.x+=1
            return True
        else:
            for i in range(self.size):
                self.board[current] = i
                if self.noConflicts(current):
                    done = self.rQueens(current + 1, )
                    #if done:
                        #return True
            return False

    def noConflicts(self, current):
        for i in range(current):
            if self.board[i] == self.board[current]:
                return False
            elif abs(self.board[current] - self.board[i]) == abs(current - i):
                return False
        return True

if __name__ == '__main__':
    queens = Queens(10)
    queens.nQueens()
