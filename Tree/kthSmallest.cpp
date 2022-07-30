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
    int kthSmallest(TreeNode* root, int k) {
        if(root == NULL) return -1;
        
        inOrder(root);
        return temp[k-1];
    }
    TreeNode* inOrder(TreeNode* root){
        if(root == NULL) return root;
        TreeNode* left = inOrder(root->left);
        temp.push_back(root->val);
        TreeNode* right = inOrder(root->right);
        return root;
    }   
};