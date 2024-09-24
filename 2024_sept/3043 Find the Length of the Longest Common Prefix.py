class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr2) > len(arr1):
            arr1, arr2 = arr2, arr1
        
        all_prefix = set()

        for num in arr1:
            while num > 0 and num not in all_prefix: 
                all_prefix.add(num)
                num = num // 10
        res = 0
        for num in arr2:
            if num in all_prefix:
                res = max(res, len( str(num) ))
            else:
                while num > 0 and num not in all_prefix:
                    num = num // 10
                if num in all_prefix:
                    res = max(res, len( str(num) ))
        
        return res
        