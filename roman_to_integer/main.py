class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and dic[i] < dic[s+1]:
                sum += dic[s[i + 1]] - dic[s[i]]
                i += 2
            else:
                sum += dic[s[i]]
                i += 1
        return sum