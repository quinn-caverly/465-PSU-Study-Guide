class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(current1, current2): #input is the head of a linked list
            if current1.val <= current2.val:
                return_head = current1
                current1 = current1.next
            else:
                return_head = current2
                current2 = current2.next

            cur = return_head
            while current1 != None and current2 != None:
                if current1.val <= current2.val:
                    cur.next = current1
                    cur = cur.next
                    current1 = current1.next
                else:
                    cur.next = current2
                    cur = cur.next
                    current2 = current2.next

            if current1 == None:
                cur.next = current2
            else:
                cur.next = current1
                
            return return_head

        def calcHalfLength(head): #this could be quickened by counting by 2 instead of one, n -> n/2
            current=head
            count=0
            while current:
                current=current.next
                count+=1
            return count//2

        def mergesort(head):
            if head.next == None:
                return head

            half_length = calcHalfLength(head)
            current = head
            count = 1
            while count < half_length:
                current = current.next
                count+=1

            second_head = current.next
            current.next = None

            return merge(mergesort(head), mergesort(second_head))

        if head == None:
            return None
        return mergesort(head)
