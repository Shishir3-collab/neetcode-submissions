class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)
        while low<high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                low = mid+1
            else:
                high = mid
        return -1
