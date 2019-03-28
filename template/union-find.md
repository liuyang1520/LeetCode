### Python
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
