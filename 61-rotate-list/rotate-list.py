class Solution:
    def rotateRight(self, head, k):
        
        # Empty list or single node
        if not head or not head.next:
            return head

        # 1. Find length and tail
        n = 1
        tail = head

        while tail.next:
            tail = tail.next
            n += 1

        # 2. Reduce k
        k = k % n

        # No rotation needed
        if k == 0:
            return head

        # 3. Make list circular
        tail.next = head

        # 4. Find new tail
        steps = n - k

        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # 5. New head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head