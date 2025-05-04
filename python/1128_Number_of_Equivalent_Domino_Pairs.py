class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0 
        hashmap = {}
        for d in dominoes:
            key = tuple(sorted(d))
            hashmap[key] = hashmap.get(key, 0) + 1

        for val in hashmap.values():
            count += val * (val - 1) // 2  # number of pairs

        return count
