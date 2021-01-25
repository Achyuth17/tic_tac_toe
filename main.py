board=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def play(board):
    grid={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
    played=[]
    player_x=input("Enter the first player's name : ")
    player_y=input("Enter the second player's name : ")

    while len(played)<(len(board)*len(board[0])):
        print_board(board)

        print(f"Player {player_x} turn to play!!")
        play_x=int(input("Enter the grid number at which u want to play : "))
        while play_x in played or (play_x<=0 or play_x>9):
            print("Invalid position !! ")
            play_x=int(input("Enter the grid number at which u want to play : "))
        played.append(play_x)
        board[grid[play_x][0]][grid[play_x][1]]='X'

        print_board(board)
        if victory('X'):
            print(f"{player_x} is the winner !!!! ")
            break

        if len(played)<(len(board)*len(board[0])):
            print(f"Player {player_y} turn to play !! ")
            play_y=int(input("Enter the grid number at which u want to play : "))
            while play_y in played or (play_y<=0 or play_y>9) :
                print("Invalid position !! ")
                play_y=int(input("Enter the grid number at which u want to play : "))
            played.append(play_y)
            board[grid[play_y][0]][grid[play_y][1]]='O'

            if victory('O'):
                print(f"{player_y} is the winner !!!! ")
                break
    else:
        print("Tied Match !!! ")

def victory(chr):

    for i in range(len(board)):
        if board[i].count(chr)==3:
            return True

    for i in range(len(board)):
        temp=[]
        for j in range(len(board[0])):
            temp.append(board[j][i])
            if temp.count(chr)==3:
                return True

    cnt=0
    for i in range(len(board)):
        if board[i][i]==chr:
            cnt+=1
    if cnt==3:
        return True            

    cnt=0
    for i in range(len(board)-1,-1,-1):
        if board[i][len(board)-i-1]==chr:
            cnt+=1
    if cnt==3:
        return True


    return False    


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j==2:
                print(board[i][j])
            else:
                print(board[i][j],end=' | ')

play(board)
