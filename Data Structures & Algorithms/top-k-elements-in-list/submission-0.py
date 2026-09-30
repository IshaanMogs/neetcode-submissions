class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        count = []
        for i in range(len(nums)):
           freq[nums[i]]=freq.get(nums[i],0)+1
        
        while len(count)<k:
            largest = max(freq.values())
            for key,value in freq.items():
                if value==largest:
                    count.append(key)
                    del freq[key]
                    break
        return count
