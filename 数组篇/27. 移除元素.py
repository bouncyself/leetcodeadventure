'''
给你一个数组 nums和一个值 val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index, res, len_num = len(nums)-1, len(nums)-1, len(nums)
        while index!=-1:
            if nums[index] == val:
                nums[index],nums[res] = nums[res], nums[index]
                res -= 1

            index-=1
        return res+1




if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([0,1,2,2,3,0,4,2],2))

