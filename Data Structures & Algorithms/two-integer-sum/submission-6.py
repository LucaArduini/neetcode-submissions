# TITOLO: Ricerca tramite Mappa a Singolo Passaggio (One-Pass Hash Map)
# SPIEGAZIONE: Scorre l'array una sola volta, cercando il complemento nella mappa e inserendo il numero corrente se non viene trovato.
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappa_indici = {}
        
        for i, num in enumerate(nums):
            complemento = target - num
            
            # Se il complemento è già stato visitato, abbiamo trovato la coppia
            if complemento in mappa_indici:
                return [mappa_indici[complemento], i]
                
            # Altrimenti, aggiunge il numero corrente alla mappa per le prossime iterazioni
            mappa_indici[num] = i