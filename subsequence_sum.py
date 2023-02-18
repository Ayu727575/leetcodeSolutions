def driver(arr,target):
    ans = []
    stack = []
    backtrack(0,target,arr,stack,ans)
    return ans
def backtrack(i,target,arr,stack,ans):
    if i==len(arr):
        if target==0:
            print(stack)
            ans.insert(0,stack)
            print(stack)
            return
        return
    if target>=arr[i]:
        stack.append(arr[i])
        backtrack(i,target-arr[i],arr,stack,ans)
        stack.pop()
    backtrack(i+1,target,arr,stack,ans)
arr = [10,1,2,7,6,1,5]
res = []
x = driver(arr,8)
print(x)
