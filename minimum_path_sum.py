from typing import List
import sys
def min_path_sum_tab(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                dp[i][j] = matrix[i][j]
            else:
                up = matrix[i][j]
                if i>0:
                    up+=dp[i-1][j]
                else:
                    up+=sys.maxsize
                left = matrix[i][j]
                if j>0:
                    left+=dp[i][j-1]
                else:
                    left+=sys.maxsize
                
                dp[i][j] = min(up,left)
    return dp[n-1][m-1]
# using memoization
def min_path_sum(matrix,r,c):
    def back_track(matrix,i,j,dp):
        if i==0 and j==0:
            return matrix[0][0]
        if i<0 or j<0:
            return sys.maxsize
        if dp[i][j]!=-1:
            return dp[i][j]
        up = matrix[i][j] + back_track(matrix,i-1,j,dp)
        left = matrix[i][j] + back_track(matrix,i,j-1,dp)
        dp[i][j] = min(up,left)
        return dp[i][j]
    dp = [[-1 for j in range(c)] for i in range(r)]
    return back_track(matrix,r-1,c-1,dp)

def min_path_sum_tab_opt(matrix):
    n = len(matrix)
    m = len(matrix[0])
    prev = [0 for j in range(m)]
    for i in range(n):
        curr = [0]*m
        for j in range(m):
            if i==0 and j==0:
                curr[j] = matrix[i][j]
            else:
                up = matrix[i][j]
                if i>0:
                    up+=prev[j]
                else:
                    up+=sys.maxsize
                left = matrix[i][j]
                if j>0:
                    left+=curr[j-1]
                else:
                    left+=sys.maxsize
                
                curr[j] = min(up,left)
        prev=curr
    return prev[m-1]
if __name__ == "__main__":
    r, c = map(int, input().strip().split())
    arr = list(list(map(int, input().strip().split())) for i in range(r))
    ans = min_path_sum(arr, r, c)
    ans2 = min_path_sum_tab(arr)
    ans3 = min_path_sum_tab_opt(arr)
    print(ans)
    print(ans2)
    print(ans3)
