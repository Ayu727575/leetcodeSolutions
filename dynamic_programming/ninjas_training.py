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
# arr = [1,2,3,1]
# output = 4
r,c = map(int,input().strip().split())
arr = list(list(map(int, input().strip().split())) for i in range(r))
obj = Solution()
ans = obj.ninja(arr,r,c)
ans2 = obj.ninja_dp(arr,r,c)
print(ans)
print(ans2)