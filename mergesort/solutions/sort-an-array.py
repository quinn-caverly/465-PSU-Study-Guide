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
