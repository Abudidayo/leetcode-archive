class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window: 2 Variables one for buying and one for selling?
        # Keep iterating the numbers after the current, if they are lower than max, THEN set max as that num    

        # maxday = 0

        # for i in range(len(prices)):
        #     for j in range (len(prices)):
        #         if j >= i:
        #             continue
        #         else:
        #             if prices[i] > prices[j]:
        #                 maxday = max((prices[i] - prices[j]), maxday)
        #             else:
        #                 continue

        # return maxday

        # Time Limit Exceeded
        # 198 / 212 testcases passed 
        # Maybe because nested loop n(O^2)??

        # [7,1,5,3,6,4]

        buy_price = prices[0]
        profit = 0

        for i in prices:
            if buy_price > i:
                buy_price = i
            
            profit = max(profit, i - buy_price)

        return profit







