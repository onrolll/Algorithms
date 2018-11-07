class TextJustificator(object):
    """docstring for TextJustificator."""
    def __init__(self, words, line_width):
        super(TextJustificator, self).__init__()
        self.words = words
        self.width = line_width
        self.memo = {}
        self.parent = {}

    def dp(self):
        n = len(words)
        self.memo[n] = 0

        self.justify(0)

    def justify(self, i):
        if i in self.memo:
            return self.memo[i]

        self.memo[i] = float('inf')

        for j in range(i+1, len(words) + 1  ):
            bad = self.justify(j) + self.badness(words[i:j])
            if bad < self.memo[i]:
                self.memo[i] = bad
                self.parent[i] = j
        return self.memo[i]

    def badness(self, words):
        print('in badness')
        print(words)
        len = self.total_length(words)
        print(len)
        if len > self.width:
            return float('inf')
        else:
            return (self.width - len)**3

    def total_length(self, words):
        line = ' '.join(words)
        return len(line)

    def printSolution(self):
        i = 0;
        k = 0
        while k < len(self.words):
            k = self.parent[k]

            line = ' '.join(self.words[i:k])
            print(line)
            i = k


if __name__=='__main__':
    text1 = 'hello along quite brute algo'
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    words = text.split()
    tj = TextJustificator(words, 20)
    tj.dp()
    print('memo[0]',tj.memo[0])
    print(tj.memo)
    print(tj.parent)
    tj.printSolution()
