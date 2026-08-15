class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lista = {}
        for i in nums:
          if i in lista:
            lista[i] += 1
          else:
            lista[i] = 1
          while lista[i] >=2:
            return True
        return False
