# TITOLO: Verifica Palindromo tramite Indici Opposti
# SPIEGAZIONE: Filtra la stringa mantenendo solo i caratteri alfanumerici in formato minuscolo, 
# poi confronta i caratteri speculari dall'esterno verso l'interno usando indici positivi e negativi.
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filtra la stringa tenendo solo lettere e numeri, convertendo tutto in minuscolo
        stringa_pulita = "".join(carattere.lower() for carattere in s if carattere.isalnum())
        
        lunghezza = len(stringa_pulita)
        # Scorriamo fino a metà della stringa pulita
        for i in range(lunghezza // 2):
            # i parte da 0 (inizio), -(i + 1) parte da -1 (fine)
            if stringa_pulita[i] != stringa_pulita[-(i + 1)]:
                return False
                
        return True