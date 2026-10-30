int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    if (root == NULL) return NULL;
    int* result = (int*)malloc(100 * sizeof(int));
    struct TreeNode** stack = (struct TreeNode**)malloc(100 * sizeof(struct TreeNode*));
    int capacity = 100;
    int top = -1;
    
    struct TreeNode* curr = root;
    
    while (curr != NULL || top != -1) {
        while (curr != NULL) {
            stack[++top] = curr;
            curr = curr->left;
        }
        curr = stack[top--];
        if (*returnSize >= capacity) {
            capacity *= 2;
            result = (int*)realloc(result, capacity * sizeof(int));
        }
        
        result[(*returnSize)++] = curr->val;
        curr = curr->right;
    }
    
    free(stack);
    return result;
}