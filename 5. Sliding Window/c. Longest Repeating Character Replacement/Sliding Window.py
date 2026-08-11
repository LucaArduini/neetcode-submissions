class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                # (r - l + 1) è la lunghezza totale della finestra attuale.
                # (r - l + 1) - count ci dà il numero di caratteri "diversi" da 'c' nella finestra.  
                # Se questo numero > k, non possiamo più fare sostituzioni.
                while (r - l + 1) - count > k:
                    # Dobbiamo restringere la finestra da sinistra
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        
        return res