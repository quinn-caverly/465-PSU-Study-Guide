🟥 Uses binary search to insert into a sorted list to go from O(n^2) to O(log(n)): https://leetcode.com/problems/count-good-triplets-in-an-array

```python 
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        #have an array, pre = [], pre[0] will be 0 because the first element can't have any valid x values infront of it
        #have a second array which we build along, insert_array = [], when we visit an index in nums1, we put its index into 
        #insert_array, keeping it sorted. Ex) if nums1[0] is 3, we search for 3 in nums2, if its index is 5, then insert_array = [5]
        #next, if nums1[1] is 7 and its index is 32 in nums2, then insert_array = [5,32], because the first index of nums1 has the index 1 in
        #the insert_array, then pre[1] = 1 because there is one element which is infront of it

        #O(nlog(n)) because we use binary search to insert element into insert_array

        #returns the number of elements infront of it
        #because len(array) takes O(1) time, the fastest thing here is to do binary search to find the insertion point          
        def insertIntoSortedArray(num, begin_index, end_index):
            if end_index - begin_index == 0:
                insert_array.insert(end_index, num)
                return end_index

            elif end_index-begin_index == 1:
                if num < insert_array[begin_index]:
                    insert_array.insert(begin_index, num)
                    return begin_index
                else:
                    insert_array.insert(end_index, num)
                    return end_index

            middle_index = begin_index + (end_index-begin_index)//2
            compare_to = insert_array[middle_index]

            if num == compare_to:
                insert_array.insert(middle_index+1, num)
                return middle_index+1
            elif num < compare_to:
                return insertIntoSortedArray(num, begin_index, middle_index)
            else:
                return insertIntoSortedArray(num, middle_index+1, end_index)

        n = len(nums1)

        position = [None] * n
        for i in range(n):
            position[nums2[i]] = i

        pre, insert_array = [0]*n, [position[nums1[0]]]
        for i in range(1, n):
            pre[i] = insertIntoSortedArray(position[nums1[i]], 0, len(insert_array))
        
        post, insert_array = [0]*n, [position[nums1[n-1]]]
        for i in range(1, n):
            cur = n-1-i
            post[cur] = len(insert_array)-insertIntoSortedArray(position[nums1[cur]], 0, len(insert_array))

        return_sum = 0
        for a, b in zip(pre, post):
            return_sum += a * b

        return return_sum
```

---

🟥 https://leetcode.com/problems/count-of-smaller-numbers-after-self

```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = [nums[-1]]
        deq = deque([0]) #allows for O(1) inserts when adding to left or right ends

        i = len(nums)-2
        while i >= 0:
            insert_pos = bisect_left(sorted_list,nums[i]) #uses binary search to find insertion point: https://github.com/python/cpython/blob/main/Lib/bisect.py
            sorted_list.insert(insert_pos, nums[i])
            deq.appendleft(insert_pos)
            i-=1

        return deq
```
