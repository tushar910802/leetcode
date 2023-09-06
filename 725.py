# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """
        Splits a linked list into k parts.

        Args:
            root: The head of the linked list.
            k: The number of parts to split the list into.

        Returns:
            A list of k linked lists, each of which is a part of the original list.
        """
        ans = [[] for _ in range(k)]
        length = 0
        curr = root
        while curr:
            length += 1
            curr = curr.next
        subLength = length // k
        remainder = length % k

        prev = None
        head = root

        for i in range(k):
            ans[i] = head
            for j in range(subLength + (1 if remainder > 0 else 0)):
                prev = head
                head = head.next
            if prev:
                prev.next = None
            remainder -= 1

        return ans
        


## 725. Split Linked List in Parts
