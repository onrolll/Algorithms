import math

class Text(object):
    def __init__(self, words, width):
        self.words = words
        self.page_width = width
        self.str_arr = words
        self.memo = {}
        self.parent = {}

    def total_length(self, str):
        total = 0
        for string in str:
            total = total + len(string)
        total = total + len(str) # spaces
        return total

    def badness(self, str):
        line_len = self.total_length(str)
        if line_len > self.page_width:
            return float('nan')
        else:
            return math.pow(self.page_width - line_len, 3)

    def dp(self):
        n = len(self.str_arr)
        self.memo[n-1] = 0

        return self.judge(0)

    def judge(self, i):
        if i in self.memo:
            return self.memo[i]

        self.memo[i] = float('inf')
        for j in range(i+1, len(self.str_arr)):
            bad = self.judge(j) + self.badness(self.str_arr[i:j])
            if bad < self.memo[i]:
                self.memo[i] = bad
                self.parent[i] = j

        return self.memo[i]

if __name__ == '__main__':
    text = 'ajdslf dksadkf fksks kdkaksofofmgm fmslda'
    words = text.split()
    tj = Text(words, 20)
    tj.dp()
    parent = tj.parent
    k = 0
    i = 0
    while k < len(words):
        if k not in parent:
            break
        k = parent[k]
        for x in range(i, k):
            print(words[x])
        print('\n')
        i = k


    print(tj.parent)
    print(tj.memo[0])
    print(tj.memo[len(words)-1])
