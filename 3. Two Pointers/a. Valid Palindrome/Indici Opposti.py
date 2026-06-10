# TITOLO: Verifica Palindromo tramite Indici Opposti
# SPIEGAZIONE: Filtra la stringa mantenendo solo i caratteri alfanumerici in formato minuscolo, poi confronta i caratteri speculari dall'esterno verso l'interno usando indici positivi e negativi.
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Rimuove spazi e punteggiatura e converte in minuscolo
        stringa_pulita = "".join(c.lower() for c in s if c.isalnum())
        
        # Controlla la simmetria fermandosi a metà
        lunghezza = len(stringa_pulita)
        for i in range(lunghezza // 2):
            # i parte dall'inizio, -(i + 1) parte dalla fine all'indietro
            if stringa_pulita[i] != stringa_pulita[-(i + 1)]:
                return False
                
        return True