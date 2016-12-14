#include <stdlib.h>
#include <string.h>

struct Node {
  int value;
  struct Node *next;
};

struct Node *counter_effect(const char *hit_count, size_t *p_result_count) {
  *p_result_count = 0;

  const size_t count = strlen(hit_count);
  struct Node *nodes = (struct Node*)malloc(sizeof(struct Node) * count);
  if (nodes) 
  {
    *p_result_count = count;

    for (size_t index = 0; index < count; ++index) 
    {
      struct Node *node = &nodes[index];
      const int endInclusive = hit_count[index] - '0';
      
      for (int value = 0; value <= endInclusive; ++value) 
      {
        node->value = value;
        
        if (value < endInclusive) {
          node->next = (struct Node*)malloc(sizeof(struct Node));
        } else {
          node->next = NULL;
        }
        node = node->next;
      }
    }
  }
  return nodes;
}