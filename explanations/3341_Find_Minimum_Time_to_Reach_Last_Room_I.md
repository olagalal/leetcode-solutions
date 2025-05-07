# Problem: Find Minimum Time to Reach Last Room I
[LeetCode Problem Link](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i)

## Problem Statement

You are in a **dungeon with rooms arranged as a grid** of size `n x m`.

Each room is only accessible **after a certain time**, given in the matrix `moveTime`, where `moveTime[i][j]` is the earliest time you are allowed to *start moving into* room `(i, j)`.

* You start at room `(0, 0)` at time `0`.
* Moving to an **adjacent room** (up, down, left, right) takes **exactly 1 second**.
* You can **wait** in a room if needed.

**Goal:** Return the minimum time needed to reach the **bottom-right room** `(n-1, m-1)`.

## Approach

We use **Dijkstra's algorithm** (greedy + min-heap) to find the shortest time to reach each room.

### Key Observations:

* You can only move to a room if:

  * It’s adjacent.
  * The current time is **greater than** its `moveTime`.
* So, to enter a room at `(i, j)`, you must wait until at least `moveTime[i][j] + 1`.

### Why Dijkstra's?

* Each move has equal cost (1 second), but **some rooms are locked** until a future time.
* We need the earliest possible time to reach every room → Dijkstra with a min-heap fits perfectly.

## Steps:

1. **Initialize**:

   * `dist` matrix to keep track of the **minimum time** to reach each room.
   * `heap` (priority queue) initialized with `(0, 0, 0)` for time 0 at cell `(0, 0)`.

2. **Explore neighbors**:

   * For each cell `(x, y)`, check all 4 directions.
   * Skip if out of bounds.
   * Calculate `nextTime = max(currTime + 1, moveTime[nx][ny] + 1)`.

     * You move in 1 second, but may need to **wait** until `moveTime` allows entry.
   * If `nextTime` is less than the previously known time to reach `(nx, ny)`, update it and add it to the heap.

3. **Return the time** when we reach `(n - 1, m - 1)`.

## Code

```python
from heapq import heappop, heappush
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #  4 neighbors

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]  # (currentTime, x, y)

        while heap:
            currTime, x, y = heappop(heap)

            if (x, y) == (n - 1, m - 1):
                return currTime

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m: # don't go out of bounds
                    nextTime = max(currTime + 1, moveTime[nx][ny] + 1)
                    if nextTime < dist[nx][ny]: # check if we found a faster way to reach (nx, ny)
                        dist[nx][ny] = nextTime
                        heappush(heap, (nextTime, nx, ny))

        return -1
```

## Complexity

* **Time complexity:** `O(n * m * log(n * m))`
  Each room is visited once, and we use a heap for efficient retrieval.

* **Space complexity:** `O(n * m)`
  For the `dist` matrix and priority queue.
