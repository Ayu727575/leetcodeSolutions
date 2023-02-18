class Solution:
    def __init__(self) -> None:
        pass
    def permute(self,nums):
        def all_permutation(ind,arr,ans):
            if ind==len(arr):
                ds = []
                for i in range(len(arr)):
                    ds.append(arr[i])
                ans.append(list(ds))
                return
            for i in range(ind, len(arr)):
                arr[i],arr[ind] = arr[ind], arr[i]
                all_permutation(ind+1,arr,ans)
                arr[i],arr[ind] = arr[ind], arr[i]
        ans = []
        all_permutation(0,nums,ans)
        return ans
arr = list(map(int, input().strip().split()))
obj = Solution()
ans = obj.permute(arr)
print(ans)
    