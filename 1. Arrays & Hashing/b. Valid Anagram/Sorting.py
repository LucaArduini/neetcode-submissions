# TITOLO: Soluzione tramite Ordinamento (Sorting)
# SPIEGAZIONE: Verifica che le stringhe abbiano la stessa lunghezza e confronta le loro versioni ordinate alfabeticamente.
# TIME COMPLEXITY: O(N log N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Due anagrammi devono necessariamente avere la stessa lunghezza
        if len(s) != len(t):
            return False
        
        # Ordina alfabeticamente e confronta
        return sorted(s) == sorted(t)