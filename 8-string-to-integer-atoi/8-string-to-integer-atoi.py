class Solution:
    def myAtoi(self, str):
        
        MAX = 2147483647
        MIN = - 2**31
        
        i= 0
        res = 0
        negative = 1
        
        while i < len(str) and str[i] == ' ':
            i += 1
            
        if i < len(str) and str[i] == '-':
            i+=1
            negative = -1
            
        elif i < len(str) and str[i] == '+':
            i+=1
            
        checker = set('0123456789')
        while i < len(str) and str[i] in checker:
            if res > MAX // 10 or (res == MAX//10 and int(str[i])>7):
                return MAX if negative == 1 else MIN
            res = res * 10 + int(str[i])
            i += 1 
            
        return res * negative
            