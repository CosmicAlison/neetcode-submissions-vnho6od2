class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        l1 = {}
        l2 = {}
        for i in range(len(s)):
            if l1 and s[i] in l1:
                l1[s[i]] += 1
            else:
                l1[s[i]] = 1

            if l2 and t[i] in l2:
                l2[t[i]] += 1
            else:
                l2[t[i]] = 1

        
        return l1 == l2
