🟩Trivial memoization application: https://leetcode.com/problems/fibonacci-number
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        dp = {0: 0, 1: 1}
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
```
(A more python version of the same solution)

```python
class Solution:
    def fib(self, n: int) -> int:
        @cache
        def fib(n):
            if n==0 or n==1:
                return n
            return fib(n-1) + fib(n-2)

        return fib(n)
```
