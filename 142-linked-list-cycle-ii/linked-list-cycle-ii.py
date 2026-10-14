class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: Detect the cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            # No cycle exists
            return None

        # Step 2: Find the cycle entrance
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow