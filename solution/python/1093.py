"""
@difficulty: medium
@tags: misc
@notes: Basic statistic calculations. 
"""
class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        minimum, maximum, mean, median, mode = [255, 0, 0, 0, 0]
        _count, _modeCount = 0, 0
        for i, val in enumerate(count):
            if val > 0 and i < minimum:
                minimum = i
            if val > 0 and i > maximum:
                maximum = i
            if val > _modeCount:
                mode = i
                _modeCount = val
            if val > 0:
                mean = float(mean * _count + val * i) / (_count + val)
                _count += val
        _medianCount = _count / 2.0
        _tempCount = 0
        for i in range(0, len(count) - 1):
            _tempCount += count[i]
            if _tempCount == _medianCount:
                median = (i + i + 1) / 2.0
                break
            if _tempCount < _medianCount and _tempCount + count[i+1] > _medianCount:
                median = i + 1
                break
        return map(float, [minimum, maximum, mean, median, mode])
