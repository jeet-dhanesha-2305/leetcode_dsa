class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        my_dict = defaultdict(int)
        for elem in arr:
            rem = elem % k
            my_dict[rem] += 1
        
        for key, values in my_dict.items():
            if key != 0 and my_dict[key] != my_dict[k-key]:
                return False
            if key == 0 and my_dict[key] % 2 != 0:
                return False
        return True