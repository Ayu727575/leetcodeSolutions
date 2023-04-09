def knapsack_memo(ind,wt,val, w, dp):
    if ind==0:
        if wt[ind]<=w:
            return val[ind]
        return 0
    if dp[ind][w]!=-1:
        return dp[ind][w]
    not_take = 0 + knapsack_memo(ind-1,wt,val,w,dp)
    take = 0
    if wt[ind]<=w:
        take = val[ind]+knapsack_memo(ind-1,wt,val,w-wt[ind],dp)
    dp[ind][w] = max(not_take,take)
    return dp[ind][w]
def knapsack(wt, val, n, w):
    dp = [[-1 for _ in range(w+1)] for _ in range(n)]
    return knapsack_memo(n-1,wt,val,w,dp)

if __name__ == "__main__":
    wt = [1,2,4,5]
    val = [5,4,8,6]
    w = 5
    n = len(wt)
    print("The Maximum value of items, thief can steal is ",knapsack(wt,val,n,w))
