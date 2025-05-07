# Problem: 3536. Maximum Product of Two Digits
[LeetCode Problem Link](https://leetcode.com/problems/maximum-product-of-two-digits/)

## Problem Statement

You are given an integer `n`. Extract all digits of `n` and return the **maximum product** of any two **distinct digits**.

### Example:

**Input:** `n = 9288`
**Output:** `72`
**Explanation:** Digits are \[9, 2, 8, 8]. The highest product is 9 × 8 = 72.


## Approach

### Step-by-Step:

1. **Extract all digits** of `n` using modulus `% 10` and integer division `// 10`.
2. **Store the digits** in a list.
3. **Sort the digits** in descending order.
4. The answer is the product of the **two largest digits**.

### Why it works:

The highest product of any two digits must come from the two largest digits. Since we only need the top 2, sorting or finding top two max values is sufficient.

### Code Explanation:
```python
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        digits.sort(reverse=True)

        return digits[0] * digits[1]
```

## 💡 Follow-up

**What if we don't want to use extra space?**

If we don't want to use an extra list to store digits:

* We can track the top two digits **in-place** while iterating through `n`.

```python
class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = max2 = 0
        while n > 0:
            digit = n % 10
            if digit > max1:
                max1, max2 = digit, max1
            elif digit > max2:
                max2 = digit
            n //= 10
        return max1 * max2
```

This version uses **O(1) space** and is more efficient.

## Summary:

| Approach        | Time Complexity     | Space Complexity | Notes                             |
|----------------|---------------------|------------------|-----------------------------------|
| Extra Array     | O(d log d)          | O(d)             | Sorts digits after extracting     |
| In-Place (O(1)) | O(d)                | O(1)             | Tracks top 2 digits while looping |

