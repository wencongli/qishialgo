/*
Morris traversal: C++
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Postorder Traversal.
Memory Usage: 9.2 MB, less than 87.10% of C++ online submissions for Binary Tree Postorder Traversal.
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        // Morris traversal
        vector<int> ans;
        TreeNode* dummy = new TreeNode(-1);
        dummy->left=root;
        TreeNode* p= dummy;
        while (p){
            if (p->left==nullptr)
                p=p->right;
            else{
                TreeNode *q=p->left;
                while (q->right!=nullptr && q->right!=p)
                    q=q->right;
                if (q->right==nullptr){
                    q->right=p;
                    p=p->left;
                }
                else{
                    //cout<<p->val<<endl;
                    reverse_traversal(p, ans);
                    q->right=nullptr;
                    p=p->right;
                }
            }
        }
        return ans;
        
    }
    
private:
    void reverse_traversal(TreeNode* curr, vector<int> &ans){
        vector<int> temp;
        TreeNode* p;
        p=curr->left;
        while (p && p!=curr){
            temp.push_back(p->val);
            p=p->right;
        }
        reverse(temp.begin(), temp.end());
        int n=temp.size();
        for (int i=0; i<n; i++){
            //std::cout<<temp[i]<<std::endl;
            ans.push_back(temp[i]);
        }
            
            
    }
};
