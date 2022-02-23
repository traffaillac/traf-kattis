#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * Base functions to manage a priority queue. O(log n)
 */
static int Heap_push(short* heap, int num, int key) {
	int lo = num++;
	int hi;
	while ((hi = (lo - 1) >> 1) >= 0 && key > heap[hi]) {
		heap[lo] = heap[hi];
		lo = hi;
	}
	heap[lo] = key;
	return num;
}
static int Heap_pop(short* heap, int num) {
	num--;
	int hi = 0;
	int lo;
	while ((lo = hi * 2 + 1) < num) {
		lo += lo + 1 < num && heap[lo + 1] > heap[lo];
		if (heap[num] > heap[lo])
			break;
		heap[hi] = heap[lo];
		hi = lo;
	}
	heap[hi] = heap[num];
	return num;
}
static void Heap_debug(short* heap, int num) {
	putchar('[');
	for (int i = 0; i < num; i++)
		printf("%d%c", heap[i], i < num - 1 ? ' ' : ']');
}

static inline int min(int a, int b) { return a < b ? a : b; }
static inline int max(int a, int b) { return a > b ? a : b; }



int main() {
	short array[2048];
	short heap_lo[2048];
	short heap_hi[2048];
	int error[2048];
	int best[26][2048];
	int N, K;
	scanf("%d %d", &N, &K);
	for (int n = 0; n < N; n++)
		scanf("%hd", &array[n]);
	
	for (int k = 1; k <= K; k++)
		best[k][1] = 0;
	for (int n = 2; n <= N; n++) {
		error[n - 1] = 0;
		error[n - 2] = abs(array[n - 1] - array[n - 2]);
		int num_lo = Heap_push(heap_lo, 0, min(array[n - 1], array[n - 2]));
		int num_hi = Heap_push(heap_hi, 0, -max(array[n - 1], array[n - 2]));
		int sum_lo = heap_lo[0];
		int sum_hi = -heap_hi[0];
		for (int i = n - 3; i >= 0; i--) {
			int median = array[i];
			if (median < heap_lo[0]) {
				sum_lo += median - heap_lo[0];
				num_lo = Heap_push(heap_lo, num_lo, median);
				median = heap_lo[0];
				num_lo = Heap_pop(heap_lo, num_lo);
			} else if (median > -heap_hi[0]) {
				sum_hi += median + heap_hi[0];
				num_hi = Heap_push(heap_hi, num_hi, -median);
				median = -heap_hi[0];
				num_hi = Heap_pop(heap_hi, num_hi);
			}
			error[i] = median * (num_lo - num_hi) - sum_lo + sum_hi;
			if (num_lo < num_hi) {
				num_lo = Heap_push(heap_lo, num_lo, median);
				sum_lo += median;
			} else {
				num_hi = Heap_push(heap_hi, num_hi, -median);
				sum_hi += median;
			}
		}
		
		best[1][n] = error[0];
		for (int k = 2; k <= K; k++) {
			int dst = INT_MAX;
			for (int i = n - 1; i > 0; i--)
				dst = min(dst, best[k - 1][i] + error[i]);
			best[k][n] = dst;
		}
	}
	
	printf("%d\n", best[K][N]);
}
