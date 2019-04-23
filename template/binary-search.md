### Python
#### Standard, return index which value == target
```python
def bs(sortedArray, target):
    left, right = 0, len(sortedArray)
    while left <= right:
        mid = (left + right) / 2
        if sortedArray[mid] == target:
            return mid
        elif sortedArray[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
```

#### Rightmost, return max-index which value <= target, when duplicates or non-exact matching
```python
def bs(sortedArray, target):
    left, right = 0, len(sortedArray)
    while left < right:
        mid = (left + right) / 2
        if sortedArray[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left - 1
```

#### Leftmost, return min-index which value >= target, when duplicates or non-exact matching
```python
def bs(sortedArray, target):
    left, right = 0, len(sortedArray)
    while left < right:
        mid = (left + right) / 2
        if sortedArray[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```
