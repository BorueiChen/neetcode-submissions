class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        element_list = []
        for element in nums:
            if element not in element_list:
                element_list.append(element)
            else:
                return True
        return False