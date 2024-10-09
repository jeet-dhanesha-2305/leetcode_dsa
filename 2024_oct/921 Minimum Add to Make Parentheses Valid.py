class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        myStack = deque()
        
        res = 0
        for br in s:
            if br == "(":
                myStack.append(br)
            else:
                if len(myStack) > 0:
                    myStack.pop()
                else:
                    res += 1
        
        if len(myStack) > 0:
            res += len(myStack)
        
        return res

        