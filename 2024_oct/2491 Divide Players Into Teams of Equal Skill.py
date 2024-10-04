class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        total = sum(skill)
        n = len(skill)

        if total % ( n//2 ) != 0:
            return -1
        
        count = Counter(skill)
        
        target = total // ( n//2)
        res = 0

        for s in skill:
            if count[s] == 0:
                continue
            
            diff = target - s
            if count[diff] == 0:
                return -1
            
            res += s*diff
            count[s] -= 1
            count[diff] -= 1
        
        return res