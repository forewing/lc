#include <stdbool.h>

const int MASKS[6] = {
    0b00000000, 0b10000000, 0b11000000, 0b11100000, 0b11110000, 0b11111000,
};

bool validUtf8(int* data, int dataSize) {
    int remain = 0;
    for (int i = 0; i < dataSize; i++) {
        int ones = -1;
        for (int j = 0; j <= 4; j++) {
            if ((data[i] & MASKS[j + 1]) == MASKS[j]) {
                ones = j;
                break;
            }
        }
        if (ones == -1) {
            return false;
        }

        if (remain != 0) {
            if (ones == 1) {
                remain--;
            } else {
                return false;
            }
        } else if (ones == 0) {
            remain = 0;
        } else if (ones == 1) {
            return false;
        } else {
            remain = ones - 1;
        }
    }

    return remain == 0;
}
