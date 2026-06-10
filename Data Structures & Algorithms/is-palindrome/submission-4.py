# TITOLO: Reverse String
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        # o sfruttando una list comprehension:
        # chars = [c.lower() for c in s if c.isalnum()]

        newStr = ''.join(chars)

        # Confronta la stringa con la sua versione invertita [::-1]
        return newStr == newStr[::-1]