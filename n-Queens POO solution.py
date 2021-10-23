from random import choice
from math import sqrt
from sys import setrecursionlimit
from bokeh.plotting import figure, output_file, show

class Board:

    def __init__(self):
        #The board is composed by a bunch of squares
        self.squares = []

    def create_board(self, width):

        id = - width
        row = 0
        column = 0
        diagonalSWNE = - 1
        diagonalSENW = width + 1
        self.create_all_rows(width, id, row, column, diagonalSWNE, diagonalSENW)

    def create_all_rows(self, width, index, r, c, dswne, dsenw):

        for i in range(width):
            index = index + width
            r = r + 1
            dswne = dswne + 1
            self.create_row(width, index, r, c, dswne, dsenw)
            dsenw = dsenw + 1

    def create_row(self, width, index, r, c, dswne, dsenw):

        for i in range(width):
            index = index + 1
            c = c + 1
            dswne = dswne + 1
            dsenw = dsenw - 1
            isoccupied = False
            available = True
            s = Square(index, r, c, dswne, dsenw, isoccupied, available)
            self.squares.append(s)

class Square:

    def __init__(self, id, row, column, diagonalSWNE, diagonalSENW, isoccupied, available):
        self.id = id
        self.row = row
        self.column = column
        self.diagonalSWNE = diagonalSWNE
        self.diagonalSENW = diagonalSENW
        self.isoccupied = isoccupied
        self.available = available
        self.matchesFound = 0

def initialization(data):
    #Choosing a random square
    choosen_square = choice(data.squares)
    filtration(choosen_square, data.squares)

def filtration(square, data):
    #Declaring the attributes of the choosen square (cs) to filtrate the data adter
    square.isoccupied = True
    row_cs = square.row
    column_cs = square.column
    diagonalSWNE_cs = square.diagonalSWNE
    diagonalSENW_cs = square.diagonalSENW

    #Modyfying the availability of the squares if one of its attributes matches the same attribute in an occupied square
    for i in data:
        if i.row == row_cs or i.column == column_cs or i.diagonalSWNE == diagonalSWNE_cs or i.diagonalSENW == diagonalSENW_cs:
            i.available = False

def choosing_best_square(data):
    free_squares = [i for i in data if i.available == True]
    for square in free_squares:
        square.isoccupied = True
        row_cs = square.row
        column_cs = square.column
        diagonalSWNE_cs = square.diagonalSWNE
        diagonalSENW_cs = square.diagonalSENW

        for i in free_squares:
            #How many squares have same values
            if i.row == row_cs or i.column == column_cs or i.diagonalSWNE == diagonalSWNE_cs or i.diagonalSENW == diagonalSENW_cs:
                square.matchesFound += 1
    minimum_coincidences = min([i.matchesFound for i in free_squares])
    options = [i for i in free_squares if i.matchesFound == minimum_coincidences]
    choosen_square = choice(options)
    for i in free_squares:
        i.matchesFound = 0
        i.isoccupied = False
    return choosen_square

def plotting(data):
    output_file('rectangles.html')

    #os means occupied squares
    Top_os = [i.row for i in data if i.isoccupied == True]
    Right_os = [i.column for i in data if i.isoccupied == True]
    Bottom_os = [i-1 for i in Top_os]
    Left_os = [i-1 for i in Right_os]

    p = figure(width=1000, height=1000)
    p.quad(top=Top_os, bottom=Bottom_os, left=Left_os, right=Right_os, color="#000000")
    show(p)

def run(board):
    best_square = choosing_best_square(board.squares)
    filtration(best_square, board.squares)

def main(board):
    backup = board
    if len([i for i in board.squares if i.available == True]) != 0:
        run(board)
        main(board)
    elif len([i for i in board.squares if i.available == True]) == 0 and len([i for i in board.squares if i.isoccupied == True]) <= sqrt(len(board.squares))-1:
        board = backup
        initialization(board)
        main(board)
    else:
        pass

if __name__ == '__main__':
    setrecursionlimit(6750)
    b = Board()
    b.create_board(15)
    initialization(b)
    main(b)
    ocu = [i.id for i in b.squares if i.isoccupied == True ]
    print(ocu)
    plotting(b.squares)



