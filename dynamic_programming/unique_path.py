from typing import List
class Solution:
    # plain recursion
    def unique_path(self,r,c)->int:
        def dfs(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            return dfs(i-1,j)+dfs(i,j-1)
        return dfs(r-1,c-1)
    # recursion+DP
    def unique_path_dp(self,r,c)->int:
        def dfs(i,j,dp):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j] = dfs(i-1,j,dp)+dfs(i,j-1,dp)
            return dp[i][j]
        dp = [[-1 for i in range(c+1)] for i in range(r)]
        return dfs(r-1,c-1,dp)
    # tabulation+DP
    def unique_path_dp_tabu(self,r,c)->int:
        dp = [[0 for i in range(c+1)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if i==0 and j==0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[r-1][c-1]
    def unique_path_dp_tabu_opt(self,r,c)->int:
        prev = [0]*c
        for i in range(r):
            curr = [0]*c
            for j in range(c):
                if i==0 and j==0:
                    curr[j] = 1
                    continue
                curr[j] = curr[j-1]+prev[j]
            prev = curr
        return prev[j]


        
        
# arr = [1,2,3,1]
# output = 4
# arr = list(list(map(int, input().strip().split())) for i in range(r))
r,c = map(int,input().strip().split())
obj = Solution()
ans = obj.unique_path(r,c)
ans2 = obj.unique_path_dp(r,c)
ans3 = obj.unique_path_dp_tabu(r,c)
ans4 = obj.unique_path_dp_tabu_opt(r,c)
print(ans)
print(ans2)
print(ans3)
print(ans4)