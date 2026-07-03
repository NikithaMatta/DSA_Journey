class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
            if hashMap[num] > n:
                    return num
        