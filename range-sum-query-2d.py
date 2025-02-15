class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row_len, col_len = len(matrix), len(matrix[0]) 
        # Making first row and column be 0
        self.prefix_array = [[0] * (col_len + 1) for _ in range(row_len + 1)]
        for row in range(row_len):
            for column in range(col_len):
                prefix_add = matrix[row][column]

                # This is prefix sum for cell above the cell we want to find sum for
                prefix_add = self.prefix_array[row][column + 1]

                # This is prefix sum for cell to the right of cell we want to find sum for
                prefix_add += self.prefix_array[row + 1][column]

                # Removing duplicate addition
                prefix_add -= self.prefix_array[row][column]
                self.prefix_array[row + 1][column + 1] = prefix_add

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Converting indices to fit with prefix sum array indices
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # Sum of the elements at the lower right corner
        ret = self.prefix_array[row2][col2]

        # Sum of elements at the upper right corner
        ret -= self.prefix_array[row2][col1 - 1]

        # Sum of elements at the lower left corner
        ret -= self.prefix_array[row1 - 1][col2]

        # Adding back area that was double subtracted
        ret += self.prefix_array[row1 - 1][col1 - 1]
        return ret


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
