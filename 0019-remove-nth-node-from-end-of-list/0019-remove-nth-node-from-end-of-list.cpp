class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = 1; 
        ListNode *curr = head;

        while(curr->next) {
            curr = curr->next;
            length++;
        }

        int a = length - n;
        if(a == 0) {
            return head->next;
        }

        curr = head;
        int k = 1;
        while (k < a) {
            curr = curr->next;
            k++;
        }

        curr->next = curr->next->next;
        return head;
    }
};
