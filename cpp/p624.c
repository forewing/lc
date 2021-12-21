const int MAX = 10001;

int maxDistance(int** arrays, int arraysSize, int* arraysColSize) {
    int l1 = arrays[0][arraysColSize[0] - 1], pl1 = 0;
    int l2 = -MAX, pl2 = -1;
    int s1 = arrays[0][0], ps1 = 0;
    int s2 = MAX, ps2 = -1;

    for (int i = 1; i < arraysSize; i++) {
        int l = arrays[i][arraysColSize[i] - 1];
        int s = arrays[i][0];
        if (l > l1) {
            l2 = l1;
            pl2 = pl1;
            l1 = l;
            pl1 = i;
        } else if (l > l2) {
            l2 = l;
            pl2 = i;
        }
        if (s < s1) {
            s2 = s1;
            ps2 = ps1;
            s1 = s;
            ps1 = i;
        } else if (s < s2) {
            s2 = s;
            ps2 = i;
        }
    }

    if (pl1 != ps1) {
        return l1 - s1;
    }

    return (l1 - s2 > l2 - s1) ? (l1 - s2) : (l2 - s1);
}