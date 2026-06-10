import heapq


class MedianFinder:
    def __init__(self):
        """
        left  : 大顶堆（使用负数实现）
        right : 小顶堆
        """
        self.left = []
        self.right = []

    def addNum(self, num):
        """
        添加一个数字
        时间复杂度：O(log n)
        """

        # 先放入大顶堆
        heapq.heappush(self.left, -num)

        # 将大顶堆最大值移到小顶堆
        heapq.heappush(
            self.right,
            -heapq.heappop(self.left)
        )

        # 保持左堆元素数 >= 右堆元素数
        if len(self.right) > len(self.left):
            heapq.heappush(
                self.left,
                -heapq.heappop(self.right)
            )

    def findMedian(self):
        """
        返回当前中位数
        时间复杂度：O(1)
        """

        # 奇数个元素
        if len(self.left) > len(self.right):
            return -self.left[0]

        # 偶数个元素
        return (-self.left[0] + self.right[0]) / 2

    def print_heaps(self):
        """
        打印堆内容（便于观察）
        """

        left_values = sorted([-x for x in self.left])
        right_values = sorted(self.right)

        print("较小一半(大顶堆):", left_values)
        print("较大一半(小顶堆):", right_values)


# ==========================
# 测试程序
# ==========================

if __name__ == "__main__":

    mf = MedianFinder()

    nums = [3, 1, 4, 1, 5]

    print("插入过程演示")
    print("=" * 40)

    for num in nums:

        mf.addNum(num)

        print(f"\n插入 {num} 后：")

        mf.print_heaps()

        print("当前中位数 =", mf.findMedian())

    print("\n" + "=" * 40)
    print("最终结果")

    mf.print_heaps()

    print("最终中位数 =", mf.findMedian())

"""输出如下：

插入过程演示
========================================

插入 3 后：
较小一半(大顶堆): [3]
较大一半(小顶堆): []
当前中位数 = 3

插入 1 后：
较小一半(大顶堆): [1]
较大一半(小顶堆): [3]
当前中位数 = 2.0

插入 4 后：
较小一半(大顶堆): [1, 3]
较大一半(小顶堆): [4]
当前中位数 = 3

插入 1 后：
较小一半(大顶堆): [1, 1]
较大一半(小顶堆): [3, 4]
当前中位数 = 2.0

插入 5 后：
较小一半(大顶堆): [1, 1, 3]
较大一半(小顶堆): [4, 5]
当前中位数 = 3

========================================
最终结果
较小一半(大顶堆): [1, 1, 3]
较大一半(小顶堆): [4, 5]
最终中位数 = 3
"""