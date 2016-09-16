"""
https://www.hrwhisper.me/leetcode-contains-duplicate-i-ii-iii/
Imagine there is an axis divided by length of t + 1, each segment can be treated as a bucket.
There will be k numbers stored in the buckets at the same time (k + 1 will replace 1).
The trick part is that we just need to confirm whether two numbers fall in the same bucket or the number in the next bucket is closer than t.
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) < 2 or t < 0:
            return False
        axis_bucket = {}
        for i in range(len(nums)):
            index = nums[i] / (t + 1)
            if (index in axis_bucket) or ((index-1) in axis_bucket and abs(nums[i] - axis_bucket[index-1]) <= t) \
                or ((index+1) in axis_bucket and abs(nums[i] - axis_bucket[index+1]) <= t):
                    return True
            axis_bucket[index] = nums[i]
            if i >= k:
                axis_bucket.pop(nums[i-k] / (t + 1))
        return False


"""
Using balanced binary search tree, like AVL, red-black tree.
In C++:
set, multiset, map, multimap all use red-black tree to search, delete, add in O(logn)
hashmap best case O(1), worst case O(n)
abs(nums[i] - nums[j]) <= t
nums[j] - t <= nums[i] <= nums[j] + t
The tree maintains k elements in it, if any pair satisfied the condition, should return True.

C++ code:
"""
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        multiset<int> query_window;
        for(int i = 0; i < nums.size(); i++) {
            auto minValue = query_window.lower_bound(nums[i] - t);
            if (minValue != query_window.end() && *minValue - nums[i] <= t)
                return true;
            query_window.insert(nums[i]);
            if (i >= k)
                query_window.erase(nums[i-k]);
        }
        return false;
    }
};












