from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i,x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i

if __name__ == "__main__":
    str = input()
    left = str.split(", target = ")[0]
    target = int(str.split(", target = ")[1])
    nums = eval(left.split()[2])
    print(twoSum(nums, target))

# ============================================================
# LeetCode 提交版本（复制以下代码到 LeetCode 提交窗口）:
# ============================================================
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]