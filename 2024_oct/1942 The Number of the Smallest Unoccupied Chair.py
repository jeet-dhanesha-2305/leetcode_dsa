class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        pTim = [(t[0],t[1],i) for i, t in enumerate(times) ]
        pTim.sort()

        usedChair = []
        availChair = [i for i in range(len(times))]

        for a, l, i in pTim:

            while usedChair and usedChair[0][0] <= a:
                leave, chair = heapq.heappop(usedChair)
                heapq.heappush(availChair, chair)

            chair = heapq.heappop(availChair)
            heapq.heappush(usedChair, (l, chair))
        
            if i == targetFriend:
                return chair 
        