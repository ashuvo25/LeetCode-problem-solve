from queue import PriorityQueue
class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()

        for i in nums:
            if pq.qsize() >= k:
              if pq.queue[0] < i:
                pq.get()
                pq.put(i)
              else:
               continue
                
            else:
                pq.put(i)
        return pq.get()

        


