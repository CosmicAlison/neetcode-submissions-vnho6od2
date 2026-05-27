class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        strings = defaultdict()
        
        for s in strs:
            sortedS = "".join(sorted(s))
            if strings and sortedS in strings:
                strings[sortedS].append(s)
            else:
                strings[sortedS] = [s]

        return list(strings.values())
