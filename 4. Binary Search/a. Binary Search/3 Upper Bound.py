# ● Cosa cerca: Il primo elemento che "esce" dal range del target.
# ● Uso ideale: Quando vuoi trovare la fine di un blocco di duplicati, o vuoi sapere quanti elementi sono più piccoli di un valore.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Intervallo di ricerca [l, r)
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)

            if nums[m] <= target:
                l = m +1
            else:
                #elif nums[m] > target:
                r = m
        
        # NB: nel while non cerco target, ma "il primo valore più grande di target"
    
        # Fine del ciclo:
        # l (e r) puntano al primo elemento strettamente maggiore di target.
        # Quindi l - 1 è l'ultimo elemento <= target.
        # Se quell'elemento è proprio target, abbiamo trovato
        # l'ultima occorrenza di target.

        return l - 1 if (l and nums[l - 1] == target) else -1



# Esecuzione del test
# NB: se l'array contiene duplicati, la funzione 
# restituisce l'indice dell'ultima occorrenza di target.
nums = [1, 2, 4, 4, 4, 7]
target = 4

sol = Solution()
risultato = sol.search(nums, target)
print("Risultato finale:", risultato)

