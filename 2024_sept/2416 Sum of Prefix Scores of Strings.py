class PrefixNode:
    def __init__(self):
        self.children = [None]*26
        self.count = 0

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()
    
    def insert(self, w):
        curr = self.root
        for c in w:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = PrefixNode()
            curr = curr.children[i]
            curr.count += 1
        
        return
    
    def get_score(self, w):
        curr = self.root
        score = 0
        for c in w:
            i = ord(c) - ord('a')
            curr = curr.children[i]
            score += curr.count
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        
        prefix_tree = PrefixTree()

        for w in words:
            prefix_tree.insert(w)
        
        for w in words:
            res.append( prefix_tree.get_score(w) )

        return res
        