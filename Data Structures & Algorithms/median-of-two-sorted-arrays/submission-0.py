class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_array = [0] * (len(nums1) + len(nums2))
        pointer1, pointer2, m_ptr = 0, 0, 0

        while pointer1 < len(nums1) or pointer2 < len(nums2):
            if pointer1 == len(nums1):
                merge_array[m_ptr:] = nums2[pointer2:]
                break
            if pointer2 == len(nums2):
                merge_array[m_ptr:] = nums1[pointer1:]
                break
            
            if nums1[pointer1] < nums2[pointer2]:
                merge_array[m_ptr] = nums1[pointer1]
                pointer1 += 1
            else:
                merge_array[m_ptr] = nums2[pointer2]
                pointer2 += 1
            m_ptr += 1
        
        if (len(nums1) + len(nums2)) % 2 == 1:
            return merge_array[(len(nums1) + len(nums2))//2]
        else:
            mid = (len(nums1) + len(nums2))//2
            return (merge_array[mid - 1] + merge_array[mid]) / 2