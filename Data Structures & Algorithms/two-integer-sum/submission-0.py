# TITOLO: Ricerca tramite Mappa di Supporto (Two-Pass Hash Map)
# SPIEGAZIONE: Associa ogni numero al suo indice in un dizionario, poi scorre l'array per trovare se il complemento (target - numero) esiste a un indice diverso.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Popola la mappa con valore come chiave e indice come valore
        mappa_indici = {}
        for i, num in enumerate(nums):
            mappa_indici[num] = i
            
        # Scorre l'array per trovare il complemento richiesto
        for i, num in enumerate(nums):
            complemento = target - num
            # Verifica se il complemento è presente nella mappa ed è associato a un indice diverso da i
            if complemento in mappa_indici and mappa_indici[complemento] != i:
                indice_j = mappa_indici[complemento]
                # Ritorna gli indici ordinati (il minore per primo)
                return [i, indice_j] if i < indice_j else [indice_j, i]