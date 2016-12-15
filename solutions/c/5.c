#include <stdlib.h>

unsigned long long get_currently_allocated_size(void);

void *mem_alloc(size_t size);

void mem_free(void*);

struct Node {
  void *data;
  size_t dataSize;
  struct Node *next;
} *mem_root = NULL;

unsigned long long mem_alloc_count = 0;

unsigned long long get_currently_allocated_size(void) {
  return mem_alloc_count;
}

void *mem_alloc(size_t size) {
  void *mem = malloc(size);
  if (mem) {
  	struct Node *mem_node = (struct Node*)malloc(sizeof(struct Node));
  	if (!mem_node) {
  	  free(mem); mem = NULL;
  	} else {
  	  mem_alloc_count += size;
  	  mem_node->data = mem;
  	  mem_node->dataSize = size;
  	  mem_node->next = mem_root;
  	  mem_root = mem_node;
  	}
  }
  return mem;
}

void mem_free(void* ptr) {
  if (ptr) 
  {
  	struct Node dummy = { .next = mem_root };
  	
  	struct Node *slow, *fast;
  	slow = &dummy;
  	fast = mem_root;
  
  	while (fast && fast->data != ptr) {	  
  	  slow = slow->next; 
  	  fast = fast->next;
  	}
  	
  	if (fast && fast->data == ptr) {
  	  mem_alloc_count -= fast->dataSize;
  	  slow->next = fast->next;
      free(fast->data);
      free(fast);
  	}
  }
}
