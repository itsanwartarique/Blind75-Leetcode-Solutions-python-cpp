class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        hashMap = {}
        res = []
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] +=1
        heapq.heapify(minHeap)
        for i in hashMap:
            heapq.heappush(minHeap,(hashMap[i],i))
            while(len(minHeap)>k):
                heapq.heappop(minHeap)
        for i in minHeap:
            res.append(i[1])
        return res