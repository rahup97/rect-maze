import numpy as np
import cv2

class Link():
    value = 0
    parent = 0
    def __init__(self, a, b):
        self.value = a
        self.parent = b
## The readImage function takes a file path as argument and returns image in binary form.
## You can copy the code you wrote for section1.py here.
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
## You can copy the code you wrote for section1.py here.
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
##  You can copy the code you wrote for section1.py here.
def colourCell(img, row, column, flag):   ## Add required arguments here.
    
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
            img[top + 1 : bottom + 2, left + 1 : right] = 150
        if i[0] == row - 1:
            img[top - 1 : bottom, left + 1 : right] = 150
        if i[1] == column + 1:
            img[top + 1 : bottom, left + 1 : right + 2] = 150
        if i[1] == column - 1:
            img[top + 1 : bottom, left - 1 : right] = 150
    if flag == 1:
        img[top + 5 : bottom - 4, left + 5 : right - 4] = 0
    ###################################################
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph(img):  ## You can pass your own arguments in this space.
    graph = {}
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
    r = len(img) / cell
    c = len(img) / cell
    for i in range(r):
        for j in range(c):
            graph[(i, j)] = findNeighbours(img, i, j)
    ###################################################

    return graph

def next_num():          ##This is a sequence for assigning numbers to the cells in recursive function 
    del x[0]
    return x[0]

def numberMaze(graph, initial, new, l):         
    empty = 0                                   ##This assigns numbers to the cells based on a certain algorithm that we have used
                                                  ##Starting from the first cell, the cells are assigned number 1 and everytime a branching occurs the next cells are assigned the next numbers, and if branhing does not occur the same number is continuosly assigned.
    lar = 0                                         ##Them using class. we create links between these numbers, and to find shortest path between cells, we just traverse those certain numbers that we have assigned. suppose 1->3->5->8 are the links created, then to go from 1 to 8, we traverse all cells from 1 to 3 to 5 to the final cell in 8
    
    for k in graph[initial]:
        if new[tuple(k)] == -1:
            empty += 1
    if empty == 0:
        return
    elif empty == 1:
        for i in range(len(graph[initial])):        
            if new[tuple(graph[initial][i])] == -1:
                new[tuple(graph[initial][i])] = new[initial] 
                numberMaze(graph, tuple(graph[initial][i]), new, l) 
    else:
        for i in range(len(graph[initial])):
            if new[tuple(graph[initial][i])] == -1:
                n = next_num()
                new[tuple(graph[initial][i])] = n
                l.append(Link(n, new[initial]))
                numberMaze(graph, tuple(graph[initial][i]), new, l)

def shortestNumberedPath(l, initial, final, path):   ##This function is required to find the shortest path
                                                        ##It acquires the required sequence of links that had been developed using the algorith, explained above and returns it to the required function 
    if final == initial:
        return
    else:
        for i in l:
            if i.value == final:
                parent = i.parent
                break
        path.append(parent)
        shortestNumberedPath(l, initial, parent, path)
        
##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath(graph, initial, final, img): ## You can pass your own arguments in this space.
    #############  Add your Code here   ###############
    shortest = [initial]
    visited = [initial]
    count = 1
    global path
    path = []
    global new
    new = {}
    global l
    l = []
    breadth = len(img)/20          
    length = len(img[0])/20          
    if length == 10:
        initial = (0,0)      
        final = (9,9)           
    else:
        initial = (0,0)
        final = (19,19)
    graph = buildGraph(img)
    for k in graph.keys():
        new[k] = -1
    new[initial] = 1
    global x
    x = range(1, 1000)
    numberMaze(graph, initial, new, l)
    path.append(new[final])
    shortestNumberedPath(l, new[initial], new[final], path)
    path.reverse()
    current = initial
    while(True):
        if current == final:
            return shortest
        for j in graph[current]:
            if not tuple(j) in visited:
                if new[tuple(j)] == new[current]:
                    current = tuple(j)
                    shortest.append(current)
                    visited.append(current)
                    break
                else:
                    if new[tuple(j)] == path[count]:
                        count += 1
                        shortest.append(tuple(j))
                        current = tuple(j)
                        visited.append(current)
                        break
    ###################################################

## This is the main function where all other functions are called. It accepts filepath
## of an image as input. You are not allowed to change any code in this function.
def main(filePath, flag = 0):                 
    img = readImage(filePath)      ## Read image with specified filepath.
    breadth = len(img)/20          ## Breadthwise number of cells
    length = len(img[0])/20           ## Lengthwise number of cells
    if length == 10:
        initial_point = (0,0)      ## Start coordinates for maze solution
        final_point = (9,9)        ## End coordinates for maze solution    
    else:
        initial_point = (0,0)
        final_point = (19,19)
    graph = buildGraph(img)       ## Build graph from maze image. Pass arguments as required.
    shortestPath = findPath(graph, initial_point, final_point, img)  ## Find shortest path. Pass arguments as required.
    print shortestPath             ## Print shortest path to verify
    string = str(shortestPath) + "\n"
    for i in shortestPath:         ## Loop to paint the solution path.
        img = colourCell(img, i[0], i[1], 200)
    if __name__ == '__main__':     ## Return value for main() function.
        return img
    else:
        if flag == 0:
            return string
        else:
            return graph


## The main() function is called here. Specify the filepath of image in the space given.            
if __name__ == '__main__':
    filePath = 'maze00.jpg'        ## File path for test image
    img = readImage(filePath)
    img = main(filePath)           ## Main function call
    cv2.imshow('canvas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





