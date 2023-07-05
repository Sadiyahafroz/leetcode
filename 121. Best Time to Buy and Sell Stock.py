class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=prices[0]
        for price in prices:
            if price<x:
                x=price
        print("Min Price",x)
        i=prices.index(x)
        print(i)
        y=prices[-1]
        l=len(prices)
        
        for j in range(len(prices)):
            if prices[j]>y:
                if j>i:
                    y=prices[j]
                    print(prices[j])
        print("Max price",y)
        print(prices.index(y))
            
        profit=y-x
        return profit