import numpy as np


def find_moves(position, boardSize):
	#checks for availible moves given position and returns allowed new positions
	moves = [[2,1], [1,2], [-1,2], [-2,1],
			 [-2,-1], [-1,-2], [1,-2], [2,-1]]
	allowed = []
	for move in moves:
		newPos = position + move
		if np.all(newPos >= [0,0]) and np.all(newPos < [boardSize,boardSize]):
			allowed.append(newPos)
	return(np.array(allowed))


board = np.array([[0.0]*8]*8)

position = np.array([0,0])
print(position)
board[position[0], position[1]] = 1
print(board)

def iterate_board(oldBoard):
	#takes in the current board state and returns the next board state
	#probabilities move from one coord to another and superpose
	#this gives a new probability state
	
	newBoard = np.array([[0.0]*8]*8)
	for x in len(oldBoard):
		for y in len(oldBoard):
			position = np.array[x,y]
			newPositions = find_moves(position,len(oldBoard))
			print(newPositions)
			posCount = len(newPositions)
			probability = 1.0 / float(posCount)
	for pos in newPositions:
		board[pos[0], pos[1]] = board[pos[0], pos[1]] + probability
		print(board[pos[0], pos[1]])
	print(board)