class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s: dict[str, num] = {}
        counts_t: dict[str, num] = {}
        
        for char in s:
            if char in counts_s.keys():
                counts_s[char] += 1
            else:
                counts_s[char] = 1
        
        for char in t:
            if char in counts_t.keys():
                counts_t[char] += 1
            else:
                counts_t[char] = 1

        return counts_s == counts_t