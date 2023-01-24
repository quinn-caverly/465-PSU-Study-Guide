class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(a, b):
            if a.val <= b.val:
                head, a = a, a.next
            else:
                head, b = b, b.next

            current = head
            while a!=None and b!=None:
                if a.val <= b.val:
                    current.next, a = a, a.next
                    current = current.next
                else:
                    current.next, b = b, b.next
                    current = current.next

            if a==None:
                current.next = b
            else:
                current.next = a
            return head

        #handles edge cases where lists are None, etc.
        queue = []
        for i in lists:
            if i != None:
                queue.append(i)
        if len(queue) == 0:
            return None

        #uses a queue, iterative instead of a recursive mergesort function
        while len(queue) > 1:
            queue.insert(0, merge2Lists(queue.pop(), queue.pop()))

        return queue[0]
