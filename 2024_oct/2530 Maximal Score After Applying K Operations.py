class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        arr = []
        for elem in nums:
            heappush(arr, -1*elem)
        
        res = 0
        while k > 0:
            maxElem = -1*heappop(arr)
            res += maxElem
            newElem = ceil(maxElem/3)
            heappush(arr,-1*newElem)
            k -= 1

        return res