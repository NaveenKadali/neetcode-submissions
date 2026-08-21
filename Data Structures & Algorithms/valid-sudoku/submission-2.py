class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows_hash_map = {i: set() for i in range(9)}
        cols_hash_map = {i: set() for i in range(9)}
        grids_hash_map = defaultdict(set)

        for row in range(9):
            for col in range(9):
                element = board[row][col]
                
                grid = (row+3)//3 + col//3

                if element.isdigit():

                    if element in rows_hash_map[row]:
                        return False
                    else:
                        rows_hash_map[row].add(element)
                        
                    if element in cols_hash_map[col]:
                        return False
                    else:
                        cols_hash_map[col].add(element)
                    
                    if element in grids_hash_map[(row//3, col//3)]:
                        return False
                    else:
                        grids_hash_map[(row//3, col//3)].add(element)

        return True                    