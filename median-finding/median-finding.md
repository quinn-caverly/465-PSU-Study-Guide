🟧 Bucket method to find kth largest element. (lecture covered the process for finding kth smallest): https://leetcode.com/problems/kth-largest-element-in-an-array

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #1) pick v at random
        #2) linear scan to see if v is in the middle 50%, i.e., bet 25% and 75%
        #3) if v bad, go back to 1
        #4) either return v because v is kth largest or call func again

        #running-time: T(3n/4) + O(n) -> O(n) by Master's Theorem

        def go():
            #step 1
            v = random.choice(nums)

            #step 2
            sL, sR, sV = [], [], []
            for i in nums:
                if i == v:
                    sV.append(i)
                elif i < v:
                    sL.append(i)
                else:
                    sR.append(i)

            #step 3
            if len(sL)/len(nums) > 0.75 or len(sR)/len(nums) > 0.75:
                return go()

            #step 4
            if k <= len(sR):
                return self.findKthLargest(sR, k)
            elif k <= len(sR) + len(sV):
                return v
            else:
                return self.findKthLargest(sL, k-len(sR)-len(sV))
            
        return go()
  ```
  ---

🟧 Max subarry problem which was covered in lecture, but this algo returns the # of subarrays not the actual subarrays as was in lecture: https://leetcode.com/problems/maximum-subarray

first solution which I did prior to the class, solves in one iteration of the array, beats 98% of solutions on leetcode (apparently this is called Kadane's algorithm, can't be used for lecture problem because problem shown in lecture actually returns the sub-array not the max value)
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_val = nums[0]
        for i in nums[1::]:
            if current+i<i: #if we gain nothing by increasing the size of the array
                current = i
            else:
                current += i
            if current > max_val:
                max_val = current
        return max_val
```

