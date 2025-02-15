# Run complexity: O(n^3)
# Space complexity: O(k) where k is the number of quads that sum to target
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad_sum_target = []
        i1 = 0
        while i1 < len(nums):
            # a, b, c, d must be distinct
            i2  = i1 + 1
            while i2 < len(nums):
                # a, b, c, d must be distinct
                l, r = i2 + 1, len(nums) - 1
                while l < r:
                    quad_sum = nums[i1] + nums[i2] + nums[l] + nums[r]
                    if  quad_sum == target:
                        quad_sum_target.append([nums[i1], nums[i2], nums[l], nums[r]])
                        l += 1
                        # Keep adding to l until get next number
                        while nums[l] ==  nums[l - 1] and l < r:
                            l += 1
                    elif quad_sum > target:
                        r -= 1
                    else:
                        l += 1
                i2 += 1
                # Keep adding to i2 until get next number
                while i2 < len(nums) and nums[i2] == nums[i2 - 1]:
                    i2 += 1
            i1 += 1
            # Keep adding to i2 until get next number
            while i1 < len(nums) - 1 and nums[i1] == nums[i1 - 1]:
                    i1 += 1
        return quad_sum_target
