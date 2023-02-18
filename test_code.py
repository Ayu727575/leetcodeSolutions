class Solution:
    def __init__(self) -> None:
        pass

    def findCombinations(self,ind,arr,target,ans,ds):
        if target == 0:
            ans.append(ds)
            return
        for i in range(ind, len(arr)):
            if i>ind and arr[i]==arr[i-1]: continue
            if arr[i]>target: break
            ds.append(arr[i])
            self.findCombinations(i+1,arr,target-arr[i],ans,ds)
            ds.pop()
    def combinationSum2(self,candidates, target):
        ans = []
        candidates.sort()
        self.findCombinations(0,candidates,target,ans,[])
        return ans
can = [1,1,1,2,2]
obj = Solution()
result = obj.combinationSum2(can,4)
print(result)
        