# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if the linked list has a cycle.

        Args:
            head: The head node of the linked list.

        Returns:
            True if the linked list has a cycle, False otherwise.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
        
## 141. Linked List Cycle
