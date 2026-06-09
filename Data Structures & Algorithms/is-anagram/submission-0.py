# TITOLO: Soluzione tramite Ordinamento (Sorting)
# SPIEGAZIONE: Verifica che le stringhe abbiano la stessa lunghezza e confronta le loro versioni ordinate alfabeticamente.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)