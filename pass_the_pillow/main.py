class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycleLen = 2*(n-1)
        time = time%cycleLen
        if time <n:
            return time+1
        else:
            return 2*n - time - 1