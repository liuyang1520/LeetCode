# Edge case "0", "0" -> "00"
# If the first element is not "0" (the largest one), then should be fine, else return "0"
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        numsString = [str(i) for i in nums]
        for i in range(len(numsString) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if numsString[i] + numsString[j] > numsString[j] + numsString[i]:
                    numsString[i], numsString[j] = numsString[j], numsString[i]
        return "".join(numsString) if numsString[0] != "0" else "0"
