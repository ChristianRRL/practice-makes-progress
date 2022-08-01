class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if i != j:
                    if x + y == target:
                        # print(i,j,x,y)
                        return [i,j]
        
        return None
