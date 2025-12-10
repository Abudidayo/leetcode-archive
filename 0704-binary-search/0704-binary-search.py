class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        m = None

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

        # First attempt
        # l, r = 0, len(max) - 1
        # m = None
        # for i in range(len(nums)):
        #     m = len(max) / 2
        #     if nums[m] == target:
        #         return True
        #     elif nums[i] > m:
        #         nums[m:]
        #         l = m + 1
        #         m = len(max) / 2
        #     elif nums[i] < m:
        #         nums[:m]
        #         r = m - 1
        #         m = len(max) / 2

        # return True