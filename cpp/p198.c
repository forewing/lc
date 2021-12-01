inline int max(int a, int b) {
    return a > b ? a : b;
}

int rob(int* nums, int numsSize) {
    if (numsSize == 1) {
        return nums[0];
    }

    int dp0 = nums[0];
    int dp1 = max(nums[0], nums[1]);

    for (int i = 2; i < numsSize; i++) {
        int t = dp1;
        dp1 = max(dp0 + nums[i], t);
        dp0 = t;
    }

    return dp1;
}