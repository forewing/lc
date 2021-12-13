int maxPower(char* s) {
    int ans = 0, cur = 1;
    char l = *s;
    s++;
    for (; *s != '\0'; s++) {
        if (*s == l) {
            cur++;
        } else {
            if (cur > ans) {
                ans = cur;
            }
            cur = 1;
        }
        l = *s;
    }
    if (cur > ans) {
        ans = cur;
    }
    return ans;
}