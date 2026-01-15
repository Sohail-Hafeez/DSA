class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0
        j = 1
        while i <len(prices):
            while j <len(prices):
                if prices[j]<=prices[i]:
                    prices[i] -= prices[j]
                    break
                j = j+1

            i = i+1
            j = i+1
        return prices
           
            


        