board=[
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

def play(board):
    played=[]
    player_x=input("Enter the first player's name : ")
    player_y=input("Enter the second player's name : ")

    while len(played)<9:
        print_board(board)

        print(f"Player {player_x} turn to play!!")
        play_x=list(map(int,input("Enter the position at which u want to enter : ").split(" ")))
        while play_x in played:
            print("Invalid position !!")
            play_x=list(map(int,input("Enter the position at which u want to enter : ").split(" ")))
        played.append(play_x)
        board[play_x[0]][play_x[1]]='X'

        print_board(board)
        if victory('X'):
            print(f"{player_x} is the winner !!!! ")
            break

        if len(played)<9:
            print(f"Player {player_y} turn to play !! ")
            play_y=list(map(int,input("Enter the position at which u want to enter : ").split(" ")))
            while play_y in played :
                print("Invalid position !! ")
                play_y=list(map(int,input("Enter the position at which u want to enter : ").split(" ")))
            played.append(play_y)
            board[play_y[0]][play_y[1]]='O'

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