'''

Let's apply it — Problem 5: Best Time to Buy and Sell Stock

You're given an array prices where prices[i] is the stock price on day i. You want to maximize profit by choosing one day to buy and a later day to sell. Return the max profit possible (or 0 if no profit is possible).
Example: prices = [7,1,5,3,6,4] → 5 (buy at 1, sell at 6)


'''


def max_profit(prices):

    min_price = prices[0] 
    max_profit = 0

    for i, price in enumerate(prices):

        if price < min_price:
            min_price = price
        
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

        return max_profit
        
   
