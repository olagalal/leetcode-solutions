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
