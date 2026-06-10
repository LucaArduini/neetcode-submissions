# exercise: Container With Most Water
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(1)

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        best_area = 0

        while l < r:
            best_area = max(best_area, (r - l) * min(heights[l], heights[r]))

            # LOGICA DEI PUNTATORI (Il cuore dell'algoritmo):
            # Se la barra a sinistra è più corta di quella a destra, 
            # non abbiamo speranza di trovare un'area maggiore tenendo la sinistra 
            # (perché anche spostando destra, l'altezza sarebbe limitata dalla sinistra).
            # Quindi spostiamo il puntatore della barra più corta per cercare un'altezza maggiore.
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return best_area




if __name__ == "__main__":
    sol = Solution()
    
    # Lista dei casi di test: (input, output_atteso)
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # Esempio classico
        ([1, 1], 1),                        # Caso minimo
        ([4, 3, 2, 1, 4], 16),              # Caso con i bordi alti
        ([1, 2, 1], 2),                     # Caso con picco centrale
        ([1,7,2,5,4,7,3,6], 36),            # es Neetcode
        ([1,4,2,7,7,7,3,1,1,4], 32),        # dubbio Luca
    ]
    
    for heights, expected in test_cases:
        result = sol.maxArea(heights)
        status = "PASSED" if result == expected else f"FAILED (expected {expected}, got {result})"
        print(f"Input: {heights} | Risultato: {result} | {status}")