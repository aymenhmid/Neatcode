# complexity O(n+k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
#2nd approach
# initialize counter O(n) , sort dict O(m log m) ,extract top k elements : O(m+k)
from collections import OrderedDict
from collections import Counter
class Solution:
    def topKFrequent(self, nums,k):
        
        my_dict = Counter(nums)
        sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_dict_desc.keys())[:k]
