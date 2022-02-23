#include <stdio.h>

static int numbers[16] = {1};

int main() {
    int full = 3, top = 1, bottom = 1;
    for (int n = 1; n <= 15; n++) {
        numbers[n] = full;
        int l = full;
        full = 3 * l + top + bottom;
        top = l + top;
        bottom = l + bottom;
    }
    int n;
    while (scanf("%d", &n), n >= 0)
        printf("%d\n", n & 1 ? 0 : numbers[n >> 1]);
}
