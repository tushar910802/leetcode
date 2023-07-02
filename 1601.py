# DFS
class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        self.ans = 0
        self.requests = requests
        arr1 = [0] * n
        arr2 = [0] * n
        cur_flags = [0] * len(self.requests)
        self.dfs(0, arr1, arr2, cur_flags)
        return self.ans

    def dfs(self, cur_ind, arr1, arr2, cur_flags):
        if cur_ind == len(self.requests):
            flag = True
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    flag = False
                    break
            if flag == True:
                self.ans = max(self.ans, sum(cur_flags))
            return
        self.dfs(cur_ind + 1, arr1, arr2, cur_flags)
        arr1[self.requests[cur_ind][0]] += 1
        arr2[self.requests[cur_ind][1]] += 1
        cur_flags[cur_ind] = 1
        self.dfs(cur_ind + 1, arr1, arr2, cur_flags)
        arr1[self.requests[cur_ind][0]] -= 1
        arr2[self.requests[cur_ind][1]] -= 1
        cur_flags[cur_ind] = 0



### 1601. Maximum Number of Achievable Transfer Requests
