#include <stdio.h>

int main() {
	int y;
	scanf("%d", &y);
	int bits = 4 << ((y - 1960) / 10);
	printf("%d\n", bits);
}
