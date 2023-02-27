from typing import List
class Solution:
    # plain recursion
    def ninja(self, nums: List[int],r,c)->int:
        def t_points(ind,last):
            if ind==0:
                maxi = 0
                for i in range(c):
                    if i!=last:
                        maxi = max(maxi,nums[0][i])
                return maxi
            maxi = 0
            for i in range(c):
                if i!=last:
                    points = nums[ind][i]+t_points(ind-1,i)
                    maxi = max(maxi,points)
            return maxi
        return t_points(r-1,c)
    # recursion+DP
    def ninja_dp(self, nums: List[int],r,c)->int:
        def t_points(ind,last,dp):
            if ind==0:
                maxi = 0
                for i in range(c):
                    if i!=last:
                        maxi = max(maxi,nums[0][i])
                return maxi
            if dp[ind][last]!=-1:
                return dp[ind][last]
            maxi = 0
            for i in range(c):
                if i!=last:
                    points = nums[ind][i]+t_points(ind-1,i,dp)
                    maxi = max(maxi,points)
            dp[ind][last] = maxi
            return dp[ind][last]
        dp = [[-1 for i in range(c+1)] for i in range(r)]
        return t_points(r-1,c,dp)
    # tabulation+DP
    def ninja_dp_tabu(self, nums: List[int],r,c)->int:
        dp = [[0 for _ in range(c+1)] for _ in range(r)]
        dp[0][0] = max(nums[0][1],nums[0][2])
        dp[0][1] = max(nums[0][0],nums[0][2])
        dp[0][2] = max(nums[0][0],nums[0][1])
        dp[0][3] = max(nums[0][1],max(nums[0][1],nums[0][2]))
        for ind in range(1, r):
            for last in range(c+1):
                dp[ind][last]=0
                for j in range(c):
                    if j!=last:
                        point = nums[ind][j]+dp[ind-1][j]
                        dp[ind][last] = max(point,dp[ind][last])
        return dp[r-1][c]
        
# arr = [1,2,3,1]
# output = 4
r,c = map(int,input().strip().split())
arr = list(list(map(int, input().strip().split())) for i in range(r))
obj = Solution()
ans = obj.ninja(arr,r,c)
ans2 = obj.ninja_dp(arr,r,c)
ans3 = obj.ninja_dp_tabu(arr,r,c)
print(ans)
print(ans2)
print(ans3)