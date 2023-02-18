def subsequence(i,arr2,summ,res):
    if i==len(arr2):
        res.append(summ)
        return
    subsequence(i+1,arr2,summ+arr2[i],res)
    subsequence(i+1,arr2,summ,res)


arr2 = [3,1,2]
res =[]
subsequence(0,arr2,0,res)
print(res)

