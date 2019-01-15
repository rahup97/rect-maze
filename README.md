# rectMaze
Rectangular maze solving using image processing using python modules.

We have selected certain stock rectangular maze images of an NxN dimension, and using image processing techniques and shortest path algorithms we have solved these mazes.

This is further divided into three different directories where we are trying to do three different things.

1) findNeighbours - The stock maze images in this directory have been divided into cells. We have found the traversable cells for each cell and highlighted those to depict them as being the "neighbours" for that cell.

2) mazeSolve - Here we find the optimum path from the start coordinate of (0,0) to the final coordinate (n-1, n-1), and highlight the said path.

3) mazeSolve-checkpoints - Here our images contain certain checkpoints depicted with coloured boxes. Here we have found an optimum path considering the fact that we must go through each checkpoint before reaching the finishing cell.

We have used the OpenCV and numpy libraries in Python to find these solutions. The shortest path algorithm we have used is based on the BFS algorithm.

### Credits
IIT-B, e-Yantra Labs

#### Other Contributors
Chethan K P - [chethan749](https://github.com/chethan749)
