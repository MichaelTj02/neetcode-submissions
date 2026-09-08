/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // ListNode* prev;
        
        // while (head != nullptr) {
        //     temp = head;

        // }

        ListNode* reversed = nullptr;
        while (head != nullptr) {
            ListNode* temp = head->next;
            reversed = new ListNode(head->val, reversed);
            head = head->next;
        }

        return reversed;
    }
};
