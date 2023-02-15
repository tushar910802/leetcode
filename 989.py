class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        N = len(num)
        carry = 0
        num[-1] += k
        for i in range(N-1,-1,-1):  
            num[i] +=  carry
            carry = 0
            if num[i] >= 10:
                carry += num[i]//10
                num[i] %= 10
            
        overflow = []
        while carry > 0:
            overflow.append(carry%10)
            carry //=10
        overflow.reverse()
        return overflow + num
