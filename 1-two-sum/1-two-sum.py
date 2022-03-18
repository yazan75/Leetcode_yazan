class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if 1 >= len(nums) or len(nums) > 10**4 :
  
            return False

        dict1={}
    
        for i in range (len(nums)):
            if nums[i] in dict1:
                return dict1[nums[i]], i
            else: 
                dict1[target-nums[i]] = i 