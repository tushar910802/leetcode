# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly-linked list.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.

        Returns:
        - Optional[ListNode]: The new head of the reversed linked list.

        Example:
        Given the linked list 1 -> 2 -> 3 -> 4 -> 5, after reversal,
        the linked list becomes 5 -> 4 -> 3 -> 2 -> 1.

        Note:
        - The function uses a recursive approach to reverse the linked list.
        - It recursively calls itself to reverse the rest of the list.
        - The result is the new head of the reversed linked list.
        """
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead 