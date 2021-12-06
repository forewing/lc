int minCostToMoveChips(int* position, int positionSize) {
    int c0 = 0, c1 = 0;
    for (int i = 0; i < positionSize; i++) {
        if (position[i] % 2 == 0) {
            c0++;
        } else {
            c1++;
        }
    }
    return c0 < c1 ? c0 : c1;
}