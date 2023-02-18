class Solution:
    def __init__(self) -> None:
        pass
    def permute(self,nums):
        def all_permutation(arr,ds,ans,freq):
            if len(ds)==len(arr):
                ans.append(list(ds))
                return
            for i in range(len(arr)):
                if not freq[i]:
                    freq[i] = True
                    ds.append(arr[i])
                    all_permutation(arr,ds,ans,freq)
                    ds.pop()
                    freq[i] = False
        ans = []
        freq = [False for i in range(len(nums))]
        all_permutation(nums,[],ans,freq)
        return ans
arr = list(map(int, input().strip().split()))
obj = Solution()
ans = obj.permute(arr)
print(ans)
    