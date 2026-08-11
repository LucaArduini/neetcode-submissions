from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            i = l + ((r - l) // 2)
            #print("l:", l, "r:", r, "\ti:", i)
            
            if matrix[i//COLS][i%COLS] < target:
                l = i + 1
            elif matrix[i//COLS][i%COLS] > target:
                r = i - 1
            else:
                return True

        return False



# Esecuzione del test
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=13

sol = Solution()
risultato = sol.searchMatrix(matrix, target)

if risultato == -2:
    print("Il test è stato interrotto per evitare il crash.")
else:
    print("Risultato finale:", risultato)