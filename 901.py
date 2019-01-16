"""
Use a stack to keep tracking the previous aggregated data
"""
class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            _, prev = self.stack.pop()
            count += prev
        self.stack.append((price, count))
        return count
