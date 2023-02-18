def fabbo(n,dp_array):
    if n<=1:
        return n
    if dp_arr[n]!=-1:
        return dp_arr[n]
    dp_arr[n] = fabbo(n-1,dp_arr)+fabbo(n-2,dp_arr)
    return dp_array[n]
def fabbo_2(n):
    prev,prev2 = 1,0
    for i in range(2,n+1):
        curr = prev+prev2
        prev2 = prev
        prev = curr
    return prev
n = int(input())
dp_arr = [-1 for i in range(n+1)]
#print(fabbo(n,dp_arr))
print(fabbo_2(n))
