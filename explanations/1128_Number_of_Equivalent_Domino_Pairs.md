# Problem: Number of Equivalent Domino Pairs
[LeetCode Problem Link](https://leetcode.com/problems/number-of-equivalent-domino-pairs)

## Problem Statement
Given a list of dominoes, where each domino is represented by a pair of integers, return the number of equivalent domino pairs.

Two dominoes `a = [a1, a2]` and `b = [b1, b2]` are considered equivalent if:
- `a1 == b1` and `a2 == b2`, or
- `a1 == b2` and `a2 == b1`.

## Approach

### Steps:
1. **Sort each domino** to ensure that the order of the numbers doesn't matter. This means `[a, b]` and `[b, a]` are treated the same.
2. **Store the sorted dominoes in a hashmap** where the key is the sorted domino tuple and the value is the count of how many times that domino appears.
3. **Count the number of pairs**:
   - For each unique domino, if it appears `n` times, the number of pairs can be calculated by the formula: `n * (n - 1) / 2`.
   - This formula comes from the combinatorial principle of selecting two items from a set of size `n`.

### Code Explanation:

```python
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0 
        hashmap = {}
        for d in dominoes:
            key = tuple(sorted(d))  # Sort domino to handle different orders
            hashmap[key] = hashmap.get(key, 0) + 1  # Increment frequency
        
        for val in hashmap.values():
            count += val * (val - 1) // 2  # Calculate pairs for each frequency

        return count
```