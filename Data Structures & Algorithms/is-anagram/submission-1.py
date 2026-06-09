# TITOLO: Soluzione tramite Ordinamento (Sorting)
# SPIEGAZIONE: Verifica che le stringhe abbiano la stessa lunghezza e confronta le loro versioni ordinate alfabeticamente.
# TIME COMPLEXITY: O(N log N) - L'operazione di ordinamento (sorting) è l'operazione più costosa e domina la complessità temporale.
# SPACE COMPLEXITY: O(N) - La funzione sorted() crea una nuova lista di N caratteri in memoria.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)