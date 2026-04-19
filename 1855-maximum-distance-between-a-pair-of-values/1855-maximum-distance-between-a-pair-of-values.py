class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1 = [55,30,5,4,2]
        # nums2 = [100,20,10,10,5]
        # Output: 2 

        i = 0
        j = 0
        ans = 0

        while 0 <= i < len(nums1) and 0 <= j < len(nums2):

            if i > j:
                j += 1
                continue

            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans
            