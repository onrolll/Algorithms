from numpy import argmin

def justify(text, line_width):

    parent = {}
    DP(0, words, parent)
    k = 0
    i = 0
    while k < len(words):
        k = parent[k]
        for x in range(i, len(words) - i):
            if words[x] == k:
                print('\n')
                i += x
                break
            else:
                print(word[x] + ' ')


def DP(i, words, parent):
    if i == len(words):
        return 0
    else:
        #while j < len(words) +
        sums = {}
        for j in range(i+1,len(words)):

            sum = DP(j, words, parent) + badness(words, i,j, 15)
            print(sum)
            sums.append(sum)
        parent[i] = i + 1 + argmin(sums)
        print(min(sums))
        return sums[min(sums)]



def rJustify(text, i, parent):
    if i == len(text):
        return False
    else:
        result = []
        for j in range(n+1):
            candidate = badness(text, i, j) + rJustify(text, j, parent)
            if candidate == False:
                break
            result.append(candidate)
        parent[i] == argmin(result)
        return min(result)
def badness(words, i, j, line_width):
    if (sum(len(words[x]) for x in range(i,j+1)) + j - i) > line_width:
        return float('inf')
    else:
        return (line_width - sum(len(words[x]) for x in range(i,j+1)) + j - i)**3


if __name__ == '__main__':
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    words = text.split()
    justify(words, 15)
