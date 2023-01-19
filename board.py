# DATA will be filled with tiles
DATA = []

def create_board(num):

    '''Function that will create a chess board'''

    # DATA will contain all the tiles with their values


    ## All the following variables are initialiazed as if they
    ## were part of the properties of the tile 0,0

    # Identifier of the tile
    tile_id = - num

    # Row to which the tile belongs
    ## The number of rows will be equal to num
    row = 0

    # Column to which the tile belongs
    ## The number of columns will be equal to num
    column = 0

    ### SW_NE means that the diagonal go from the SouthWest to the NorthEast
    ### It begins in the top left corner and ends in the bottom right corner

    ### SE_NW means that the diagonal go from the SouthEast to the NorthWest
    ### It begins in the top right corner and ends in the bottom left corner

    # Diagonal SW-NE to which the tile belongs

    # Begins with a value of -1 because 
    # when the tile we are creating moves down in the rows it adds 1 to the diagonal
    # and when the tile we are creating moves to the right it adds 1 more

    ## The number of diagonals SW-NE will be (num*2) - 1
    diagonalSW_NE = - 1

    # Diagonal SE-NW to which the tile belongs

    #Begins with a value of num + 1 because
    # when the tile we are creating moves down it adds 1 to the diagonal
    # and when the tile we are creating moves to the right 1 is substracted

    ## The number of diagonals SE-NW will be (num*2) - 1
    diagonalSE_NW = num + 1

    # Calling the adding_all_rows function
    adding_all_rows(num, tile_id, row, column, diagonalSW_NE, diagonalSE_NW)

    return DATA
def adding_all_rows(width, index, r, c, dswne, dsenw):

    # Iterating n times depending on the width
    # In every iteration it will declare the properties of the tile
    # with the properties of column 0 and the row number i 

    # In this function we are moving down in every iteration  

    for i in range(width):

        # Every iteration the id adds n because every row
        # have n tiles and because we are starting a new one
        # we must increase it
        index += width

        # As I said moving down in the rows
        r += 1

        # Incrementing 1 the diagonal before we call adding_tile
        # because it is like we are moving one diagonal to the right
        dswne += 1

        # Calling adding_tile 
        adding_tile(width, index, r, c, dswne, dsenw)

        # Incrementing 1 the diagonal after we call adding_tile
        # because it is like we are moving one diagonal to the left

        # Remember dswne increases left to right and increases right to left
        dsenw += 1

def adding_tile(width, index, r, c, dswne, dsenw):

    # Iterating n times depending on the width
    # In every iteration it will declare the properties of every tile in the row
    # with the propertie of row = r and the column number i

    # In this function we are moving to the right of the row in every iteration

    for i in range(width):

        # Index increase 1
        index += 1

        # Column increase 1
        c += 1

        # Diagonal SW-NE increase 1
        dswne += 1

        # Diagonal SE-NW decrease 1
        dsenw -= 1

        # Calling adding_tile_to_DATA and passing all the right arguments
        adding_tile_to_DATA(index, r, c, dswne, dsenw)

def adding_tile_to_DATA(index, r, c , dswne, dsenw):

    ## Finally declaring all the values in a dictionary

    # Declaring an empty dictionarie  
    tile = {}

    # Adding every value of the tile
    tile.update({'id': index})
    tile.update({'row': r})
    tile.update({'column': c})
    tile.update({'diagonal SW-NE': dswne})
    tile.update({'diagonal SE-NW': dsenw})

    # Adding the tile to DATA
    DATA.append(tile)

    # So at the end we have a list of all the tiles,
    # the tiles are dictionaries with their own values
    # The keys in all tiles are id, row, column, diagonal SW-NE, diagonal SE-NW
