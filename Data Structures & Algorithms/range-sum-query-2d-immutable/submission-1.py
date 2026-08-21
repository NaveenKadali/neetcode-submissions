class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.matrix = matrix
        self.no_of_rows = len(matrix)
        self.no_of_cols = len(matrix[0])

        self.sum_matrix = [
            [0 for col in range(self.no_of_cols)
            ] for row in range(self.no_of_rows)]
            
        self.fill_up_sum_matrix()

    def fill_up_sum_matrix(self):

        rows = len(self.matrix)
        cols = len(self.matrix[0])
                
        for row in range(0, rows):
            row_sum = 0
            for col in range(0, cols):
                row_sum += self.matrix[row][col]
                self.sum_matrix[row][col] = row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        sum_ = 0
        for row in range(row1, row2+1):

            if col1 == 0:
                sum_ += self.sum_matrix[row][col2]
            else:
                sum_ += self.sum_matrix[row][col2] - self.sum_matrix[row][col1-1]
        
        return sum_
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)