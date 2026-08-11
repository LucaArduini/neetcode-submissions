from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)
            #print("l:", l, "r:", r, "-> m:", m)

            if nums[m] < target:
                l = m +1
            elif nums[m] > target:
                r = m -1
            else:
                return m
        
        return -1



# Esecuzione del test
nums=[-1,0,2,4,6,8]
target=3

sol = Solution()
risultato = sol.search(nums, target)

if risultato == -2:
    print("Il test è stato interrotto per evitare il crash.")
else:
    print("Risultato finale:", risultato)