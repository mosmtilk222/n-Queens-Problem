import numpy as np
import cv2

def base_board(size):

  '''Function that will return a base image of the board with the specified number of tiles'''

  # Number of pixels width our image will have
  PXWIDTH = 1000

  # Width every tile will have
  tileSize =  PXWIDTH // size

  ## Initializing the matrix with zeros
  # The image will be all black because zero in grayscale is black
  board = np.zeros((PXWIDTH,PXWIDTH))

  ### Initializing the variable white
  ## This will lately be useful to know which tiles are white and which not
  # It is False because this will help to have the left bottom corner black (as it is in chess) 
  white = False

  ## Initializing the max limit of a further range function
  # Helps to not having troubles with multiples
  limit = tileSize* (PXWIDTH//tileSize)

  ## For loop that will iterate through the columns
  # 0 beginning, limit is the end and tile size are the steps
  for start in range(0, limit, tileSize):

    # This handles the problem that when you finish one row and begin with another
    # even numbers size end with a color and begin with the same color
    # odd numbers size end with a color and begin with the other
    # so this stablish the right order for both

    if white == True and size % 2 == 0:
      white = False
    elif white == False and size % 2 == 0:
      white = True

    # For loop that will iterate through the rows
    # same arguments
    for finish in range(0, limit, tileSize):
        
        # This 'paints' the white tiles only when white is true
        if white == True:

          ## Painting
          # 255 is the number of white
          board[finish:finish+tileSize, start:start+tileSize] = 255

          # Declaring white to false because next tile will be black
          white = False

        # If the tile is black just leave it as it is
        else:

          # But the next tile will be white
          white = True

  # Returning the finished np array 
  return board
  
def drawing_lines(path, tile, size, image_number):
    """
    Draws a line where it is not allowed to put a queen in the given image
    
    path: str: path where the image is located
    tile: dict: contains the row, column, diagonal SW-NE, diagonal SE-NW information
    size: int: size of the chessboard
    image_number: int: the number of the image
    """
    # Getting the attributes of the tile
    row = tile['row']
    column = tile['column']
    diagSWNE = tile['diagonal SW-NE']
    diagSENW = tile['diagonal SE-NW']

    # Calculation of tilesize
    tileSize = 1000 // size

    # Calculation of center position of the queen
    cCenter = ((tileSize*column)- tileSize//2, (tileSize*row)- tileSize//2)

    # Calculation of horizontal line starting and ending point
    hLineFirstPoint = (0, tileSize//2 + tileSize*(row-1))
    hLineSecondPoint = (999, tileSize//2 + tileSize*(row-1))
    
    # Calculation of vertical line starting and ending point
    vLineFirstPoint = (tileSize//2 + tileSize*(column-1), 0)
    vLineSecondPoint = (tileSize//2 + tileSize*(column-1), 999)

    # Calculation of diagonal SWNE line starting and ending point
    if diagSWNE < size:
      diagSWNEFirstPoint = (0, (tileSize*diagSWNE)-1)
      diagSWNESecondPoint = ((tileSize*diagSWNE)-1, 0)

    elif diagSWNE > size:
      diagSWNEFirstPoint = ((tileSize*(diagSWNE-size))-1, 999)
      diagSWNESecondPoint = (999, (tileSize*(diagSWNE-size))-1)

    else:
      diagSWNEFirstPoint = (0, 999)
      diagSWNESecondPoint = (999, 0)

    # Calculation of diagonal SENW line starting and ending point
    if diagSENW < size:
      diagSENWFirstPoint = (999, (tileSize*diagSENW)-1)
      diagSENWSecondPoint = ((tileSize*(size-diagSENW))-1, 0)
      
    elif diagSENW > size:
      diagSENWFirstPoint = ((tileSize*(size-(diagSENW-size)))-1, 999)
      diagSENWSecondPoint = (0, (tileSize*(diagSENW-size))-1)
   
    else:
      diagSENWFirstPoint = (999, 999)
      diagSENWSecondPoint = (0, 0)

    # Read the image from the path
    img = cv2.imread(path + f'\image{str(image_number-1)}.jpg')

    # Name of the new image
    name = path + f'\image{str(image_number)}.jpg'

    # Draws horizontal line
    cv2.line(img, hLineFirstPoint, hLineSecondPoint, (200,0,0), 3)

    # Draws vertical line
    cv2.line(img, vLineFirstPoint, vLineSecondPoint, (200,0,0), 3)

    # Draws diagonal SW-NE line
    cv2.line(img, diagSWNEFirstPoint, diagSWNESecondPoint, (0,0,200), 3)

    # Draws diagonal SE-NW line
    cv2.line(img, diagSENWFirstPoint, diagSENWSecondPoint, (0,0,200), 3)

    # Draws a circle for the queen
    cv2.circle(img, cCenter, 10, (0,200,0), 4)

    # Save the new image
    cv2.imwrite(name, img)



def video(path, size):
    """
    Create a video from images in the specified path and with the specified size
    
    path: str: path where the images are located
    size: int: size of the video (number of images)
    """

    # Define the frame size of the output video
    frame_size = (1000, 1000)

    # Create an output video file with the DIVX codec, frame rate of 1 and the previously defined frame size
    out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, frame_size)

    # Iterate over the numbers from 1 to the specified size plus 2
    for number in range(1, size+2):

        # Read the image in the specified path with the name "image{number}.jpg"
        img = cv2.imread(path + f'/image{str(number)}.jpg')

        # Add the image to the output video file
        out.write(img)

    # Release the output video file
    out.release()


