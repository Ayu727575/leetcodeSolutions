def subsequence(i,arr,arr2,summ):
    if i==len(arr2):
        if summ==11:
            print(arr)
            return True
        return False
    arr.append(arr2[i])
    summ+=arr2[i]
    flag = subsequence(i+1,arr,arr2,summ)
    if flag:
        return True
    arr.pop()
    summ-=arr2[i]
    flag = subsequence(i+1,arr,arr2,summ)
    if flag:
        return True
    return False


arr2 = [2,1,4,3,1]
print(subsequence(0,[],arr2,0))

