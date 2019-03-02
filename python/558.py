"""
When root has 4 subtrees, and all of them are leaf and same value (can only be true), need to reformat the root to leaf and true.
Use setattr and getattr for convenience.
"""
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        def combine(qt1, qt2):
            if (qt1.isLeaf and qt1.val) or (qt2.isLeaf and qt2.val):
                return Node(True, True, None, None, None, None)
            elif qt1.isLeaf and qt2.isLeaf:
                return Node(False, True, None, None, None, None)
            elif qt1.isLeaf:
                return qt2
            elif qt2.isLeaf:
                return qt1
            qt = Node(None, False, None, None, None, None)
            for d in ['topLeft', 'topRight', 'bottomLeft', 'bottomRight']:
                setattr(qt, d, combine(getattr(qt1, d), getattr(qt2, d)))
            if all(getattr(qt, d).isLeaf and getattr(qt, d).val for d in ['topLeft', 'topRight', 'bottomLeft', 'bottomRight']):
                return Node(True, True, None, None, None, None)
            return qt
        
        return combine(quadTree1, quadTree2)
