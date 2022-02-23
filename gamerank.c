#include <stdio.h>

static const short up[26] = {
	[0] = 32767,
	[1 ... 10] = 5,
	[11 ... 15] = 4,
	[16 ... 20] = 3,
	[21 ... 25] = 2,
};

int main() {
	int rank = 25;
	int stars = 0;
	int consecutive = 0;
	int c;
	for (;;) {
		c = getchar();
		if (c == 'W') {
			consecutive++;
			stars += 1 + (rank >= 6 && consecutive >= 3);
			if (stars > up[rank])
				stars -= up[rank], rank--;
			
		} else if (c == 'L') {
			consecutive = 0;
			if (rank >= 1 && rank <= 20)
				stars--;
			if (stars < 0) {
				if (rank == 20)
					stars = 0;
				else
					stars = up[++rank] - 1;
			}
		} else break;
	}
	printf(rank == 0 ? "Legend\n" : "%d\n", rank);
	return 0;
}
