class Solution:

    def __init__(self) -> None:

        self.exception = Exception("Invalid")

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_element(element, seen_digits):
            
            print(element, seen_digits)
            if element.isdigit():

                if element in seen_digits:
                    raise self.exception
                else:
                    seen_digits.append(element)
                    return seen_digits
            else:
                return seen_digits

        def check_row_elements(row):
            
            seen_digits = []
            for col in range(0, 9):
                row_element = board[row][col]
                seen_digits = check_element(row_element, seen_digits)

        def check_column_elements(col):
            
            seen_digits = []
            for row in range(0, 9):
                col_element = board[row][col]
                seen_digits = check_element(col_element, seen_digits)
        
        def check_grid(i, j):

            print("grid:", i, j)
            
            seen_digits = []
            for row in range(i, i+3):
                for col in range(j, j+3):

                    grid_element = board[row][col]
                    print(i, j, grid_element, seen_digits)
                    seen_digits = check_element(grid_element, seen_digits)


        
        def validate_grids():
            
            for i in range(0, 9, 3):
                
                for j in range(0, 9, 3):

                    check_grid(i, j)

        def validate_rows_and_columns():

            for i in range(9):
                check_column_elements(i)
                check_row_elements(i)

        def validate_diagonals():

            top_left_to_bottom_right_seen_elements = []
            top_right_to_bottom_left_seen_elements = []
            
            for i in range(0, 9):
                for j in range(0, 9):
                    if i==j:
                        tl_to_br_element = board[i][i]
                        tr_to_bl_element = board[i][8-i]

                        top_left_to_bottom_right_seen_elements = check_element(tl_to_br_element, top_left_to_bottom_right_seen_elements)
                        top_right_to_bottom_left_seen_elements = check_element(tr_to_bl_element, top_right_to_bottom_left_seen_elements)  
        
        def validate_sudoko():

            validate_grids()
            validate_rows_and_columns()
            #validate_diagonals()
            
        try:
            validate_sudoko()
            return True
        except Exception as e:
            return False