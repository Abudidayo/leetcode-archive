class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # [1,1,1,6,1,1,1]

        ans = 0

        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] == colors[j]:
                    continue
                
                ans = max(ans, abs(i-j))

        return ans
