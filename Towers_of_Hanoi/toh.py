class Tower(object):
    """docstring for Tower."""
    def __init__(self, index):
        super(Tower, self).__init__()
        self.index = index
        self.discs = []

    def moveTopTo(self, tower):
        top = self.discs.pop()
        tower.appendDisc(top)
        print("Moved top from tower %d to tower %d"% (self.index,tower.index))

    def moveDiscs(self,discs, destination, buffer):
        if discs > 0:
            self.moveDiscs(discs-1, buffer, destination)
            self.moveTopTo(destination)
            buffer.moveDiscs(discs-1, destination, self)
        #printState(self, destination, buffer)

    def appendDisc(self, disc):
        if len(self.discs) > 0 and disc >= self.discs[-1]:
            print('Error appending disc %d to tower %d.' % (disc,self.index))
            return
        self.discs.append(disc)

    def print(self):
        print('Tower %d' % (self.index))
        for i in range(len(self.discs)-1, -1, -1 ):
            print('%d -> %d \n' % (i, self.discs[i]))

def printState(t1,t2,t3):
    unordered = [t1,t2,t3]
    ordered = [0,1,2]
    for i in range(3):
        if unordered[i].index == 0:
            ordered[0] = unordered[i]
        elif unordered[i].index == 1:
            ordered[1] = unordered[i]
        else:
            ordered[2] = unordered[i]
    print('===========BeginState==============')
    for i in range(3):
        ordered[i].print()
    print('===========EndState================')
if __name__ == '__main__':
    t1 = Tower(0)
    t2 = Tower(1)
    t3 = Tower(2)

    #towers_of_hanoi = [[Tower(i)] for i in range(3)]

    t1.appendDisc(55555)
    t1.appendDisc(5555)
    t1.appendDisc(555)
    t1.appendDisc(55)
    t1.appendDisc(5)

    towers_of_hanoi = [t1,t2,t3]
    t1.moveDiscs(5,t3,t2)


    for i in range(3):
        towers_of_hanoi[i].print()
