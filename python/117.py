# BFS solution, using 2 queues, one for next layer, one for current layer
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            queue = [root]
        else:
            queue = []
        queueLayer = []
        while queue:
            cur = queue.pop()
            if cur.left:
                queueLayer.insert(0, cur.left)
            if cur.right:
                queueLayer.insert(0, cur.right)
            if not queue:
                cur.next = None
                queue = queueLayer
                queueLayer = []
            else:
                cur.next = queue[-1]


# Find a nice implementation here: http://chaoren.is-programmer.com/posts/43820.html
# Core idea: build the "next" linked list of next layer when doing traversal in current layer.
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        cur = root
        while cur:
            starterNextLayer = None
            temp = None
            while cur:
                if not starterNextLayer:
                    if cur.left:
                        starterNextLayer = cur.left
                    elif cur.right:
                        starterNextLayer = cur.right
                if cur.left:
                    if temp:
                        temp.next = cur.left
                    temp = cur.left
                if cur.right:
                    if temp:
                        temp.next = cur.right
                    temp = cur.right
                cur = cur.next
            cur = starterNextLayer