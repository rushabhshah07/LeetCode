class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        n = len(matrix)

        ans = []

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    ans.append((i,j))

        for R,C in ans:
            matrix[R] = [0]*m

            for i in range(n):
                matrix[i][C] = 0

        