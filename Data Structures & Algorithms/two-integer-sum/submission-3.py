# TITOLO: Ricerca tramite Mappa a Singolo Passaggio (One-Pass Hash Map)
# SPIEGAZIONE: Scorre l'array una sola volta, cercando il complemento nella mappa e inserendo il numero corrente se non viene trovato.
# TIME COMPLEXITY: O(N) - Scorre l'array una volta sola. L'inserimento e la ricerca nella mappa costano mediamente O(1).
# SPACE COMPLEXITY: O(N) - Nel caso peggiore, memorizza quasi tutti gli elementi nel dizionario prima di trovare la coppia.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappa_indici = {}
        
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in mappa_indici:
                return [mappa_indici[complemento], i]
            mappa_indici[num] = i