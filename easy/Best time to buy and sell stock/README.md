# Best Time to Buy and Sell Stock

## 📝 Problem Description

📘 **Problem:** [Best Time to Buy and Sell Stock - LeetCode #121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)


You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.  
If you cannot achieve any profit, return 0.

---

### 🔐 Constraints:
- 1 <= prices.length <= 10⁵  
- 0 <= prices[i] <= 10⁴

---

### 📥 Input:
- `prices`: A list of integers representing stock prices per day

### 📤 Output:
- An integer representing the maximum possible profit

---

## 📊 Example 1:

**Input:**  
`prices = [7,1,5,3,6,4]`  
**Output:**  
`5`  
**Explanation:**  
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

---

## 📊 Example 2:

**Input:**  
`prices = [7,6,4,3,1]`  
**Output:**  
`0`  
**Explanation:**  
No profit can be made, so return 0.

---

## ✅ My Solution Explanation

This solution uses a **one-pass greedy algorithm** that keeps track of the **lowest price so far** and the **maximum profit** that can be made.

### ✨ How it works:
1. Start with the first price as the minimum (`min_price`) and initialize `best_res` (the result) to 0.
2. Loop through each price in the list:
   - If we find a price lower than our `min_price`, we update `min_price` and also reset `max_price` to this new minimum.
   - If the current price is higher than the current `max_price`, we update `max_price` and calculate the profit (`max_price - min_price`), then update `best_res` if this profit is better than the previous.
3. Return `best_res` at the end.

### 💡 Intuition:
We always want to buy at the lowest possible price **before** a higher price comes, so we track the minimum and whenever the current price is profitable, we consider selling.

---

## 🧾 Code

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_price = 0
        best_res = 0
        for i in prices:
            if min_price > i:
                min_price = i
                max_price = i
            elif i > max_price:
                max_price = i
                best_res = max(best_res, max_price - min_price)
                
        return best_res

```

## 🧠 Complexity

   
- Time Complexity: O(n)



## 📌 Tags

`greedy`, `array`, `esay`