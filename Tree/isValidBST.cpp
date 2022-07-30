/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int>temp;
    bool isValidBST(TreeNode* root) {
       
        if(root == NULL) return true;
        inOrder(root);
        int n = temp.size();
        for(int i =0,j=1; j<n;j++,i++){
            if(temp[i]>=temp[j]) return false;
        }
        return true;
    }
    TreeNode* inOrder(TreeNode* root){
        if(root == NULL) return root;
        inOrder(root->left);
        temp.push_back(root->val);
        inOrder(root->right);
        return root; 
    }  
};