class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        
        rightMaxVal = [0]*n
        currMax = nums[n-1]

        for i in range(n-1, -1, -1):
            if nums[i] > currMax:
                currMax = nums[i]
        
            rightMaxVal[i] = currMax
        
        res = 0
        l = 0
        for r in range(n):
            while nums[l] > rightMaxVal[r]:
                l += 1
            res = max(res, r-l)
        
        return res