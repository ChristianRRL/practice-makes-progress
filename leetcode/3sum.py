class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        l = []
        # for i, x in enumerate(nums):
        #     for j, y in enumerate(nums):
        #         for k, z in enumerate(nums):
        #             if (i != j) and (i != k) and (j != k):
        #                 if (x + y + z) == 0:
        #                     l.append([x,y,z])
        
        for i, x in enumerate(nums[:len(nums)-2]):
            for j, y in enumerate(nums[1:len(nums)-1]):
                for k, z in enumerate(nums[2:]):
                    if (i != j) and (i != k) and (j != k):
                        if (x + y + z) == 0:
                            l.append([x,y,z])
        # NOTE: Above is wrong answer
        
        return l