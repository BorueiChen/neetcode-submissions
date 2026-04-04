# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []

        def dfs(node):
            if not node:
                self.res.append("N")
                return
            
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(self.res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.idx = 0
        data = data.split(',')

        def dfs():
            if data[self.idx] == 'N':
                self.idx += 1
                return None
            
            node = TreeNode(data[self.idx])
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))