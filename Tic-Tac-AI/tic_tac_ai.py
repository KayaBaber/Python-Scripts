import random as rd
import numpy as np
import copy
#import matplotlib.pyplot as plt




'''Graphics'''
def display_board(gameBoard):
    numerals="    "
    for c in range(len(gameBoard)):
        numerals+= str(c+1) + " "*3
    print numerals
    r=1
    for row in gameBoard:
        print "  "+"-"*4*len(gameBoard)+"-"
        rowNice=str(r)+" | "
        for i in row:
        	     rowNice+=i+" | "
        print rowNice
        r+=1
    print "  "+"-"*4*len(gameBoard)+"-"+" \n"
    return 0




'''AI Implementations'''
def gen_boards(gameBoard, player):
    openings = find_openings(gameBoard)
    boards = []
    for coords in openings:
        b = copy.deepcopy(gameBoard)
        b[coords[0]][coords[1]] = player
        boards.append(b)
    return boards


def find_openings(gameBoard):
    openings=[]
    for rows in range(len(gameBoard)):
        for cols in range(len(gameBoard)):
            if gameBoard[rows][cols] ==" ":    
                openings.append([rows,cols])
    return openings


def minimax(gameBoard, player, oppo, turn):
    if check_win(gameBoard) == player:
        print "WIN! ------------"
        display_board(gameBoard)
        return 1.0
    if check_win(gameBoard) == oppo:
        print "LOSS! -----------"
        display_board(gameBoard)
        return -1.0
    if check_full(gameBoard) == True:
        print "DRAW! -----------"
        display_board(gameBoard)
        return 0.0
    boards=gen_boards(gameBoard, turn)
    scores = []
    mScore = 0
    print scores
    if turn == player:
        for b in boards:
            scores.append(minimax(b, player, oppo, oppo))
        mScore = max(scores)
        #mScore -= 0.1*abs(mScore)
    if turn == oppo:
        for b in boards:
            scores.append(minimax(b, player, oppo, player))
        mScore = min(scores)
        #mScore += 0.1*abs(mScore)
    print scores
    return mScore
     

def minimax_ai(gameBoard, player, oppo):
    openings = find_openings(gameBoard)
    boards = gen_boards(gameBoard, player)
    scores = []
    for b in boards:
        scores.append(minimax(b, player, oppo, player))
    mIndex = scores.index(max(scores))
    coords = openings[mIndex]
    return coords[0], coords[1]



def rand_ai(gameBoard):
    openings = find_openings(gameBoard)
    choice = rd.randrange(0, len(openings))
    coord = openings[choice]
    row=coord[0]
    col=coord[1]
    return row, col




'''Player Input'''
def human_player(gameBoard):
    row = raw_input("Row: ")
    col = raw_input("Column: ")
    
    if (row.isdigit()==False) or (col.isdigit()==False): 
        print "That's not a location. Pick a valid location"
        row, col = human_player(gameBoard)
        
    row =int(row)-1
    col =int(col)-1
    
    if (row > len(gameBoard)-1) or (row < 0):
        print "That row isn't on the board. Pick a valid location."
        row, col = human_player(gameBoard)
    if (col > len(gameBoard)-1) or (col < 0):
        print "That column isn't on the board. Pick a valid location"
        row, col = human_player(gameBoard)
    if gameBoard[row][col] != " ":
        print "That location is taken, pick another"
        row, col = human_player(gameBoard)
    return row, col



    
'''Game Backend'''
def check_win(gameBoard,winLen=3):
    #checks if someone won
    gameBoard=np.array(gameBoard)
    winStringX="X"*winLen
    winStringO="O"*winLen
    
    for row in gameBoard: #check rows
        if ("".join(row.tolist())).find(winStringX)==0:
            return "X"
        if ("".join(row.tolist())).find(winStringO)==0:
            return "O"
            
    for col in range(len(gameBoard)): #check columns
        if ("".join(gameBoard[:,col].tolist())).find(winStringX)==0:
            return "X"
        if ("".join(gameBoard[:,col].tolist())).find(winStringO)==0:
            return "O"
            
    for d in range(winLen-len(gameBoard),len(gameBoard)-winLen): #check diagonals
        across=np.diag(gameBoard,d)
        acrossMirror=np.diag(np.fliplr(gameBoard)) #since numpy diagonals only go one way
        if ("".join(across.tolist())).find(winStringX)==0:
            return "X"
        if ("".join(across.tolist())).find(winStringO)==0:
            return "O"
        if ("".join(acrossMirror.tolist())).find(winStringX)==0:
            return "X"
        if ("".join(acrossMirror.tolist())).find(winStringO)==0:
            return "O"        
    return False
        

def check_full(gameBoard):
    #checks if the gameboard is full
    for rows in gameBoard:
        for cols in rows:
            if cols ==" ":
                return False
    return True






    
'''Main Game Code'''    
def tic_tac_game(N,M):
    gameBoard=[]
    for i in range(N):                     #initialize game board
        gameBoard.append([" "]*N)
    display_board(gameBoard)
    
    for i in range((N**2)):
        print "\nPlayer: "+"X"
        row, col = human_player(gameBoard) #take player move
        #row, col= rand_ai(gameBoard)
        gameBoard[row][col] = "X"
        display_board(gameBoard)
        
        result = check_win(gameBoard, M)   #check for player win
        if result != False:
            if result == "X":
                print "X wins!"
                return "X"
            if result == "O":
                print "O wins!"
                return "O"
        if check_full(gameBoard):
            print "Cat's game!"
            return "Draw"
        
        print "\nPlayer: "+"O"
        #row, col= rand_ai(gameBoard)       #take AI move
        row, col = minimax_ai(gameBoard, "O", "X")
        gameBoard[row][col] = "O"
        display_board(gameBoard)
        
        result = check_win(gameBoard, M)   #check for AI win
        if result != False:
            if result == "X":
                print "X wins!"
                return "X"
            if result == "O":
                print "O wins!"
                return "O"
        if check_full(gameBoard):
            print "Cat's game!"
            return "Draw"
    return 0




def game_stats(N,M):
    XLog=[]
    OLog=[]
    drawLog=[]
    for j in range(10):
        winLog=[]
        XCount=0
        OCount=0
        drawCount=0
        for i in range(100):
            win=tic_tac_game(N,M)
            if win == "X":
                XCount+=1
            if win== "O":
                OCount+=1
            if win=="Draw":
                drawCount+=1
            winLog.append(win)
            print j*100+i
        XLog.append(XCount)
        OLog.append(OCount)
        drawLog.append(drawCount)
    plt.hist(XLog,bins=5)
    plt.hist(OLog,bins=5)
    plt.hist(drawLog,bins=5)
    plt.show()
    #print winLog
    #print "X ", XCount
    #print "O ", OCount
    #print "Draw ", drawCount
    
    
#game_stats(3,3)


tic_tac_game(3,3)