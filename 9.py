class Solution(object):
    def isPalindrome(self, x):
        
        y = x
        result = 0
        if x < 0:
            return False
        
        while x > 0:
            result = result * 10 + x%10
            x = x/10
            
        if y == result:
            return True
        else:
            return False