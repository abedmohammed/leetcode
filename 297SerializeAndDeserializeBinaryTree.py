class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        res = []

        def preOrder(root):
            if not root:
                res.append("N")
                return

            res.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        return ",".join(res) 
        

    def deserialize(self, data):
        preOrder = data.split(",")
        self.i = 0

        def buildTree():
            if preOrder[self.i] == "N": 
                self.i += 1
                return None

            root = TreeNode(preOrder[self.i])

            self.i += 1
            root.left = buildTree()
            root.right = buildTree()

            return root
        
        return buildTree()
    
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(3, node4, node5)
node1 = TreeNode(1, node2, node3)

ser = Codec()
deser = Codec()
ans = ser.serialize(node1)
print(ans)
ans = deser.deserialize(ans)
print(ans.val)
print(ans.left.val)
print(ans.right.val)
print(ans.right.left.val)
print(ans.right.right.val)