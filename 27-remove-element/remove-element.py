class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i, v in enumerate(nums):
            if v!=val:
                # Partition
                nums[k]=nums[i]
                k+=1
        return k