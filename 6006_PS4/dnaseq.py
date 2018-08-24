#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.dict = {}
        for pair in pairs:
            self.put(pair[0] , pair[1])
    # Associates the value v with the key k.
    def put(self, k, v):
        if k not in self.dict:
            self.dict[k] = []
        self.dict[k].append(v)

    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        if k not in self.dict:
            return []
        return self.dict[k]

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)

#Code bellow works using provided classes and methods
# def subsequenceHashes(seq, k):
#     hash = ''
#     prev_item = ''
#     position = 0
#     for subseq in kfasta.subsequences(seq, k):
#         if hash == '':
#             hash = RollingHash(subseq)
#         else:
#             hash.slide(prev_item, subseq[len(subseq) - 1])
#         yield (hash.current_hash(), (position, subseq))
#         position += 1
#         prev_item = subseq[0]

def subsequenceHashes(seq, k):
    try:
        subseq = ''
        hash = ''
        for i in range(0, k):
            subseq += seq.__next__()
        hash = RollingHash(subseq)
        position = 0
        while  True:
            yield (hash.current_hash(),(position, subseq))
            prev_item = subseq[0]
            subseq = subseq[1:]
            subseq += seq.__next__()
            hash.slide(prev_item, subseq[-1])
            position += 1
    except StopIteration:
        return


# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
    assert m >= k
    try:
        position = 0
        while True:
            subseq = ''
            for i in range(0, k):
                subseq += seq.__next__()
            rh = RollingHash(subseq)

            yield (rh.current_hash(),(position, subseq))
            for i in range(0, m - k):
                seq.__next__()
            position += m
    except StopIteration:
        return
# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):
    print("Building table from sequence A...")
    seqtable = Multidict(intervalSubsequenceHashes(a, k, m))
    print("...done building table")

    for hashval, (bpos, bsubseq) in subsequenceHashes(b, k):
        for apos, asubseq in seqtable.get(hashval):
            if asubseq != bsubseq:
                continue
            yield(apos, bpos)
    return

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0]))
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)
