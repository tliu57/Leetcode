class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        buckets = {}
        for i, value in enumerate(nums):
            if t > 0:
                bucketNum, offset = int(value/t), 1
            else:
                bucketNum, offset = value, 0
            for idx in xrange(bucketNum-offset, bucketNum+offset+1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True
            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                if t > 0:
                    del buckets[nums[i-k]/t]
                else:
                    del buckets[nums[i-k]]
        
        return False
                
                
