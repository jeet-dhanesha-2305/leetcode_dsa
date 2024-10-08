class Solution:
    def minSwaps(self, s: str) -> int:
        extraClose  = 0
        maxExtraClose = float("-inf")

        for br in s:
            extraClose += 1 if br == "]" else -1
            maxExtraClose = max(maxExtraClose, extraClose)
        
        return (maxExtraClose+1)//2
        