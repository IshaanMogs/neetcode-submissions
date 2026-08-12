class Solution(object):
    def merge(self, nums1, m, nums2, n):
            f = m-1
            s = n-1
            k = len(nums1)-1
            while f>=0 and s>=0:
                if nums2[s]>nums1[f]:
                    nums1[k] = nums2[s]
                    s-=1
                    k-=1
                else:
                    temp = nums1[k]
                    nums1[k] = nums1[f]
                    nums1[f] = temp
                    f-=1
                    k-=1
            while s>=0:
                nums1[k] = nums2[s]
                s-=1
                k-=1
            return nums1
                