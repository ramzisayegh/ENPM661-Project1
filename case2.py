#link to GitHub
#https://github.com/ramzisayegh/ENPM661-Project1

import numpy as np 
import copy 

#declare initial state
#change this based on whichever test case
initial = [[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]]

#declare final or goal state
#will always be the same
final = [[1, 2, 3, 4],[ 5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 0]]

#function to find location of blank tile. returns (row,col) coordiante of blank tile
#reads node as numpy array and uses np.where to find indeces of blank tile
#returns (x,y) coordinate of blank tile
def FindBlank(puzzle):
	puzzle = np.asarray(puzzle)
	blank = np.where(puzzle==0)
	blank_index = list(zip(blank[0],blank[1]))
	return blank_index[0]




#Functions to move the blank tile left, right, up, or down one space
#All four functions follow the same logic

#call FindBlank function to find blank tile and store as x,y
#create a deepcopy of the node passed through as to not modify it, just find the child
#if the blank tile is not on the left edge, switch blank tile and tile to the left of it
#if the blank tile cannot be moved to the left, return the child = 0 to be discarded later
def MoveLeft(node_left):
	left_child = copy.deepcopy(node_left)
	coor = FindBlank(left_child)
	x = coor[0]
	y = coor[1]
	if y>0:
	    left_ele = left_child[x][y-1]
	    left_child[x][y] = left_ele
	    left_child[x][y-1] = 0
	else:
		left_child = 0
	return left_child

def MoveRight(node_right):
	right_child = copy.deepcopy(node_right)
	coor = FindBlank(node_right)
	x = coor[0]
	y = coor[1]
	if y<3:
	    right_ele = right_child[x][y+1]
	    right_child[x][y] = right_ele
	    right_child[x][y+1] = 0
	else:
		right_child = 0
	return right_child

def MoveUp(node_up):
	up_child = copy.deepcopy(node_up)
	coor = FindBlank(node_up)
	x = coor[0]
	y = coor[1]
	if x>0:
	    up_ele = up_child[x-1][y]
	    up_child[x][y] = up_ele
	    up_child[x-1][y] = 0
	else:
		up_child = 0
	return up_child

def MoveDown(node_down):
	down_child = copy.deepcopy(node_down)
	coor = FindBlank(node_down)
	x = coor[0]
	y = coor[1]
	if x<3:
	    down_ele = down_child[x+1][y]
	    down_child[x][y] = down_ele
	    down_child[x+1][y] = 0
	else:
		down_child = 0
	return down_child



#function to convert list to an integer to be compared easily
#flattens list, converts to string then to integer by joining strings
def listToInt(node):
	li1D = sum(node, [])
	s = [str(i) for i in li1D]
	an_integer = int("".join(s))
	return an_integer

#function to check if a node has been visited
#calls listToInt function and compares with visited list that is constantly updated
#returns True if already visited, False if not
def isVisited(node1):
	check = copy.deepcopy(node1)
	x = listToInt(check)
	for i in range(len(visited)):
		if x==visited[i]:
			return True
		else:
			return False





#initialize queue data structure and visited list
queue = []
visited = []

#push initial state into queue and its converted integer form into visited
queue.append(initial)
visited.append(listToInt(initial))


#while there are still nodes in the queue, we will keep searching for solution
while (len(queue)>0):

	#initialize done variable to 0 and only change to 1 when solution is found, instigating break out of while loop
    done = 0

    #start searching process by popping first node in queue, following FIFO convention for BFS search
    node_i = queue.pop(0)

    #find all children of node_i (some may be 0 according to MoveAction functions)
    children = [MoveLeft(node_i), MoveRight(node_i), MoveUp(node_i), MoveDown(node_i)]
    child_real = []

  	#check all children and append child_real list with only possible solution (i.e. excluding children=0)
    for j in range(len(children)):
	    if (children[j] != 0):
		    child_real.append(children[j])

	#loop through each real child
	#if child has NOT been visited, check if it is the goal state
	#if it IS the goal state, puzzle is solved, done=1 and end search
	#if it is NOT goal state, push child into queue and append visited list with child
    for i in range(len(child_real)):
	    if (isVisited(child_real[i])==False):
		    if (listToInt(child_real[i])==listToInt(final)):
			    solved = child_real[i]
			    visited.append(listToInt(solved))
			    done = 1
			    break
		    else:
			    queue.append(child_real[i])
			    visited.append(listToInt(child_real[i]))

	#once puzzle is solved, break out of while loop
    if (done == 1):
    	break


#print solved puzzle
print("Puzzle Solved!")
print(solved)


#open an output txt file for states generated
output = open("Case2_Output.txt","w")

#fill txt file with visited list (states will be one long string of numbers)
output.write('\n'.join(str(x) for x in visited))
