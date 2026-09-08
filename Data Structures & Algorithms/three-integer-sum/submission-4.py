class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        index = 0
        res = []
        
        while index < len(nums) - 1:
            curr = nums[index]
            left = index + 1
            right = len(nums) - 1
            while left < right:
                result = nums[left] + nums[right]
                total = result + curr
                if total < 0 :
                    left+=1
                elif total > 0:
                    right-=1
                else:
                    threesum = [nums[index], nums[left], nums[right]]
                    if threesum not in res:
                        res.append(threesum)
                    left += 1  
                    right -= 1

            index+=1

        return res