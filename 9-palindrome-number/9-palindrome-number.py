class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        reverse_num = 0
        digit=0
        
        while x // 10**digit !=0 :
            
            reverse_num = ((x//10**digit)%10) + (reverse_num*10)
            digit+=1
            
        return x== reverse_num    
            