class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Sposta il puntatore sinistro fino a trovare un carattere alfanumerico
            while left < right and not s[left].isalnum():
                left += 1
            # Sposta il puntatore destro fino a trovare un carattere alfanumerico
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Confronta i caratteri in minuscolo
            if s[left].lower() != s[right].lower():
                return False
            
            # Muovi entrambi i puntatori verso il centro
            left += 1
            right -= 1
        
        return True