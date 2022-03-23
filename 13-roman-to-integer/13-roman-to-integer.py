class Solution:
    def romanToInt(self, s: str) -> int:
        
        roma= {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        total = 0
        cerrent = 0
        prev = 0
        
        for i in range(len(s)):
            current = roma[s[i]]
            if current > prev:
                total = total + current - 2*prev
            else : total = total + current    
            prev = current
        return total    
        