class Solution:
    def partition(self, head, x):
        
        # Dummy nodes
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy

        curr = head

        while curr:
            next_node = curr.next

            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = next_node

        # Connect the two partitions
        less.next = greater_dummy.next

        # Important: terminate the greater list
        greater.next = None

        return less_dummy.next