class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return matrix

        n_rows, n_cols = len(matrix), len(matrix[0])
        degree, output = 0, []

        while degree < (min(n_rows, n_cols) + 1) // 2:
            output += self._spiralOrder(matrix, degree, n_rows ,n_cols)
            degree += 1
        return output

    def _spiralOrder(self, matrix, degree, n_rows ,n_cols):
        output = []        
        output += matrix[degree][degree: n_cols - degree]

        for i in range(degree + 1, n_rows - degree - 1, 1):
            output.append(matrix[i][n_cols - degree - 1])
        
        if degree < n_rows // 2:
            for j in range(n_cols - degree - 1, degree - 1, -1):
                output.append(matrix[n_rows - degree - 1][j])
        
        if degree < n_cols // 2:
            for i in range(n_rows - degree - 2, degree, -1):
                output.append(matrix[i][degree])
        
        return output

