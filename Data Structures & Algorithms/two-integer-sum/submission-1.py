# TITOLO: Ricerca tramite Mappa a Singolo Passaggio (One-Pass Hash Map)
# SPIEGAZIONE: Scorre l'array una sola volta, cercando il complemento nella mappa e inserendo il numero corrente se non viene trovato.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappa_indici = {}
        
        for i, num in enumerate(nums):
            complemento = target - num
            
            # Se il complemento è già nella mappa, abbiamo trovato la coppia
            if complemento in mappa_indici:
                # L'indice memorizzato nella mappa è necessariamente più piccolo di i
                return [mappa_indici[complemento], i]
            
            # Altrimenti, memorizziamo il numero corrente e il suo indice
            mappa_indici[num] = i