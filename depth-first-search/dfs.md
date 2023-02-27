🟧 https://leetcode.com/problems/validate-binary-search-tree

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

---

🟧 https://leetcode.com/problems/path-sum-ii
```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        output_array = []

        def dfs(node, path):
            path = path.copy()
            path.append(node.val)

            if node.left == None and node.right == None:
                print(path)
                if sum(path) == targetSum:
                    nonlocal output_array
                    output_array.append(path)
            
            if node.left != None:
                dfs(node.left, path)

            if node.right != None:
                dfs(node.right, path)

        
        if root == None:
            return []

        dfs(root, [])

        return output_array
```

---

🟧 https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # take left child of the node, put it in the right position
        # then, put the previous right node as the right child of the rightmost node of original left child
        def flop(node):
            if node == None: return

            if node.left != None:
                rightPointer = node.right
                node.right = node.left

                cur = node.right
                while cur.right != None:
                    cur = cur.right

                cur.right = rightPointer
                node.left = None

            flop(node.right)

        flop(root)
```
