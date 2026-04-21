class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = False
        found = set()
        candiate = {} # target[0]: [idx in triplet], ... 
        for c_idx, triplet in enumerate(triplets):
            for idx, num in enumerate(triplet):
                if num == target[idx]:
                    if num not in candiate:
                        candiate[num] = []
                    candiate[num].append(c_idx)
        if len(candiate[target[0]]) == 0 or len(candiate[target[1]]) == 0 or len(candiate[target[2]]) == 0:
            return False
        result = []
        for c1 in candiate[target[0]]:
            for c2 in candiate[target[1]]:
                for c3 in candiate[target[2]]:
                    result.append([max(triplets[c1][0],  triplets[c2][0], triplets[c3][0]), 
                                max(triplets[c1][1],  triplets[c2][1], triplets[c3][1]), 
                                max(triplets[c1][2],  triplets[c2][2], triplets[c3][2])])
        

        return target in result