from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s  = Counter(s)
        dict_t  = Counter(t)

        if dict_t == dict_s:
            return True
        return False
# without usinf the counter library
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
