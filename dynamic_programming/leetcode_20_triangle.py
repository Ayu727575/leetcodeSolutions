import sys
def Solution(triangle):
    def min_cost_fun(i,j):
        if i==len(triangle)-1:
            return triangle[i][j]
        # for k in range(len(triangle[i])):
        #     cur_cost = triangle[i][k]+min_cost_fun(i+1,k)
        #     min_cost = min(min_cost,cur_cost)
        bottom_left = triangle[i][j]+min_cost_fun(i+1,j)
        bottom_right =triangle[i][j]+min_cost_fun(i+1,j+1)
        return min(bottom_left,bottom_right)
    return min_cost_fun(0,0)
def Solution_dp(triangle):
    dp = [[-1 for i in range(len(triangle))] for j in range(len(triangle))]
    def min_cost_fun(i,j):
        if i==len(triangle)-1:
            return triangle[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        # for k in range(len(triangle[i])):
        #     cur_cost = triangle[i][k]+min_cost_fun(i+1,k)
        #     min_cost = min(min_cost,cur_cost)
        bottom_left = triangle[i][j]+min_cost_fun(i+1,j)
        bottom_right =triangle[i][j]+min_cost_fun(i+1,j+1)
        dp[i][j]=min(bottom_left,bottom_right)
        return dp[i][j]
    return min_cost_fun(0,0)
def Solution_dp_tabulation(triangle):
    n = len(triangle)
    dp = [[-1] * n for _ in range(n)]
    dp[n - 1] = triangle[n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            lower_left = triangle[i][j] + dp[i + 1][j]
            lower_right = triangle[i][j] + dp[i + 1][j + 1]
            dp[i][j] = min(lower_left, lower_right)
    return dp[0][0]
    

if __name__ == "__main__":
    r = int(input())
    arr = list(list(map(int, input().strip().split())) for i in range(r))
    print(Solution(arr))