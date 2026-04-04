class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_2_list = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            sorted_str_2_list[sorted_str].append(string)
        
        return [v for k,v in sorted_str_2_list.items()]