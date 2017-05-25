import numpy as np
import cv2
np.set_printoptions(threshold=np.nan)
## The readImage function takes a file path as argument and returns image in binary form.
def readImage(filePath):
    #############  Add your Code here   ###############
    img = cv2.imread(filePath, 0)
    ret, binaryImage = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.
def findNeighbours(img,row,column):
    neighbours = []
    #############  Add your Code here   ###############
    i = 0
    while(True):
        if img[i, i] != 0:
            border = i 
            break
        i += 1
    i = border
    cell = 0
    while(True):
        if img[i, i] == 0:
            cell = i 
            break
        i += 1
    if img[cell - border * 2, cell] == 0 or img[cell, cell - border * 2] == 0:
        cell = cell + border
    row_new = (2 * row + 1) * (cell / 2)
    col_new = (2 * column + 1) * (cell / 2)
    top = row_new - (cell / 2) + 1
    bottom = row_new + (cell / 2) - 2
    left = col_new - (cell / 2) + 1
    right = col_new + (cell / 2) - 2
    if img[top, col_new] != 0:
        neighbours.append([row - 1, column])
    if img[bottom, col_new] != 0:
        neighbours.append([row + 1, column])
    if img[row_new, left] != 0:
        neighbours.append([row, column - 1])
    if img[row_new, right] != 0:
        neighbours.append([row, column + 1])
    ###################################################
    return neighbours

##  colourCell function takes 4 arguments:-
##            img - input image
##            row - row coordinates of cell to be coloured
##            column - column coordinates of cell to be coloured
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
def colourCell(img, row, column, colorVal):   ## Add required arguments here.
    
    #############  Add your Code here   ###############
    neighbours = findNeighbours(img, row, column)
    i = 0
    while(True):
        if img[i, i] != 0:
            border = i
            break
        i += 1
    i = border
    cell = 0
    while(True):
        if img[i, i] == 0:
            cell = i 
            break
        i += 1
    if img[cell - border * 2, cell] == 0 or img[cell, cell - border * 2] == 0:
        cell = cell + border
    row_new = (2 * row + 1) * (cell / 2)
    col_new = (2 * column + 1) * (cell / 2)
    top = row_new - (cell / 2) + 1
    bottom = row_new + (cell / 2) - 2
    left = col_new - (cell / 2) + 1
    right = col_new + (cell / 2) - 2
    for i in neighbours:
        if i[0] == row + 1:
            img[top + 1 : bottom + 2, left + 1 : right] = colorVal
        if i[0] == row - 1:
            img[top - 1 : bottom, left + 1 : right] = colorVal
        if i[1] == column + 1:
            img[top + 1 : bottom, left + 1 : right + 2] = colorVal
        if i[1] == column - 1:
            img[top + 1 : bottom, left - 1 : right] = colorVal
    
    ###################################################
    return img

##  Main function takes the filepath of image as input.
##  You are not allowed to change any code in this function.
def main(filePath):
    img = readImage(filePath)
    coords = [(0,0),(9,9),(3,2),(4,7),(8,6)]
    string = ""
    for coordinate in coords:
        img = colourCell(img, coordinate[0], coordinate[1], 150)
        neighbours = findNeighbours(img, coordinate[0], coordinate[1])
        print (neighbours)
        string = string + str(neighbours) + "\n"
        for k in neighbours:
            img = colourCell(img, k[0], k[1], 230)
    if __name__ == '__main__':
        return img
    else:
        return string + "\t"
## Specify filepath of image here. The main function is called in this section.
if __name__ == '__main__':
    filePath = 'maze00.jpg'
    img = main(filePath)
    cv2.imshow('canvas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
