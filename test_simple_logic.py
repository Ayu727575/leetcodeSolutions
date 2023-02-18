def solve(col, board, ans, left_row, upper_digonal,lower_digonal,n):
            if col==n:
                ans.append(["".join(i) for i in board])
                return
            for row in range(n):
                if left_row[row]==0 and lower_digonal[row+col]==0 and upper_digonal[n-1+col-row]==0:
                    board[row][col] = "Q"
                    left_row[row] = 1
                    lower_digonal[row+col]=1
                    upper_digonal[n-1+col-row]=1
                    solve(col+1,board,ans,left_row,upper_digonal,lower_digonal,n)
                    board[row][col] = "."
                    left_row[row]=0
                    lower_digonal[row+col]=0
                    upper_digonal[n-1+col-row]=0

n=4
ans = []
board = [["."]*n for i in range(n)]
left_row = [0 for i in range(n)]
upper_digonal = [0 for i in range(2*n-1)]
lower_digonal = [0 for i in range(2*n-1)]
solve(0, board, ans, left_row, upper_digonal, lower_digonal, n)
print(ans)
