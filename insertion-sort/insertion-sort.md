🟧 Basic insertion sort with linked list: https://leetcode.com/problems/insertion-sort-list

```python
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head, current = ListNode(head.val), head.next
        while current!=None:
            prev, sorted_iterator, done = ListNode("placeholder", sorted_head), sorted_head, False

            while sorted_iterator!=None:
                if current.val < sorted_iterator.val:
                    if prev.val == "placeholder":
                        new_head = ListNode(current.val, sorted_head)
                        sorted_head, done = new_head, True
                        break
                    else:
                        new_node = ListNode(current.val, sorted_iterator)
                        prev.next, done = new_node, True
                        break
                prev = sorted_iterator
                sorted_iterator=sorted_iterator.next

            if done==False:
                prev.next = ListNode(current.val)

            current=current.next

        return sorted_head
```
