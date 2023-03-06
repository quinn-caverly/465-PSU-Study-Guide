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

🟧 https://leetcode.com/problems/flatten-binary-tree-to-linked-list
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

---

🟥 https://leetcode.com/problems/swim-in-rising-water
```python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        '''
        add squares to the binary heap as we find them, pop lowest square and keep moving,
        while keeping track of the highest value in the trail,
        which is essentially the highest value which is visited
        '''

        #these methods return True if we should add element at spot to heap, False else
        def checkAbove(loc) -> bool:
            if loc[0] > 0 and grid[loc[0]-1][loc[1]] != -1:
                return True
            return False

        def checkBelow(loc) -> bool:
            if loc[0] < n-1 and grid[loc[0]+1][loc[1]] != -1:
                return True
            return False

        def checkLeft(loc) -> bool:
            if loc[1] > 0 and grid[loc[0]][loc[1]-1] != -1:
                return True
            return False

        def checkRight(loc) -> bool:
            if loc[1] < n-1 and grid[loc[0]][loc[1]+1] != -1:
                return True
            return False

        heap = [] #of key-value pairs: num and location

        elem = (grid[0][0], [0,0])
        largest = grid[0][0]
        n = len(grid)

        #check top, bottom, left, right elements, set visited elements to -1
        while elem[1] != [n-1,n-1]:
            loc = elem[1]

            if checkAbove(loc) == True:
                heapq.heappush(heap, (grid[loc[0]-1][loc[1]], [loc[0]-1, loc[1]]))
                grid[loc[0]-1][loc[1]] = -1

            if checkBelow(loc) == True:
                heapq.heappush(heap, (grid[loc[0]+1][loc[1]], [loc[0]+1, loc[1]]))
                grid[loc[0]+1][loc[1]] = -1

            if checkLeft(loc) == True:
                heapq.heappush(heap, (grid[loc[0]][loc[1]-1], [loc[0], loc[1]-1]))
                grid[loc[0]][loc[1]-1] = -1

            if checkRight(loc) == True:
                heapq.heappush(heap, (grid[loc[0]][loc[1]+1], [loc[0], loc[1]+1]))
                grid[loc[0]][loc[1]+1] = -1

            elem = heapq.heappop(heap)
            if elem[0] > largest:
                largest = elem[0]

        return largest
```
