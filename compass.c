#include <stdio.h>

int main() {
	int n1, n2;
	scanf("%d %d", &n1, &n2);
	int cw = (unsigned)(n2 - n1 + 360) % 360;
	int ccw = (unsigned)(n1 - n2 + 360) % 360;
	printf("%d\n", cw <= ccw ? cw : -ccw);
	return 0;
}
