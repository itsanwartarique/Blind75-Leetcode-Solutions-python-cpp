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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
         if(head== NULL || n==0){
            return NULL;
        }
        int count =0;
        ListNode* temp = head;
        while(temp != NULL){
            count += 1;
            temp=temp->next;
        }
        int i =0;
        temp =head;
        while(i<count-n-1){
            temp = temp->next;
            i++;
        }
        cout<<temp->val;
        if(temp == head && temp->next !=NULL){ 
           return head->next;
        }
        temp->next = temp->next->next;
        return head;
    }
};