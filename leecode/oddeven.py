class Solution:
    def sortArrayByParityII(self, A):
        result = []
        i = 0
        j = 1
        for a in A:
            if a%2 == 0:
                result[i] = a
                i += 2
            else:
                result[j] = a
                j += 2

        return result

A = [4,2,5,7]
s = Solution()
print(s.sortArrayByParityII(A))
