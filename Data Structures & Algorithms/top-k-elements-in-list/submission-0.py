class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k_and_frequent = (None, 0)
        frequent_table = {}
        for num in nums:
            if num not in frequent_table:
                frequent_table[num] = 1
            frequent_table[num] = frequent_table[num] + 1
        
        sorted_keys = sorted(frequent_table, key=lambda k: frequent_table[k], reverse=True)

        
        return sorted_keys[:k]