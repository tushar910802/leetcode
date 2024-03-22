# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseList(head: ListNode) -> ListNode:
            """
            Determines if a singly-linked list is a palindrome.

            Parameters:
            - head (Optional[ListNode]): The head of the linked list.

            Returns:
            - bool: True if the linked list is a palindrome, False otherwise.

            Example:
            Given the linked list 1 -> 2 -> 2 -> 1, the function should return True,
            as the linked list is a palindrome.

            Note:
            - The function uses a two-pointer approach to find the middle of the linked list.
            - It then reverses the second half of the linked list.
            - Finally, it compares the values of the first and second halves to determine
            if the linked list is a palindrome.
            """
            prev = None
            curr = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        slow = reverseList(slow)

        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True