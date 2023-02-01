
🟥 Uses adjacency list: https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even

```python
class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        #generate standard adjacency list for simple, undirected graph
        adjacency_list = {x: [] for x in range(1, n+1)}
        
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        #collects nodes which have an odd degree
        odd_adjacency_list = dict(filter(lambda x: len(x[1])%2!=0, adjacency_list.items()))
        
        size = len(odd_adjacency_list)

        if size==0:
            return True

        elif size in [2,4]:
            key_list = list(odd_adjacency_list.keys())
            a, b = key_list[0], key_list[1]               

            if size==2: #either we connect to each other, or we connect both to a node which was originally even
                if a not in odd_adjacency_list[b] and b not in odd_adjacency_list[a]:
                    return True
                for key, value in adjacency_list.items():
                    if a not in value and b not in value:
                        return True              

            else: #because we are only allowed 2 extra edges, they have to connect to each other somehow, 3 possiblities
                c, d = key_list[2], key_list[3]
                
                canBeValid = lambda a, b: a not in odd_adjacency_list[b] and b not in odd_adjacency_list[a]

                if canBeValid(a, b) and canBeValid(c, d):
                    return True
                elif canBeValid(a, c) and canBeValid(b, d):
                    return True
                elif canBeValid(a, d) and canBeValid(b, c):
                    return True

        return False
```
---
