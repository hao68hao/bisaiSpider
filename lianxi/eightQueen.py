#! /usr/bin/env python

__metaclass__ = type

class Chessboard:
    board = []
    def __init__(self, queens):
        """the constructor function of Chessboard class"""
        for site in range(queens):
            self.board.append(-1)
        self.arrangements = 0
    def __getitem__(self, index):
        """overloaded const int& operator[] const"""
        return self.board[index]
    def __setitem__(self, index, value):
        """overloaded non-const int& operator[]"""
        self.board[index] = value
    def addCount(self):
        """++arrangements"""
        self.arrangements += 1
    def getCount(self):
        """return arrangements"""
        return self.arrangements

def show(board, queens):
    """show the result"""
    board.addCount()
    print '-------------------------------------'
    print '--> Arrangement index', board.getCount()
    for ix in range(queens):
        print '(%d, %d)' % (ix, board[ix]),
        if ix == queens - 1:
            print

def conflict(board, site):
    """check whether the site can be placed on the board"""
    for ix in range(site):
        if board[ix] == board[site]:
            return True
        if abs(board[ix] - board[site]) == site - ix:
            return True
    return False

def put(board, site, queens):
    """depth first algorithm"""
    for ix in range(queens):
        board[site] = ix
        if not conflict(board, site):
            if site == queens - 1:
                show(board, queens)
            else:
                put(board, site + 1, queens)

def Queens():
    """N-Queens Problem Solver"""
    queens = input('Queens: ')
    checkerboard = Chessboard(queens)
    put(checkerboard, 0, queens)
    print '-------------------------------------'
    print '--> total arrangements:', checkerboard.getCount()

Queens()
