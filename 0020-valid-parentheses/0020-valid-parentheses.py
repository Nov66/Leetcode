class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpenPair = { ")": "(", "}": "{", "]": "[" }
        pair = []

        for c in s:
            if c in closeToOpenPair:
                if pair and pair[-1] == closeToOpenPair[c]:
                    pair.pop()
                else:
                    return False
            else: 
                pair.append(c)
        
        return not pair 