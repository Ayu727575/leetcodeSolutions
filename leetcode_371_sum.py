from typing import List
def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[0 for j in range(c)] for i in range(r)]
        print(res)
        temp = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                temp.append(mat[i][j])
        x = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = temp[x]
                x+=1
        print(x)
        if r==1:
            return res[0]
        return res
mat = [[1,2],[3,4]]
res = matrixReshape(mat,2,2)
print(res)
