from random import choice
from math import sqrt
import sys
from bokeh.plotting import figure, show

DATA = []

def run(datos):
    casillas_ocupadas = []
    casilla_elegida = eleccion_de_casilla(datos)
    casillas_ocupadas.append(casilla_elegida)
    eliminacion_de_posibilidades = filtracion([casilla_elegida], datos)
    run2(eliminacion_de_posibilidades, casilla_elegida, casillas_ocupadas)

def run2(datos, casilla, casillas_ocu):
    casilla_elegida = eleccion_de_casilla2(datos)
    casillas_ocu.append(casilla_elegida)
    eliminacion_de_posibilidades = filtracion([casilla_elegida], datos)
    if len(eliminacion_de_posibilidades) != 0:
        run2(eliminacion_de_posibilidades, casilla_elegida, casillas_ocu)
    elif len(eliminacion_de_posibilidades) == 0 and len(casillas_ocu) <= sqrt(len(DATA)) - 1:
        run(DATA)
    else:
        casillas_finales = list(map(lambda i: i['id'], casillas_ocu))
        x = list(map(lambda i: i['columna'], casillas_ocu))
        y = list(map(lambda i: i['fila'], casillas_ocu))
        p = figure(title="Board", x_axis_label='column', y_axis_label='row')
        p.circle(x, y, legend_label="Queen.", line_color='red')
        show(p)
        print(f'La solucion es: {casillas_finales}')

def creating_board():
    num = int(input('How many squares width do you want the board?:'))
    tile_id = - num
    row = 0
    column = 0
    diagonalSO_NE = - 1
    diagonalSE_NO = num + 1
    adding_all_rows(num, tile_id, row, column, diagonalSO_NE, diagonalSE_NO)

    return num

def adding_all_rows(squares, index, r, c, dsone, dseno):
  for i in range(squares):
    index = index + squares
    r = r + 1
    dsone = dsone + 1
    adding_row(squares, index, r, c, dsone, dseno)
    dseno = dseno + 1

def adding_row(squares, index, r, c, dsone, dseno):
  for i in range(squares):
    index = index + 1
    c = c + 1
    dsone = dsone + 1
    dseno = dseno - 1
    adding_tile(index, r, c, dsone, dseno)

def adding_tile(index, r, c , dsone, dseno):
  square = {}
  square.update({'id': index})
  square.update({'fila': r})
  square.update({'columna': c})
  square.update({'diagonal SO-NE': dsone})
  square.update({'diagonal SE-NO': dseno})
  DATA.append(square)

def eleccion_de_casilla(datos):
    casilla_elegida = choice(datos)

    return casilla_elegida

def eleccion_de_casilla2(datos):
    free_squares = []
    len_free_squares = 0
    for i in datos:
        new_data = filtracion([i], datos)
        if len(new_data) > len_free_squares:
            len_free_squares = len(new_data)

    for i in datos:
        new_data = filtracion([i], datos)
        if len(new_data) == len_free_squares:
            free_squares.append(i)

    casilla_elegida = choice(free_squares)

    return casilla_elegida

def filtracion(casilla, datos):
    fila_ce = (list(map(lambda i: i['fila'], casilla)))[0]
    columna_ce = (list(map(lambda i: i['columna'], casilla)))[0]
    diagonalSO_NE_ce = (list(map(lambda i: i['diagonal SO-NE'], casilla)))[0]
    diagonalSE_NO_ce = (list(map(lambda i: i['diagonal SE-NO'], casilla)))[0]

    nueva_DATA = [i for i in datos if i['fila'] != fila_ce and i['columna'] != columna_ce and i['diagonal SO-NE'] != diagonalSO_NE_ce and i['diagonal SE-NO'] != diagonalSE_NO_ce]

    return nueva_DATA

if __name__ == '__main__':
    sys.setrecursionlimit(6750)
    creating_board()
    run(DATA)