'''
Write a program that takes an array that denotes the daily closing prices of a stock to determine the maximum profit by buying and selling one share of the stock.

Input Format

9
310 315 275 260 270 290 230 255 250

Constraints

NA

Output Format

30

Sample Input 0

9
310 315 275 260 270 290 230 255 250
Sample Output 0

30
Explanation 0

Buy at 260, Sell at 290

Sample Input 1

4
1 2 3 4
Sample Output 1

3
Explanation 1

Buy at 1, Sell at 4
'''


n=int(input())
prices=list(map(int,input().split()))
min_price = prices[0]
max_profit = 0
for price in prices:
    min_price = min(price, min_price) 
    profit = price - min_price         
    max_profit = max(profit, max_profit)  
print(max_profit)



    
