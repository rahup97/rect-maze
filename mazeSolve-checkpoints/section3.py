import numpy as np
import cv2

## Reads image in HSV format. Accepts filepath as input argument and returns the HSV
## equivalent of the image.
def readImageHSV(filePath):
    #############  Add your Code here   ###############
    img = cv2.imread(filePath)
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ###################################################
    return hsvImg

## Reads image in binary format. Accepts filepath as input argument and returns the binary
## equivalent of the image.
def readImageBinary(filePath):
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

##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.
##  You can change the colourCell() functions used in the previous sections to suit your requirements.

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

#####################################    Add Utility Functions Here   ###################################
##                                                                                                     ##
##                   You are free to define any functions you want in this space.                      ##
##                             The functions should be properly explained.                             ##
class Link():
    value = 0
    parent = 0
    def __init__(self, a, b):
        self.value = a
        self.parent = b
        
def next_num():                                     ##This is a sequence for assigning numbers to the cells in recursive function 
    del x[0]
    return x[0]

def numberMaze(graph, initial, new, l):             ##This assigns numbers to the cells based on a certain algorithm that we have used
    empty = 0                                       ##Starting from the first cell, the cells are assigned number 1 and everytime a branching occurs the next cells are assigned the next numbers, and if branhing does not occur the same number is continuosly assigned.
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

def shortestNumberedPath(l, initial, final, path):      ##This function is required to find the shortest path
    if final == initial:                                ##It acquires the required sequence of links that had been developed using the algorith, explained above and returns it to the required function 
        return
    else:
        for i in l:
            if i.value == final:
                parent = i.parent
                break
        path.append(parent)
        shortestNumberedPath(l, initial, parent, path)

def OptimumPath(markers, initial, final, filePath):         ##This function checks the length of all the possible paths and assigns the shortest path length and returns that path as the final shortest optimum path
    shortest = range(5000)
    img = readImageBinary(filePath)
    graph = buildGraph(img)
    if len(markers) == 0:
        shortest = findPath(graph, initial, final, img)
        optimumPath.append(shortest)
        return
    for k in markers:
        path = findPath(graph, initial, k, img)
        if len(path) < len(shortest):
            shortest = path
            marker = k
    markers.remove(marker)
    optimumPath.append(shortest)
    OptimumPath(markers, marker, final, filePath)
##                                                                                                     ##
##                                                                                                     ##
#########################################################################################################


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
                    

## The findMarkers() function returns a list of coloured markers in form of a python dictionaries
## For example if a blue marker is present at (3,6) and red marker is present at (1,5) then the
## dictionary is returned as :-
##          list_of_markers = { 'Blue':(3,6), 'Red':(1,5)}

def findMarkers(filepath):    ## You can pass your own arguments in this space.
    list_of_markers = {}
    #############  Add your Code here   ###############
    i = 10
    img = cv2.imread(filepath)
    while i < len(img):
        j = 10
        while j < len(img[0]):
            pixel = img[i, j]
            if pixel[0] < 10 and pixel[1] < 10:
                list_of_markers['Red'] = ((i-10)/20, (j-10)/20)
            if pixel[0] < 10 and pixel[2] < 10:
                list_of_markers['Green'] = ((i-10)/20, (j-10)/20)
            if pixel[1] < 10 and pixel[2] < 10:
                list_of_markers['Blue'] = ((i-10)/20, (j-10)/20)
            if pixel[0] > 240 and pixel[1] < 10 and pixel[2] > 240:
                list_of_markers['Pink'] = ((i-10)/20, (j-10)/20)
            j += 20
        i += 20
    ###################################################
    return list_of_markers

## The findOptimumPath() function returns a python list which consists of all paths that need to be traversed
## in order to start from the bottom left corner of the maze, collect all the markers by traversing to them and
## then traverse to the top right corner of the maze.

def findOptimumPath(markers, initial, final, filePath):     ## You can pass your own arguments in this space.
    path_array = []
    #############  Add your Code here   ###############
    global optimumPath
    optimumPath = []
    OptimumPath(markers, initial, final, filePath)
    path_array = optimumPath
    ###################################################
    return path_array
        
## The colourPath() function highlights the whole path that needs to be traversed in the maze image and
## returns the final image.

def colourPath(img, path, markers):      ## You can pass your own arguments in this space. 
    #############  Add your Code here   ###############
    for i in path:
        for j in i:
            if j in markers:
                flag = 1
            else:
                flag = 0
            img = colourCell(img, j[0], j[1], flag)

    ###################################################
    return img


## This is the main() function for the code, you are not allowed to change any statements in this part of
## the code. You are only allowed to change the arguments supplied in the findMarkers(), findOptimumPath()
## and colourPath() functions.

def main(filePath, flag = 0):
    imgHSV = readImageHSV(filePath)                ## Acquire HSV equivalent of image.
    listOfMarkers = findMarkers(filePath)              ## Acquire the list of markers with their coordinates. 
    test = str(listOfMarkers)
    imgBinary = readImageBinary(filePath)          ## Acquire the binary equivalent of image.
    initial_point = ((len(imgBinary)/20)-1,0)      ## Bottom Left Corner Cell
    final_point = (0, (len(imgBinary[0])/20) - 1)  ## Top Right Corner Cell
    pathArray = findOptimumPath(listOfMarkers.values(), initial_point, final_point, filePath) ## Acquire the list of paths for optimum traversal.
    print pathArray
    img = colourPath(imgBinary, pathArray, listOfMarkers.values())         ## Highlight the whole optimum path in the maze image
    if __name__ == "__main__":                    
        return img
    else:
        if flag == 0:
            return pathArray
        elif flag == 1:
            return test + "\n"
        else:
            return img
## Modify the filepath in this section to test your solution for different maze images.           
if __name__ == "__main__":
    filePath = "maze00.jpg"                        ## Insert filepath of image here
    img = main(filePath)                 
    cv2.imshow("canvas", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


