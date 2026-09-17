class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        o = set()
        for num in nums:
            if num in o:
                return True
            else:
                o.add(num)
                
        return False
        