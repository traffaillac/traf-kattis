#include <stdio.h>

int W, L;
char house[420];

static int vert(int c) {
	for (int r = 1; r < L - 1; r++) {
		if (house[r * (W + 1) + c] == '*')
			return r;
	}
	return 0;
}

static int horiz(int r) {
	for (int c = 1; c < W - 1; c++) {
		if (house[r * (W + 1) + c] == '*')
			return c;
	}
	return 0;
}

int main() {
	for (int t = 1; scanf("%d %d ", &W, &L), W > 0; t++) {
		fread(house, (W + 1) * L, 1, stdin);
		int r, c, dr, dc;
		(dr = 0, dc = 1, r = vert(c = 0)) ||
			(dc = -1, r = vert(c = W - 1)) ||
			(dr = 1, dc = 0, c = horiz(r = 0)) ||
			(dr = -1, c = horiz(r = L - 1));
		while (house[r * (W + 1) + c] != 'x') {
			r += dr;
			c += dc;
			if (house[r * (W + 1) + c] == '\\') {
				if (dr == 0)
					dr = dc, dc = 0;
				else
					dc = dr, dr = 0;
			}
			if (house[r * (W + 1) + c] == '/') {
				if (dr == 0)
					dr = -dc, dc = 0;
				else
					dc = -dr, dr = 0;
			}
		}
		house[r * (W + 1) + c] = '&';
		printf("HOUSE %d\n", t);
		fwrite(house, (W + 1) * L, 1, stdout);
	}
	return 0;
}
