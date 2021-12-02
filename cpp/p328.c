#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* oddEvenList(struct ListNode* head) {
    if (!head || !head->next || !head->next->next) {
        return head;
    }

    struct ListNode* tail = head;
    struct ListNode* head2 = head->next;
    struct ListNode* tail2 = head2;

    for (struct ListNode* ptr = head2->next; ptr; ptr = ptr->next ? ptr->next->next : NULL) {
        tail->next = ptr;
        tail = tail->next;
        tail2->next = ptr->next;
        tail2 = tail2->next;
    }
    tail->next = head2;

    return head;
}