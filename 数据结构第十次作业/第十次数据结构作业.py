class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []          # 关键字
        self.children = []      # 孩子
        self.leaf = leaf

    def __str__(self):
        return str(self.keys)


class BTree:
    def __init__(self, m=3):
        self.m = m
        self.max_keys = m - 1   # 3阶B树最多2个关键字
        self.root = BTreeNode()

    def insert(self, key):
        root = self.root

        self._insert(root, key)

        # 根结点上溢
        if len(root.keys) > self.max_keys:
            self._split_root()

    def _insert(self, node, key):

        # 叶子结点直接插入
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
            return

        # 找插入位置
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        child = node.children[i]

        self._insert(child, key)

        # 子结点上溢
        if len(child.keys) > self.max_keys:
            self._split_child(node, i)

    def _split_child(self, parent, index):

        child = parent.children[index]

        # child有3个关键字
        # [k0, k1, k2]
        mid = 1
        promote = child.keys[mid]

        left = BTreeNode(child.leaf)
        right = BTreeNode(child.leaf)

        left.keys = [child.keys[0]]
        right.keys = [child.keys[2]]

        if not child.leaf:
            left.children = child.children[:2]
            right.children = child.children[2:]

        parent.keys.insert(index, promote)

        parent.children[index] = left
        parent.children.insert(index + 1, right)

    def _split_root(self):

        old_root = self.root

        mid = 1
        promote = old_root.keys[mid]

        left = BTreeNode(old_root.leaf)
        right = BTreeNode(old_root.leaf)

        left.keys = [old_root.keys[0]]
        right.keys = [old_root.keys[2]]

        if not old_root.leaf:
            left.children = old_root.children[:2]
            right.children = old_root.children[2:]

        new_root = BTreeNode(False)

        new_root.keys = [promote]
        new_root.children = [left, right]

        self.root = new_root

    def print_tree(self, node=None, level=0):

        if node is None:
            node = self.root

        print("    " * level +
              f"keys={node.keys}, children={len(node.children)}")

        for child in node.children:
            self.print_tree(child, level + 1)

    def draw(self, node=None, level=0):

        if node is None:
            node = self.root

        print("    " * level + str(node.keys))

        for child in node.children:
            self.draw(child, level + 1)


# =====================
# 测试
# =====================

data = [10, 20, 5, 6, 12, 30, 25]

bt = BTree(3)

for x in data:
    bt.insert(x)

print("树结构：")
bt.print_tree()

print("\n简图：")
bt.draw()