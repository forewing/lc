const long long MAX_POS = ((long long)1 << 31) - 1;
const long long MAX_NEG = (long long)1 << 31;

int myAtoi(char* s) {
    while (*s == ' ') {
        s++;
    }
    int sign = 1;
    if (*s == '-') {
        sign = -1;
        s++;
    } else if (*s == '+') {
        s++;
    }

    long long num = 0;
    for (; *s >= '0' && *s <= '9'; s++) {
        num *= 10;
        num += *s - '0';
        if ((sign == 1 && num >= MAX_POS) || (sign == -1 && num >= MAX_NEG)) {
            return sign == 1 ? MAX_POS : -MAX_NEG;
        }
    }
    return num * sign;
}