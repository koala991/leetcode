class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n_rows = len(matrix) 
        n_cols = 0 if n_rows == 0 else len(matrix[0])
        i, j = 0, n_cols - 1
        output = False
        while i <= n_rows - 1 and j >= 0:
            if matrix[i][j] == target:
                output = True
                break
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
        return output