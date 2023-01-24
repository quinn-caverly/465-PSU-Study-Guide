
https://leetcode.com/problems/sort-an-array/

<details>
<summary>Basic Mergesort Implementation on Integer Array</summary>
<br>
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(a, b):
            length_a = len(a) #faster than repetitively computing len(a)/len(b)
            length_b = len(b)
            index_a = 0
            index_b = 0

            output_array = []
            for i in range(length_a+length_b):
                if index_a == length_a:
                    while index_b < length_b: #could also use np.concatenate, this is faster
                        output_array.append(b[index_b])
                        index_b+=1
                    break
                if index_b == length_b:
                    while index_a < length_a:
                        output_array.append(a[index_a])
                        index_a+=1
                    break

                if a[index_a] <= b[index_b]:
                    output_array.append(a[index_a])
                    index_a+=1
                else:
                    output_array.append(b[index_b])
                    index_b+=1

            return output_array

        def mergesort(nums):
            if len(nums) > 1:
                return merge(mergesort(nums[0:len(nums)//2]), mergesort(nums[len(nums)//2::]))
            else:
                return nums

        return mergesort(nums)
```
</details>

https://leetcode.com/problems/sort-list/
```python
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
```
https://leetcode.com/problems/merge-k-sorted-lists/
```python
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
```
