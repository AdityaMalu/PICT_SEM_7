
def is_safe(board,row,col,n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    i,j = row,col
    while i >=0 and j >=0:
        if board[i][j] == 1:
            return False
        i-=1
        j-=1

    i,j = row,col
    while i>=0 and j < n:
        if board[i][j] == 1:
            return False
        i-=1
        j+=1

    return True

def solve(board,row,n):
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col] = 1

            if solve(board,row+1,n):
                return True
            
            board[row][col] = 0
    return False

def print_(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()
    print()


N = int(input("Enter the number of queens (N): "))
board = [[0] * N for _ in range(N)]

    # Try placing the first queen in every column of the first row
solution_found = False
for col in range(N):
        board[0][col] = 1  # Place the first queen
        if solve(board, 1, N):  # Start solving for the rest of the queens
            solution_found = True
            break
        board[0][col] = 0  # Backtrack if no solution found

if solution_found:
        print("Solution:")
        print_(board, N)
else:
        print("No solution exists.")