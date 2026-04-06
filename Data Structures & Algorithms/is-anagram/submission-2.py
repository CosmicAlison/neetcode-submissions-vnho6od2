class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        l1 = {}
        l2 = {}
        for i in range(len(s)):
            if l1 and s[i] in l1:
                l1[s[i]] = l1[s[i]] + 1
            else:
                l1[s[i]] = 1

            if l2 and t[i] in l2:
                l2[t[i]] = l2[t[i]] + 1
            else:
                l2[t[i]] = 1

        for x in s:
            if x not in l2:
                return False
            if l1[x] != l2[x]:
                return False
        
        return True
