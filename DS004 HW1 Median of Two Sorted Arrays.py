# 4. Median of Two Sorted Arrays
# Runtime: 96 ms, faster than 88.50% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len=len(nums1)+len(nums2)
        mid=total_len//2
        
        def find(lst1, lst2, k, even):
            # k: k-th element, k>=1
            # make sure lst1 is the shorter one
            if (len(lst1)>len(lst2)):
                return find(lst2, lst1, k, even)
            
            if (len(lst1)==0):
                if (even):
                    return (lst2[k-1]+lst2[k])/2
                else:
                    return lst2[k-1]
            #elif (len(lst2)==0):
            #    return lst1[k]
            else:
                # lst1 and lst2 are both not empty
                if (1==k):
                # return the least element
                    flag1=True
                    ret=lst1[0]
                    if (lst1[0]>lst2[0]):
                        flag1=False
                        ret=lst2[0]
                    if(not even):
                        return ret
                    else:
                        # if even, find the next value next to the mid
                        if(flag1):
                            return (ret+find(lst1[1:],lst2,k,False))/2
                        else:
                            return (ret+find(lst1, lst2[1:], k, False))/2
                else:
                    # ind is used to bisection search
                    # ind is capped by the length of lst1
                    # NOTE: if ind is capped by 'lst1', 
                    # we need to make sure lst1 is the shorter one
                    ind1=min(k//2,len(lst1))
                    ind2=k-ind1
                    if lst1[ind1-1]==lst2[ind2-1]:
                        ret=lst1[ind1-1]
                        if (not even):
                            return ret
                        else:
                            return (ret+find(lst1[ind1:], lst2[ind2:], 1, False))/2
                    elif lst1[ind1-1]<lst2[ind2-1]:
                        # lst1[0:ind1] can be removed
                        return find(lst1[ind1:], lst2, k-ind1, even)
                    else:
                        # lst2[0:ind2] can be removed
                        return find(lst1, lst2[ind2:], k-ind2, even)
        
        
        if (total_len%2==1):
            return find(nums1, nums2, mid+1, False)
        else:
