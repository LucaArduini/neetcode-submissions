# TITOLO: Soluzione tramite Set (Hash Set)
# SPIEGAZIONE: Converte la lista in un set (che elimina i duplicati) e confronta se la lunghezza finale è diversa da quella originale.
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Crea un set dagli elementi della lista
        num_set = set(nums)
        # Se la lunghezza del set è inferiore a quella della lista,
        # significa che c'erano dei duplicati che sono stati rimossi.
        return len(num_set) != len(nums)