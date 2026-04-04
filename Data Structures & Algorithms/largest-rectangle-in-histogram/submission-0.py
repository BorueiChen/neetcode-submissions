class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        for idx in range(len(heights)):
            start = idx
            if not stack:
                stack.append((start, heights[idx]))
                continue

            while stack and stack[-1][1] > heights[idx]:
                start, h = stack.pop()
                ans = max(ans, h * (idx - start))

            stack.append((start, heights[idx]))
        
        while stack:
            start, h = stack.pop()
            ans = max(ans, h * (len(heights) - start))

        return ans       