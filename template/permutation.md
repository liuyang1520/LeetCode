### Python
#### itertools
```python
import itertools
list(itertools.permutations(array)
```

#### Generate list directly
```python
def permutation(array):
    res = []
    if not array: return [[]]
    for i in range(len(array)):
        for t in permutation(array[:i] + array[i+1:]):
            res.append(array[i:i+1] + t)
    return res
```

#### yield
```python
def permutation(array):
    if len(array) <=1:
        yield array
    else:
        for t in permutation(array[1:]):
            for i in range(len(array)):
                yield t[:i] + array[0:1] + t[i:]
```
