# codind=utf-8
"""
4. 寻找两个正序数组的中位数
细节靠硬写逻辑过去的，不够美观，有优化空间
"""
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         output = -1
#         n1, n2 = len(nums1), len(nums2)
#         is_even = (n1 + n2) % 2
#         k_left = (n1 + n2 + 1) // 2
#         # 交换数组保证较短数组为nums1，保证时间复杂度为 log(min(m, n))
#         if n1 > n2: 
#             output = self.findMedianSortedArrays(nums2, nums1)
#         # 边界值处理
#         elif n2 == 0:
#             output = nums2[(n1 - 1) // 2]
#             if not is_even:
#                 output += nums2[n1  // 2]
#                 output /= 2
#         else:
#             left1, right1 = 0, n1 - 1
#             while left1 <= right1:
#                 # 将sep_left_{i}作为 nums{i} 分割后左边部分的最后一个变量的索引
#                 sep_left_1 = left1 + (right1 - left1) // 2
#                 sep_left_2 = k_left - sep_left_1 - 2 
#                 if sep_left_2 > (n2 - 1) or (sep_left_2 == (n2 - 1)) and nums2[-1] > nums1[sep_left_1 + 1]:
#                     left1 = mid1 + 1
#                     continue
#                 elif sep_left_2 < -1 or (sep_left_2==-1 and nums1[sep_left_1]>=nums2[0]):
#                     right1 = mid - 1
#                     continue
#                 elif sep_left_1 == n1 - 1 and nums1[sep_left_1] > nums2[sep_left_2 + 1]:
#                     right1 = mid - 1
#                     continue
#                 elif nums1[sep_left_1] > nums2[sep_left_2 + 1]:
#                     right1 = mid - 1
#                     continue
#                 elif nums1[sep_left_1 + 1] < nums2[sep_left_2]:
#                     left1 = mid1 + 1
#                     continue
#                 else:
#                     if sep_left_2 < 0 or sep_left_2 >= len(nums2):
#                         output = nums1[sep_left_1]
#                     else:
#                         output = max(nums1[sep_left_1], nums2[sep_left_2])
#                     if not is_even:
#                         if sep_left_1 >= len(nums1):
#                             output += nums2[sep_left_2 + 1]
#                         elif sep_left_2 >= len(nums2):
#                             output += nums1[sep_left_1 + 1]
#                         else:
#                             output += min(nums1[sep_left_1 + 1], nums2[sep_left_2 + 1])
#                         output /= 2
#                     break
#         return output







class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n1 = len(nums1) if nums1 is not None else 0
        n2 = len(nums2) if nums2 is not None else 0
        # if n1 > n2:
        #     nums1, nums2 = nums2, nums1

        output = 0

        if n1 * n2 == 0:
            nums = nums1 + nums2
            nn = n1 + n2
            output = (nums[(nn - 1) // 2] + nums[nn // 2]) / 2
            return output

        is_odd = (n1 + n2 + 1) % 2        
        k = (n1 + n2 + 1) // 2

        i, j = 0, 0
        while True:
            m_k = k // 2
            if (m_k - 1) + i > n1 - 1:
                if nums1[-1] <= nums2[(m_k - 1) + j]:
                    k = k - (n1 - i)
                    i = n1
                else:
                    k = k - m_k
                    j = j + m_k
            elif (m_k - 1) + j > n2 - 1:
                if nums2[-1] <= nums1[(m_k - 1) + i]:
                    k = k - (n2 - j)
                    j = n2
                else:
                    k = k - m_k
                    i = i + m_k
            elif nums1[(m_k - 1) + i] <= nums2[(m_k - 1) + j]:
                k = k - m_k
                i = i + m_k
            elif nums1[(m_k - 1) + i] > nums2[(m_k - 1) + j]:
                k = k - m_k
                j = j + m_k
            
            if i == n1:
                output = nums2[j + (k - 1)]
                if is_odd: 
                    output += nums2[j + k]
                    output /= 2.0
                break
            elif j == n2:
                output = nums1[i + (k - 1)]
                if is_odd: 
                    output += nums1[i + k]
                    output /= 2.0
                break
            elif k == 1:
                arr = sorted(nums1[i: i + 2] + nums2[j: j + 2])
                output = arr[0]
                if is_odd:
                    output += arr[1]
                    output /= 2
                break
        
        return output

    def findK(self):
        pass
       
        

if __name__ == "__main__":
#     nums1 = [1, 3]
#     nums2 = [2]
    nums1 = [4]
    nums2 = [1, 2, 3, 5, 6, 7]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))

    