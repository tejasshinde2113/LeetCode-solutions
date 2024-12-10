from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                p1, p2 = j + 1, len(nums) - 1
                while p1 < p2:
                    curr_sum = nums[i] + nums[j] + nums[p1] + nums[p2]
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[p1], nums[p2]])
                        p1 += 1
                        p2 -= 1
                        # Skip over duplicates for p1
                        while p1 < p2 and nums[p1] == nums[p1 - 1]:
                            p1 += 1
                        # Skip over duplicates for p2
                        while p1 < p2 and nums[p2] == nums[p2 + 1]:
                            p2 -= 1
                    elif curr_sum < target:
                        p1 += 1
                    else:
                        p2 -= 1

        return res

       