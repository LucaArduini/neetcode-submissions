# La soluzione One Pass è l'evoluzione "elegante" del tuo algoritmo. Invece di trovare 
# prima il pivot e poi cercare, la One Pass fonde le due logiche in un unico ciclo while.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # Identifichiamo quale metà è ordinata
            if nums[l] <= nums[mid]:
                # Metà sinistra ordinata
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # Metà destra ordinata
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1