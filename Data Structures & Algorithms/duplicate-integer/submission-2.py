from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        # Il primo ciclo seleziona l'elemento corrente
        for i in range(n):
            # Il secondo ciclo confronta l'elemento con i successivi
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        # Se i cicli terminano senza trovare uguaglianze, non ci sono duplicati
        return False