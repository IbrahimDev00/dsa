class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    odd = 0
    for i in arr:
        if i%2 != 0:
            odd += 1
            if odd == 3:
                return(True)
        else:
            odd = 0
    return(False)