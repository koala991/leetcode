class Solution:
    # def maxArea(self, height: List[int]) -> int:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_aera = 0
        while left < right:
            if height[left] <= height[right]:
                tmp_area = (right - left) * height[left]
                left += 1
            else:
                tmp_area = (right - left) * height[right]
                right -= 1
            max_aera = max(tmp_area, max_aera)
        return max_aera

if __name__=="__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))

