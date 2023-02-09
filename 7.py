class Solution(object):
    def reverse(self, x):
        
        result = 0
        flag = 1
        if x < 0:
            x = abs(x)
            flag = -1
        
        while x > 0:
            if result > 214748364:
                return 0
            else:
                result = result * 10 + x % 10
                x = x/10
                
        return result * flag