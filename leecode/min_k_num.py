import copy


class Solution:

    def getLeastNumbers(self, arr, k):
        # print(arr)
        arr1 = copy.deepcopy(arr)
        arr1.sort()
        print(arr)
        print(arr1)


s = Solution()
arr = [3,2,1]
k = 2
s.getLeastNumbers(arr, k)