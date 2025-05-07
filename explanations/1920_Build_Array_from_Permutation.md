# Problem: 1920. Build Array from Permutation
[LeetCode Problem Link](https://leetcode.com/problems/build-array-from-permutation)

## Problem Statement

Given a **zero-based permutation** `nums` (i.e., it contains all the integers from `0` to `n - 1`, where `n == len(nums)`), build an array `ans` of the same length such that:

```python
ans[i] = nums[nums[i]]
```

Return the array `ans`.

### Example:

```python
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
```

## ✨ Approach 1: Using Extra Space (Straightforward)

### Steps:

1. Create an empty array `ans` of the same size as `nums`.
2. Loop through the indices from `0` to `n - 1`.
3. For each `i`, set `ans[i] = nums[nums[i]]`.

### Code Explanation:

```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
```

### Complexity:

* **Time:** O(n)
* **Space:** O(n)

## 💡 Follow-up: Solve it Using O(1) Space (In-Place)

### Insight:

We want to avoid using an extra array.
We can **encode two values into one** by using **modular arithmetic**, since all numbers in `nums` are from `0` to `n - 1`.

### Trick:

1. Let `n = len(nums)`.
2. For each `i`, update:

   ```python
   nums[i] += (nums[nums[i]] % n) * n
   ```

   This stores both the old and new values.
3. Finally, divide each value by `n` to retrieve the new value.

### Code Explanation:

```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            nums[i] += (nums[nums[i]] % n) * n
        
        for i in range(n):
            nums[i] //= n
        
        return nums
```

### Why It Works:

* `nums[nums[i]] % n` gets the **original** value of `nums[nums[i]]`, even if it has already been updated.
* Multiplying by `n` shifts the new value into a higher digit space.
* Final division extracts the updated value.

### Complexity:

* **Time:** O(n)
* **Space:** O(1) (in-place)

## Summary:

| Approach        | Time Complexity | Space Complexity | Notes                   |
| --------------- | --------------- | ---------------- | ----------------------- |
| Extra Array     | O(n)            | O(n)             | Straightforward         |
| In-Place (O(1)) | O(n)            | O(1)             | Uses modular arithmetic |
