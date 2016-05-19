#pseudo code
#given functions:
    '''
    check_win(gameBoard,M)
    find_openings(gameBoard)
    check_full(gameBoard)
    '''
'''
If the game is over, return the score from Xs perspective.
Otherwise get a list of new game states for every possible move
Create a scores list
For each of these states add the minimax result of that state to the scores list
If its Xs turn, return the maximum score from the scores list
If its Os turn, return the minimum score from the scores list
'''

def gen_boards(gameBoard, player):
    openings = find_openings(gameBoard)
    boards = []
    for coords in openings:
        b = gameBoard
        b[coords[0]][coords[1]]
        boards.append(b)
    return boards
    
            

def minimax(gameBoard, player, oppo):
    if check_win(gameBoard) == player:
        return 1.0
    if check_win(gameBoard) == oppo:
        return -1.0
    if check_full(gameboard) == False:
        return 0.0
    boards=gen_boards(gameBoard, oppo)
    scores = []
    for b in boards:
        scores.append(minimax(b, player, oppo))
    mScore = max(scores)0.9
    return mScore - 0.1*abs(mScore)
        
def minimax_ai(gameBoard, player, oppo):
    openings = find_openings(gameBoard)
    boards = gen_boards(gameBoard)
    scores = []
    for b in boards:
        scores.append(minimax(b))
    mIndex = scores.index(max(scores))
    coords = openings[mIndex]
    return coords[0], coords[1]
