from random import choice
from math import sqrt
import csv
import time
from GUI import base_board, drawing_lines, video
from PIL import Image
from board import create_board
import os
from datetime import datetime

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

    ## Creating the image containing the new chosen tile
    # Calling drawing lines with its arsguments
    global image_num
    image_num = 2

    drawing_lines(path, chosen_tile, num, image_num)

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

    ## Creating the image containing the new chosen tile
    # Calling drawing lines with its arsguments
    global image_num
    image_num += 1

    drawing_lines(path, chosen_tile, num, image_num)

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

        #drawing_lines(img, occ_tiles)

        # Getting the list of ids of all the tiles
        ids_occ_tiles = list(map(lambda i: i['id'], occ_tiles))

        # Showing the results
        ids_occ_tiles.sort()
        print(f'The solution is: {ids_occ_tiles}')

        # Timer end
        toc = time.time()

        # Getting the number of seconds the script took
        seconds = toc-tic

        # Appending the result to our csvfile
        with open('solutions.csv', 'a') as csvfile:

            writer = csv.writer(csvfile)

            # Appending solution, n (number of queens) and the time it took with 4 decimals
            writer.writerow([ids_occ_tiles] + [len(ids_occ_tiles)] + ["%.4f" % seconds])

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

    # Num will be the width of our board
    ## The number of tiles will be num squared
    global num
    num = int(input('How many squares width do you want the board?:'))

    # Number that will tag every image in the folder
    global image_num
    image_num = 1

    # Create the board and save it in DATA
    DATA = create_board(num)

    # Setting the timer start
    tic = time.time()

    ## Date will be the name of the folder where the image will be saved
    # Date will be a string containing the following format YYYY-MM-DD HH.MM.SS 
    date = str(datetime.fromtimestamp(tic)).replace(':', '.')[0:19]

    ## Saving the image in the proper folder
    # Getting the dictionary where we are currently working
    parentDir = os.getcwd()

    # The path to the folder
    global path
    path = os.path.join(parentDir, 'images', str(num), date)

    # Making the folder in the proper path
    os.mkdir(path)
    
    # Creating the base image
    img = Image.fromarray(base_board(num))
    img = img.convert("RGB")

    # Saving the image in the folder
    img.save(f'images/{str(num)}/{date}/image{str(image_num)}.jpg')
  
    # Calling the run function to begin the solving algorithm
    run(DATA)

    video(path, num)
