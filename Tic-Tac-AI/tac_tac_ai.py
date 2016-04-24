import random as rd

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
    
    
def rand_ai(gameBoard):
    row = rd.randrange(0, len(gameBoard))  
    col = rd.randrange(0, len(gameBoard))  
    if gameBoard[row][col] != " ":
        row, col = rand_ai(gameBoard)
    return row, col


def is_win?(gameBoard):
    winString="X"*len(gameBoard
    winStrinf2=" O"*len(gameBoard)
    for row in gameBoard:
        if row.join == winString1:
            return "X"
        if row.join == winString2:
            return "0"
        NJ
    
def tic_tac_game(N):
    gameBoard=[]
    for i in range(N):
        gameBoard.append([" "]*N)
    display_board(gameBoard)
    for i in range(N**2):
        print "\nPlayer: "+"X"
        row, col = human_player(gameBoard)
        gameBoard[row][col] = "X"
        display_board(gameBoard)
        row, col= rand_ai(gameBoard)
        gameBoard[row][col] = "O"
        display_board(gameBoard)
    display_board(gameBoard)
    return 0


tic_tac_game(3)
