#include <stdlib.h>

struct Node {
    int val;
    struct Node* next;
};

struct Node* insert(struct Node* head, int insertVal) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->val = insertVal;

    if (!head) {
        new_node->next = new_node;
        return new_node;
    }

    struct Node* ptr = head;
    while (ptr->next->val >= ptr->val && ptr->next != head) {
        ptr = ptr->next;
    }

    if (insertVal < ptr->val) {
        while (ptr->next->val < insertVal) {
            ptr = ptr->next;
        }
    }

    new_node->next = ptr->next;
    ptr->next = new_node;

    return head;
}