#include <stdio.h>
#include <string.h>

int main() {
	char maze[200][128], rows[200], cols[128];
	int T;
	scanf("%d\n", &T);
	printf("%d\n", T);
	while (T--) {
		memset(maze, '#', sizeof(maze));
		memset(rows, 0, sizeof(rows));
		memset(cols, 0, sizeof(cols));
		int x = 0, y = 100, dir = 0, c; // clockwise
		while ((c = getchar()) != '\n') {
			maze[y][x] = '.';
			rows[y] = 1;
			cols[x] = 1;
			switch (c) {
				case 'L': dir = (dir - 1) & 3; break;
				case 'R': dir = (dir + 1) & 3; break;
				case 'B': dir ^= 2; break;
			}
			switch (dir) {
				case 0: x++; break;
				case 1: y++; break;
				case 2: x--; break;
				case 3: y--; break;
			}
		}
		int y0 = 0, y1 = 199, x0 = 0, x1 = 99;
		while (rows[y0] == 0)
			y0++;
		while (rows[y1] == 0)
			y1--;
		while (cols[x0] == 0)
			x0++;
		while (cols[x1] == 0)
			x1--;
		printf("%d %d\n", y1 - y0 + 3, x1 - x0 + 2);
		for (y = y0 - 1; y <= y1 + 1; y++) {
			maze[y][x1 + 2] = 0;
			puts(maze[y]);
		}
	}
}
