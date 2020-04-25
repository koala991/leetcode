class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        delete=(len1+len2-1)//2
        while delete!=0:
            if len(nums1)==0:
                break
            i=(delete+1)//2
            if len(nums1)<i:
                i=len(nums1)
                if nums1[i-1]<nums2[i-1]:
                    del nums1[0:i]
                else:
                    del nums2[0:i]
            else:
                if nums1[i-1]<nums2[i-1]:
                    del nums1[0:i]
                else:
                    del nums2[0:i]
            delete-=i
        if len(nums1)==0:
            del nums2[0:delete]
        if (len1+len2)%2==1:
            if len(nums1)!=0:
                return min(nums1[0],nums2[0])
            else:
                return nums2[0]
        else:
            if len(nums1)==0:
                return(nums2[0]+nums2[1])/2
            if nums1[0]>nums2[0]:
                min1=nums2.pop(0)
            else:
                min1=nums1.pop(0)
            if len(nums1)!=0:
                if len(nums2)==0:
                    return (nums1[0]+min1)/2
                return (min(nums1[0],nums2[0])+min1)/2
            else:
                return (nums2[0]+min1)/2
