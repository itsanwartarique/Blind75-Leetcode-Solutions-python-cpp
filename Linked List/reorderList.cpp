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
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        ListNode* list1;
        ListNode* list2;
        //find middle 
        while(fast != NULL && fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        list1 = head;
        list2 = slow->next;
        slow->next = NULL;
        //reverse list2
        list2 = reverseList(list2);
        
        //merge list1 and list 2;
        merge(list1,list2);
        
    }
    ListNode* reverseList(ListNode* head){
        //base case
        if(head == NULL || head->next == NULL){
            return head;
        }
        //recursive calll
        ListNode* smallAns = reverseList(head->next);
        //small calculation
        ListNode* temp = smallAns;
        while(temp->next != NULL){
            temp = temp->next;
        }
        temp->next = head;
        head->next = NULL;
        return smallAns;  
    }
    ListNode* merge(ListNode* list1, ListNode* list2){
        ListNode* dummy = new ListNode(-1,list1);
        while((list1 != NULL) && (list2 !=NULL)){
            ListNode* temp1 = list1->next;
            ListNode* temp2 = list2->next;
            list1->next = list2;
            list2->next = temp1;
            
            list1 = temp1;
            list2 = temp2;
        }
        if(list2 != NULL){
            list1->next = list2;
        }
        return dummy->next;
    }
};