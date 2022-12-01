class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1 =  "aeiouAEIOU"
        
        count_i1 = 0
        count_i2 = 0
        l = int(len(s)/2)
        for i in range(0,l):
            if s[i] in s1:
                count_i1 += 1
            if s[i + l] in s1:
                count_i2 += 1
        return count_i1 == count_i2