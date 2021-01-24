```python
class FenwickTree(object):
    def __init__(self, size):
        self.nodes = [0] * (size+1)
        self.size = size
        
    def lowbit(self, x):
        return x & -x
        
    def add(self, x, value):
        while x <= self.size:
            self.nodes[x] += value
            x += self.lowbit(x)
        
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.nodes[x]
            x -= self.lowbit(x)
        return res
```
