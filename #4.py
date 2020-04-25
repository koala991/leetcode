# codind=utf-8

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        output = -1
        n1, n2 = len(nums1), len(nums2)
        is_even = (n1 + n2) % 2
        k_left = (n1 + n2 + 1) // 2
        # 交换数组保证较短数组为nums1，保证时间复杂度为 log(min(m, n))
        if n1 > n2: 
            output = self.findMedianSortedArrays(nums2, nums1)
        # 边界值处理
        elif n2 == 0:
            output = nums2[(n1 - 1) // 2]
            if not is_even:
                output += nums2[n1  // 2]
                output /= 2
        else:
            left1, right1 = 0, n1 - 1
            while left1 <= right1:
                # 将sep_left_{i}作为 nums{i} 分割后左边部分的最后一个变量的索引
                sep_left_1 = left1 + (right1 - left1) // 2
                sep_left_2 = k_left - sep_left_1 - 2 
                if sep_left_2 > (n2 - 1) or (sep_left_2 == (n2 - 1)) and nums2[-1] > nums1[sep_left_1 + 1]:
                    left1 = mid1 + 1
                    continue
                elif sep_left_2 < -1 or (sep_left_2==-1 and nums1[sep_left_1]>=nums2[0]):
                    right1 = mid - 1
                    continue
                elif sep_left_1 == n1 - 1 and nums1[sep_left_1] > nums2[sep_left_2 + 1]:
                    right1 = mid - 1
                    continue
                elif nums1[sep_left_1] > nums2[sep_left_2 + 1]:
                    right1 = mid - 1
                    continue
                elif nums1[sep_left_1 + 1] < nums2[sep_left_2]:
                    left1 = mid1 + 1
                    continue
                else:
                    if sep_left_2 < 0 or sep_left_2 >= len(nums2):
                        output = nums1[sep_left_1]
                    else:
                        output = max(nums1[sep_left_1], nums2[sep_left_2])
                    if not is_even:
                        if sep_left_1 >= len(nums1):
                            output += nums2[sep_left_2 + 1]
                        elif sep_left_2 >= len(nums2):
                            output += nums1[sep_left_1 + 1]
                        else:
                            output += min(nums1[sep_left_1 + 1], nums2[sep_left_2 + 1])
                        output /= 2
                    break
        return output








       
        

if __name__ == "__main__":
    nums1 = [2, 2, 2, 2, 4, 5, 7]
    nums2 = [2, 4, 7, 7]
    assert Solution().findMedian(nums1) == (2, 3, 3)
    assert Solution().findMedian(nums2) == (5.5, 1, 2)

    # output = Solution().findMedianSortedArrays(nums1, nums2)
    # assert output == 4

    # nums1 = [1, 2]
    # nums2 = [3, 4]
    # output = Solution().findMedianSortedArrays(nums1, nums2)
    # assert output == 2.5

    # nums1 = [1, 3]
    # nums2 = [2]
    # output = Solution().findMedianSortedArrays(nums1, nums2)
    # assert output == 2
