class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for idx, num in enumerate(triplet):
                if num == target[idx]:
                    found.add(idx)
        

        return len(found) == 3