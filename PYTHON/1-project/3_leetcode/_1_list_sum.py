
from typing import List
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int] :
        for i in range(len(nums)):
             for j in range (i+1,len(nums)):
                if nums[i]+nums[j]==target:
                   return [i,j]
                

new_instance = Solution()
return_value =new_instance.twoSum([3,2,4,7],9)
print(return_value)
