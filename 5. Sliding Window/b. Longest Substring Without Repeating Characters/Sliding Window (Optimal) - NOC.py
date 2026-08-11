class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # mp memorizza l'ultimo indice in cui abbiamo visto ogni carattere
        # Key: carattere, Value: indice (posizione)
        mp = {}
        l = 0  # Puntatore sinistro della finestra
        res = 0 # Risultato: lunghezza massima trovata

        for r in range(len(s)):
            # Se il carattere è già nel dizionario ed è all'interno della finestra attuale
            if s[r] in mp and mp[s[r]] >= l:
                # Spostiamo l direttamente alla posizione successiva all'ultima apparizione
                # del carattere s[r].
                l = mp[s[r]] + 1
            
            # Aggiorniamo (o inseriamo) l'ultimo indice noto del carattere
            mp[s[r]] = r
            
            # Calcoliamo la lunghezza della finestra corrente (r - l + 1)
            # e aggiorniamo il massimo se abbiamo trovato una stringa più lunga
            res = max(res, r - l + 1)
            
        return res