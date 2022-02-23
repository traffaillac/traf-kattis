#include <stdio.h>

int distinct[42];

int main() {
	for (int n = 0, i; n < 10; n++) {
		scanf("%d", &i);
		distinct[i % 42] = 1;
	}
	int sum = 0;
	for (int n = 0; n < 42; n++)
		sum += distinct[n];
	printf("%d\n", sum);
}
