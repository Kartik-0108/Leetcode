class Solution:
    def isPalindrome(self, head):
        
        # 1. Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. If length is odd, skip the middle node
        if fast:
            slow = slow.next

        # 3. Reverse the second half
        prev = None

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # 4. Compare first half with reversed second half
        while prev:
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next

        return True