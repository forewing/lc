class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def solve(n, s):
    head = Node(s[0])
    tail = head
    for i in range(1, len(s)):
        tail.next = Node(s[i])
        tail = tail.next

    edited = True
    while edited:
        edited = False
        for j in range(10):
            target = str(j) + str((j + 1) % 10)
            ptr = head
            while ptr and ptr.next:
                if ptr.val == target[0] and ptr.next.val == target[1]:
                    edited = True
                    ptr.val = str((j + 2) % 10)
                    ptr.next = ptr.next.next
                ptr = ptr.next

        # ptr = head
        # while ptr and ptr.next:
        #     for j in range(10):
        #         if not ptr.next:
        #             break
        #         com = ptr.val + ptr.next.val
        #         target = str(j) + str((j + 1) % 10)
        #         if com == target:
        #             edited = True
        #             ptr.val = str((j + 2) % 10)
        #             ptr.next = ptr.next.next
        #             break
        #     ptr = ptr.next
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return "".join(ans)


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        s = input()
        print(f"Case #{i+1}: {solve(n, s)}")
