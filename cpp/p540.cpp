#include <vector>
using std::vector;

class Solution {
   public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();

        if (n == 1) {
            return nums[0];
        } else if (nums[0] != nums[1]) {
            return nums[0];
        } else if (nums[n - 1] != nums[n - 2]) {
            return nums[n - 1];
        }

        int l = 0;
        int r = n;

        while (l < r) {
            int m = (l + r) / 2;
            if (nums[m * 2] == nums[m * 2 + 1]) {
                l = m;
            } else if (nums[m * 2] == nums[m * 2 - 1]) {
                r = m;
            } else {
                return nums[m * 2];
            }
        }
        return nums[l * 2];
    }
};