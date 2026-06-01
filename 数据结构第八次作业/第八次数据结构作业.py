#题1：构建BST，从空树开始，依次插入[50,30,70,20,40,60,80]，画出最终BST

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
            return

        cur = self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left = BSTNode(key)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = BSTNode(key)
                    return
                cur = cur.right

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)


# 构建BST
data = [50, 30, 70, 20, 40, 60, 80]

bst = BST()
for x in data:
    bst.insert(x)

print("中序遍历结果：")
bst.inorder(bst.root)
print()

"""
中序遍历结果：
20 30 40 50 60 70 80

中序遍历得到升序序列，说明BST构建正确。
"""





#题2：删除根节点。删除上题中的根节点50，分别用“中序前驱”和“中序后继”两种策略，画出结果。

#中序前驱
def delete_predecessor(root):
    # 找前驱
    parent = root
    pred = root.left

    while pred.right:
        parent = pred
        pred = pred.right

    root.key = pred.key

    if parent == root:
        parent.left = pred.left
    else:
        parent.right = pred.left

    return root


#中序后继
def delete_successor(root):
    # 找后继
    parent = root
    succ = root.right

    while succ.left:
        parent = succ
        succ = succ.left

    root.key = succ.key

    if parent == root:
        parent.right = succ.right
    else:
        parent.left = succ.right

    return root


# ==========================
# 测试前驱删除
# ==========================
data = [50, 30, 70, 20, 40, 60, 80]

bst1 = BST()

for x in data:
    bst1.insert(x)

print("前驱法删除50前：")
bst1.inorder(bst1.root)
print()

bst1.root = delete_predecessor(bst1.root)

print("前驱法删除50后：")
bst1.inorder(bst1.root)
print()


# ==========================
# 测试后继删除
# ==========================
data = [50, 30, 70, 20, 40, 60, 80]

bst2 = BST()

for x in data:
    bst2.insert(x)

print("后继法删除50前：")
bst2.inorder(bst2.root)
print()

bst2.root = delete_successor(bst2.root)

print("后继法删除50后：")
bst2.inorder(bst2.root)
print()



#思考题：两种删除节点的方法能混用吗？

#答：两种删除方法可以混用，因为无论采用中序前驱还是中序后继替换，被删除结点后所得结果仍然满足BST的性质。
#连续删除时根据树的结构灵活选择更好，可以尽量保持树的平衡。
#根据左右子树的高度选择前驱或后继进行替换，尽量删除层数较高的部分，以维持树的平衡。