class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        res = 0

        for i in range(len(s)):
            chars.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in chars:
                    chars.add(s[j])
                else:
                    break
            
            res = max(res, len(chars))
            chars.clear()

        return res