def subsequence(ind,arr2,ds,res):
    res.append(list(ds))
    for i in range(ind,len(arr2)):
        if i!=ind and arr2[i]==arr2[i-1]: continue
        ds.append(arr2[i])
        subsequence(i+1,arr2,ds,res)
        ds.pop()


arr2 = [1,2,2]
arr2.sort()
res =[]
subsequence(0,arr2,[],res)
print(res)

