class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s  = s.split()
        res = s[-1]
        return len(res)