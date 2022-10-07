from random import choice
from math import sqrt

# DATA will contain all the tiles with their values
DATA = []

def creating_board():

    # Num will be the width of our board
    ## The number of tiles will be num squared
    num = int(input('How many squares width do you want the board?:'))

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

def run(datos):

    ## The first run function is the first step in the algorithm
    ## Its different to run 2 because it makes simpler processes than run 2

    # Declaring a list of tiles that will be occupied
    # The occupied tiles will be the ones that have a queen
    occ_tiles = []

    # Firstly we will choose one random tile

    ## The first decission is made ramdomly because any tile we choose
    ## will decrease the same number of possibilitys in the next decission

    chosen_tile = random_choice(datos)

    # And add it to the occupied tiles
    occ_tiles.append(chosen_tile)

    # This variable will contain a list of tiles that are not affected
    # by the last tile we chose
    available_tiles = filtration([chosen_tile], datos)

    # Calling run 2 having made the first decission and its 
    # corresponding filtration and sending them as arguments
    run2(available_tiles, occ_tiles)

def run2(data, occ_tiles):

    # The chosen_tile will be assigned by the best choice function,
    # data is the list of available tiles
    chosen_tile = best_choice(data)

    # Adding the tile to the occupied tiles list
    occ_tiles.append(chosen_tile)

    # Getting the board filtrated again
    available_tiles = filtration([chosen_tile], data)

    # If we still have available tiles we call run2 again
    if len(available_tiles) != 0:
        
        ## Available tiles will decrease every time we call the function
        ## and occupied tiles the same but increasing

        # Available tiles and occupied tiles as arguments
        run2(available_tiles, occ_tiles)
    
    # If we don't have any available tiles and the number of tiles occupied is smaller than the width
    # we restart the algorithm
    elif len(available_tiles) == 0 and len(occ_tiles) <= sqrt(len(DATA)) - 1:

        ## If this if statement is true means that the algorithm failed

        # Restart all 
        run(DATA)

    # If all the last statements are false means that we have found the answer
    else:

        # Getting the list of ids of all the tiles
        ids_occ_tiles = list(map(lambda i: i['id'], occ_tiles))

        # Showing the results
        ids_occ_tiles.sort()
        print(f'The solution is: {ids_occ_tiles}')

def random_choice(data):

    # Getting a random tile with the math function called choice
    chosen_tile = choice(data)

    # Returns the tile so its type is dictionarie
    return chosen_tile

def best_choice(data):

    # Tiles that after a filtration left the same number
    # of possibilities to the next choice
    best_tiles = []

    # This variable contains the number of available tiles
    len_best_tiles = 0

    ## This for loop is to determine how many possibilities 
    ## the best options can leave us

    # Data es the list of available tiles
    for tile in data:

        ## The variable new_data contains the list of possibilities 
        ## after filtrating data with the tile given

        # Tile is put inside a list because filtration needs
        # it with that format
        new_data = filtration([tile], data)

        # This if statement compares between the length of new_data and 
        # and the number of best tiles we have established before

        if len(new_data) > len_best_tiles:

            # If we have found a greater number of possibilities left
            # then len_best_tiles is updated to the greater number
            len_best_tiles = len(new_data)

    ## This for loop is to find all the possibilities that leave the
    ## same number of possibilities which we determined in the last for loop

    # data is the list of tiles
    for tile in data:

        ## The variable new_data contains the list of possibilities 
        ## after filtrating data with the tile given

        # Tile is put inside a list because filtration needs
        # it with that format
        new_data = filtration([tile], data)

        # The following if statement selects the tiles that left the 
        # same amount of possibilities as the number we calculated before
        if len(new_data) == len_best_tiles:

            # Add the whole tile to our list of best tiles
            best_tiles.append(tile)

    # Again we choose between the best options because all the tiles
    # should leave the same number of possibilities
    # So it doesn't matter which tile of best_tiles we choose
    chosen_tile = choice(best_tiles)

    # Finally it returns the whole tile
    return chosen_tile

def filtration(tile, data):

    ### Filtration is a function which will take one tile and will
    ### return all the tiles that have different row, column and diagonals

    ## Beginning from the center
    ## The first argument of map is a
    ## lambda function that will get the value with the specified key inside brackets
    ## The second arguments is the tile we passed to the function
    ## Then we cast all that into a list
    ## Finally we get the first element of the list, which is the number we want

    # We do this with all the properties of the tile except id

    row_t = (list(map(lambda i: i['row'], tile)))[0]
    column_t = (list(map(lambda i: i['column'], tile)))[0]
    diagonalSW_NE_t = (list(map(lambda i: i['diagonal SW-NE'], tile)))[0]
    diagonalSE_NW_t = (list(map(lambda i: i['diagonal SE-NW'], tile)))[0]

    ## This is the core of the algorithm
    ## Basically it gets all the tiles that have different row, column and diagonals,
    ## all at the same time

    # new_data is a list of all the tiles that have different properties
    new_data = [i for i in data if i['row'] != row_t and i['column'] != column_t and i['diagonal SW-NE'] != diagonalSW_NE_t and i['diagonal SE-NW'] != diagonalSE_NW_t]

    # Returning the list of filtrated tiles
    return new_data

if __name__ == '__main__':

    # Create the board and save it in DATA
    creating_board()

    # Calling the run function to begin the solving algorithm
    run(DATA)
