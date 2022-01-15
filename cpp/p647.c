int read4(char* buf4);
/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

#include <stdlib.h>

typedef struct {
    char buf4[4];
    int ptr;
    int tail;
} Solution;

/** initialize your data structure here. */
Solution* solutionCreate() {
    Solution* sol = (Solution*)malloc(sizeof(Solution));
    sol->ptr = 0;
    sol->tail = 0;
    return sol;
}

/**
 * @param buf Destination buffer
 * @param n   Number of characters to read
 * @return    The number of actual characters read
 */
int _read(Solution* obj, char* buf, int n) {
    int ptr = 0;
    while (ptr < n && obj->ptr < obj->tail) {
        buf[ptr] = obj->buf4[obj->ptr];
        obj->ptr++;
        ptr++;
    }

    while (n - ptr >= 4) {
        int ret = read4(buf + ptr);
        ptr += ret;
        if (ret != 4) {
            return ptr;
        }
    }

    if (ptr == n) {
        return ptr;
    }

    obj->ptr = 0;
    obj->tail = read4(obj->buf4);

    while (ptr < n && obj->ptr < obj->tail) {
        buf[ptr] = obj->buf4[obj->ptr];
        obj->ptr++;
        ptr++;
    }

    return ptr;
}