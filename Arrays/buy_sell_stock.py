def buy_and_sell_once(A):
  max_profit = 0
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[j] - A[i] > max_profit:
          max_profit = A[j] - A[i]
  return max_profit


def buy_and_sell_stock_once(prices):
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        # print(price)
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
        print(f'price ={price}, min={min_price},  com={compare_profit}, max={max_profit}')
    return max_profit

def maxProfit(prices):
        
        buyprice = prices[0]
        profit = 0
		
        for i in range(1,len(prices)) :
		
            if buyprice < prices[i] :
                profit = max(profit,(prices[i]-buyprice))
				
            else:
                buyprice = prices[i]
				
        return profit

def profit(stock_prices):
    
    # Start minimum price marker at first price
    min_stock_price = stock_prices[0]
    
    # Start off with a profit of zero
    max_profit = 0
    
    for price in stock_prices:
        
        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price,price)
        
        # Check the current price against our minimum for a profit 
        # comparison against the max_profit
        comparison_profit = price - min_stock_price
        
        # Compare against our max_profit so far
        max_profit = max(max_profit,comparison_profit)
        
    return max_profit
# P = [900, 315, 275, 295, 260, 10, 290, 230, 255, 250, 600]
P = [30, 35, 27, 90, 20]
# P = [10,200,200,0,0,0,100]

max_pro = buy_and_sell_stock_once(P)
print(max_pro)


# max_pro = maxProfit(P)
# print(max_pro)

# max_pro = buy_and_sell_once(P)
# print(max_pro)