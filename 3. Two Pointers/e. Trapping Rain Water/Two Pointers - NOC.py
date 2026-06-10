class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            # Muoviamo il puntatore che ha l'altezza minore
            if leftMax < rightMax:
                l += 1
                # Aggiorniamo il massimo a sinistra
                leftMax = max(leftMax, height[l])
                # L'acqua che si accumula è la differenza tra il massimo a sx e l'altezza corrente
                res += max(0, leftMax - height[l])
            else:
                r -= 1
                # Aggiorniamo il massimo a destra
                rightMax = max(rightMax, height[r])
                # L'acqua che si accumula è la differenza tra il massimo a dx e l'altezza corrente
                res += max(0, rightMax - height[r])
                
        return res