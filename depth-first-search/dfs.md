https://leetcode.com/problems/validate-binary-search-tree

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if node == None:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            if not dfs(node.left, lower, node.val):
                return False
            if not dfs(node.right, node.val, upper):
                return False

            return True
            
        return dfs(root)
```
