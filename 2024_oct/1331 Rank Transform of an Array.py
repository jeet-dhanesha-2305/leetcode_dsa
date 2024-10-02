class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = arr.copy()
        ranks = set(ranks)
        ranks = list(ranks)
        ranks.sort()
        ranks_map = defaultdict(int)
        for i in range(len(ranks)):
            ranks_map[ ranks[i] ] = i+1
        
        res = []
        for elem in arr:
            res.append( ranks_map[elem] )
        return res        