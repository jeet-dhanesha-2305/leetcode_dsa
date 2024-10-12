class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        start, end = [], []
        n = len(intervals)

        for s, e in intervals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()

        s, e = 0, 0
        grp, res = 0, 0
        
        while s < n:
            if start[s] <= end[e]:
                grp += 1
                s += 1
            else:
                grp -= 1
                e += 1
            res = max(res, grp)
        
        return res
        