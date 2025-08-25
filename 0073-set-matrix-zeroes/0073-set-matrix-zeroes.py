class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cp = copy.deepcopy(matrix)


        for i in range(len(cp)):
            for j in range(len(cp[0])):
                if cp[i][j] == 0:
                    for k in range(len(cp)):
                        matrix[k][j] = 0
                    for l in range(len(cp[0])):
                        matrix[i][l] = 0
        
                            
        