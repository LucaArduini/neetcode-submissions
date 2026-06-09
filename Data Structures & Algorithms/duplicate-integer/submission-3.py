# TITOLO: Soluzione tramite Set (Hash Set)
# SPIEGAZIONE: Converte la lista in un set (che elimina i duplicati) e confronta se la lunghezza finale è diversa da quella originale.
# TIME COMPLEXITY: O(N) - Inserire N elementi in un hash set richiede un tempo medio proporzionale a N.
# SPACE COMPLEXITY: O(N) - Nel caso peggiore (nessun duplicato), il set occuperà una quantità di memoria pari all'array originale.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        return len(num_set) != len(nums)