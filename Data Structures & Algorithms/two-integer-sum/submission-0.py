class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range (len(nums)):
            addend = target - nums[i]
            if seen and addend in seen:
                index = seen[addend]
                smallest = min(i, index)
                largest = max(i, index)
                return [smallest, largest]
            else:
                seen[nums[i]] = i

        return[]