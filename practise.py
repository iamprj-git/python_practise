
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

def print_fun(listw):
    if listw is not None:
        print("Solution exists:")
        result = "List index {} + List index {} = 9".format(listw[0], listw[1])
        print(result)
    else:
        print("No such numbers found")

listw = [-1, -1]
x = Solution()
result = x.twoSum([4, 5, 4, 6], 9)
print_fun(result)
print("code sucessfully executed:")
