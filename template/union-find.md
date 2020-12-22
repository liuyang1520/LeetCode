### Python
#### Dict
```python
# define
f = {}
def find(x):
    f.setdefault(x, x)
    if x != f[x]:
        f[x] = find(f[x])
    return f[x]
def union(x, y):
    f[find(x)] = find(y)
    
# update
pass

# result
len(set(map(find, f)))
```

#### List
```python
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
```
