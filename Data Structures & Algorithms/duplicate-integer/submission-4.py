# TITOLO: Soluzione tramite Due Cicli Annidati (Brute Force)
# SPIEGAZIONE: Confronta ogni elemento dell'array con tutti gli elementi successivi per cercare una corrispondenza.
# TIME COMPLEXITY: O(N^2) - Per ogni elemento, scorre il resto dell'array.
# SPACE COMPLEXITY: O(1) - Non utilizza memoria aggiuntiva che cresce con la dimensione dell'input.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False