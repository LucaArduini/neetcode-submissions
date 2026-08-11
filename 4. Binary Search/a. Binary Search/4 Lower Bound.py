# ● Cosa cerca: La prima occorrenza del target (in caso di duplicati).
# ● Uso ideale: Quando vuoi trovare l'inizio di un blocco di duplicati.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Intervallo di ricerca [l, r)
        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2
            print("l:", l, "r:", r, "-> m:", m)
        
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m+1

        return l if (l < len(nums) and nums[l] == target) else -1



# Esecuzione del test
nums=[-1,0,2,4,6,8]
target=-1

sol = Solution()
risultato = sol.search(nums, target)

if risultato == -2:
    print("Il test è stato interrotto per evitare il crash.")
else:
    print("Risultato finale:", risultato)