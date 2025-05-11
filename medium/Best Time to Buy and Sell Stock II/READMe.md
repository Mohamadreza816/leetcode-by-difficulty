# Best Time to Buy and Sell Stock II

## 📝 Problem Description
📘 **Problem:** [Best Time to Buy and Sell Stock || - LeetCode #122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150/)

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

You may complete as many transactions as you like — **you can buy and sell the stock multiple times**. However, you can only hold **at most one share** at a time (i.e., you must sell the stock before buying again).  
You may buy and sell on the same day.

---

### 🔐 Constraints:
- 1 <= prices.length <= 3 *  10<sup>4</sup> 
- 0 <= prices[i] <= 10⁴

---
## 📊 Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy at 1, sell at 5 (profit = 4), buy at 3, sell at 6 (profit = 3), total = 7

---
## 🧩 Difference from Previous problem   -> [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

In the first version of the problem (Best Time to Buy and Sell Stock I), you were allowed to only make one transaction — choose the best single buy and sell to maximize profit.

In this version, you can perform as many transactions as you want, as long as you're not holding more than one share at a time.
That means you can buy/sell multiple times over the time span to maximize total profit

---
## 🧪 Solution Logic
The key idea is to accumulate profit whenever there is a price increase.
That is, every time the current price is greater than the previous day's price, we take the profit of the difference.

But in the submitted solution, instead of comparing with previous day's price, we track local minima and maxima manually:

``` python
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_price = 0
        profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
                max_price = i
                continue
            if i > max_price:
                profit += (max_price - min_price)
                min_price = i
                max_price = i

        return profit

```
---
## 🧠 Complexity

   
- Time Complexity: O(n)

---
## 📌 Tags

`array`, `medium`,