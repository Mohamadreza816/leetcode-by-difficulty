# Merge Sorted Array

📘 **Problem:** [Merge Sorted Array - LeetCode #88](https://leetcode.com/problems/merge-sorted-array/)

You are given two sorted integer arrays `nums1` and `nums2`, and two integers `m` and `n` representing the number of valid elements in `nums1` and `nums2`.

Your task is to merge `nums2` into `nums1` as one sorted array, **in-place**.

---

## 💡 Approach

This solution uses **three pointers**:
- `p1` points to the last valid element in `nums1`
- `p2` points to the last element in `nums2`
- `p` points to the last position in `nums1` (including the extra space)

We iterate from the end of the array and compare elements from the back, placing the larger one at position `p`. This avoids overwriting useful values in `nums1`.

If any elements remain in `nums2` after the main loop, we copy them directly.

---

## ✅ Python Solution

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None. Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p2 >= 0 and p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
        
```

## 🧠 Complexity

   
- Time Complexity: O(m + n)

- Space Complexity: O(1) (in-place merge)


## 📌 Tags

`Array`, `Two Pointers`, `Sorting`, `In-place` `Algorithm`

