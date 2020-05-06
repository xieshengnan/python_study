class Solution:
    def repeat_num(self, nums, n):

        set1 = set()
        for i in nums:
            if i in set1:
                print(i)
            else:
                set1.add(i)


nums = [2, 3, 1, 0, 2, 5, 3]
s = Solution()
s.repeat_num(nums, 7)
