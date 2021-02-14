#include <search.h>
#include <stdint.h>
#include <stdio.h>

static struct Cat {
	int priority;
	char name[16];
} cats[200000];

// tsearch API is incomplete, you have to dig inside to make it useful
struct node_t {
	struct Cat* cat;
	uintptr_t left_node;
	uintptr_t right_node;
};

static inline int comp(const void *a, const void *b) {
	return ((struct Cat*)a)->priority - ((struct Cat*)b)->priority;
}

int main() {
	void *root = NULL;
	char name[16];
	int N, comm, lvl, order=0;
	hcreate(250000);
	scanf("%d", &N);
	for (int i=0; i<N; i++) {
		scanf("%d", &comm);
		if (comm == 0) {
			scanf("%s%d", cats[order].name, &lvl);
			cats[order].priority = (100 - lvl) * 200000 + order;
			tsearch(&cats[order], &root, comp);
			hsearch((ENTRY){cats[order].name, &cats[order]}, ENTER);
			order++;
		} else if (comm == 1) {
			scanf("%s%d", name, &lvl);
			struct Cat* cat = hsearch((ENTRY){name, NULL}, FIND)->data;
			tdelete(cat, &root, comp);
			cat->priority -= lvl * 200000;
			tsearch(cat, &root, comp);
		} else if (comm == 2) {
			scanf("%s", name);
			struct Cat* cat = hsearch((ENTRY){name, NULL}, FIND)->data;
			tdelete(cat, &root, comp);
		} else {
			if (root == NULL) {
				puts("The clinic is empty");
			} else {
				struct node_t* n = root;
				while (n->left_node > 1)
					n = (struct node_t*)(n->left_node & ~(uintptr_t)1);
				puts(n->cat->name);
			}
		}
	}
}
