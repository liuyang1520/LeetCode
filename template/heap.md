### Python
#### heapq
##### k smallest values
```python
data = [...]
heapq.heapify(data)
[heapq.heappop(heap) for _ in xrange(k)]
```

```python
heapq.nsmallest(k, data, key=lambda x: x)
```
