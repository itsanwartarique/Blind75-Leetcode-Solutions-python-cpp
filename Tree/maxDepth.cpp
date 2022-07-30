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
    // Method 1 : DFS
//     int maxDepth(TreeNode* root) {
        
//         // Base Case
//         if(root == NULL){
//             return 0;
//         }
//         return 1 + max(maxDepth(root->left), maxDepth(root->right));
//     }
    
    // Method 2 : BFS
    int maxDepth(TreeNode* root) {
       
        // Base Case
        if(root == NULL){
            return 0;
        }
        int level = 0;
        queue<TreeNode*>pendingNodes;
        pendingNodes.push(root);
        while(!pendingNodes.empty()){
            int n = pendingNodes.size();
            for(int i = 0; i<n;i++){
              TreeNode* front = pendingNodes.front();
              pendingNodes.pop();
              if(front->left != NULL){
                 pendingNodes.push(front->left);  
              } 
              if(front->right != NULL){
                 pendingNodes.push(front->right);  
              } 
            }
            level++;
        }
        return level;
    }
};