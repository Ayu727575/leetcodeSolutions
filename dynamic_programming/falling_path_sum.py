import sys


class Solution:
    def __init__(self) -> None:
        pass

    def falling_path(self,l,m,arr):
        max_sum = 0
        def dfs(r,c,arr):
            if c<0 or c>=m:
                return -1e9
            if r==0:
                return arr[0][c]
            left_up = arr[r][c] + dfs(r-1,c-1,arr)
            up = arr[r][c] + dfs(r-1,c,arr)
            right_up = arr[r][c] + dfs(r-1,c+1,arr)
            return max(left_up, up, right_up)
        for i in range(c):
            max_sum = max(max_sum,dfs(l-1,i,arr))
        return max_sum
    
    def falling_path_dp(self,l,m,arr):
        max_sum = 0
        def dfs(r,c,arr,dp):
            if c<0 or c>=m:
                return -1e9
            if r==0:
                return arr[0][c]
            if dp[r][c] != -1:
                return dp[r][c]
            left_up = arr[r][c] + dfs(r-1,c-1,arr,dp)
            up = arr[r][c] + dfs(r-1,c,arr,dp)
            right_up = arr[r][c] + dfs(r-1,c+1,arr,dp)
            dp[r][c] = max(left_up, up, right_up)
            return dp[r][c]
        dp = [[-1 for _ in range(m)] for _ in range(l)]
        for i in range(c):
            max_sum = max(max_sum,dfs(l-1,i,arr,dp))
        return max_sum
    
    def falling_path_dp_tabu(self,l,m,arr):
        dp = [[0 for _ in range(m)] for _ in range(l)]
        maxi = -1e9
        for i in range(m):
            dp[0][i] = arr[0][i]
        for i in range(1,l):
            for j in range(m):
                up = arr[i][j]+dp[i-1][j]
                up_left = arr[i][j]
                if j-1>=0: up_left+=dp[i-1][j-1]
                else: up_left = -1e9
                up_right = arr[i][j]
                if j+1<m: up_right+=dp[i-1][j+1]
                else: up_right = -1e9
                dp[i][j] = max(up,up_left,up_right)
        for i in range(m):
            maxi = max(maxi,dp[l-1][i])      
        return maxi
    
    def falling_path_dp_tabu_opt(self,l,m,arr):
        prev = [0 for _ in range(m)]
        curr = [0]*m
        maxi = -sys.maxsize
        for i in range(m):
            prev[i] = arr[0][i]
        for i in range(1,l):
            for j in range(m):
                up = arr[i][j]+prev[j]
                up_left = arr[i][j]
                if j-1>=0: up_left+=prev[j-1]
                else: up_left = -1e9
                up_right = arr[i][j]
                if j+1<m: up_right+=prev[j+1]
                else: up_right = -1e9
                curr[j] = max(up,up_left,up_right)
            prev = curr[:]
        for i in range(m):
            maxi = max(maxi,prev[i])      
        return maxi
#[[2,1,3],[6,5,4],[7,8,9]]
r,c = map(int, input().strip().split())
arr = list(list(map(int, input().strip().split())) for _ in range(r))
obj = Solution()
ans = obj.falling_path(r,c,arr)
ans2 = obj.falling_path_dp(r,c,arr)
ans3 = obj.falling_path_dp_tabu(r,c,arr)
ans4 = obj.falling_path_dp_tabu_opt(r,c,arr)
print(ans)
print(ans2)
print(ans3)
print(ans4)