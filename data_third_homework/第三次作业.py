class HashTable:
    def __init__(self,size: int = 31):
        """
        初始化
        :param size: 列表的长度
        """
        self.size: int = size
        self.table: list[list[tuple[str,int]]] = [[] for _ in range(size)]

    def calculate_hash_result(self,key: str) ->int:
        """
        计算键的hash值
        :param key: 键
        :return: hash值（0-size-1）
        """
        return hash(key) % self.size

    def put(self,key: str,value: int) -> None:
        """
        向哈希表中添加/更新键值对
        :param key: 键
        :param value: 值
        """
        bucket_index:int = self.calculate_hash_result(key)
        bucket: list[tuple[str,int]] = self.table[bucket_index]
        for index, (old_key, old_value) in enumerate(bucket):
            #如果有旧值就替换
            if old_key == key:
                bucket[index] = (key,value)
                return
        #如果没有键就插入
        bucket.append((key,value))

    def get(self,key: str) -> int | None:
        """
        获取对应键的值
        :param key: 键
        :return: 值（不存在返回None）
        """
        bucket_index:int = self.calculate_hash_result(key)
        bucket: list[tuple[str,int]] = self.table[bucket_index]
        for index, (old_key, old_value) in enumerate(bucket):
            #找到了
            if old_key == key:
                return old_value
        return None

    def delete(self,key: str) -> None:
        """
        删除键值对
        :param key: 键
        """
        bucket_index:int = self.calculate_hash_result(key)
        bucket: list[tuple[str,int]] = self.table[bucket_index]
        for index, (old_key, old_value) in enumerate(bucket):
            if old_key == key:
                del bucket[index]
                break
        return None

    def clear(self) -> None:
        """
        清空整个哈希表
        """
        self.table= [[] for _ in range(self.size)]

    def __str__(self) -> str:
        """
        自定义哈希表的打印格式，清晰展示每个桶的内容
        """
        # 构建打印字符串
        output_lines = ["HashTable (size={}):".format(self.size)]
        for bucket_idx in range(self.size):
            bucket = self.table[bucket_idx]
            # 只打印有内容的桶（空桶跳过，减少输出冗余）
            if bucket:
                # 格式化桶内的键值对：(key1:value1), (key2:value2)
                items_str = ", ".join([f"({k}:{v})" for k, v in bucket])
                output_lines.append(f"  桶 {bucket_idx:2d}: {items_str}")  # 2d 让索引对齐
        # 如果哈希表为空，提示空表
        if len(output_lines) == 1:
            output_lines.append("  (空哈希表)")
        # 拼接所有行并返回
        return "\n".join(output_lines)

if __name__ == "__main__":
    """哈希表完整功能测试主函数"""
    print("=" * 60)
    print("            哈希表(HashTable) 功能测试")
    print("=" * 60)

    # 1. 初始化哈希表（设置size=10，减少桶数量，方便查看输出）
    print("\n【测试1：初始化哈希表】")
    ht = HashTable(size=10)
    print(f"初始化完成，哈希表大小（桶数量）：{ht.size}")
    print("初始状态哈希表：")
    print(ht)

    # 2. 测试 put 方法（添加新键值对 + 更新已有键值对）
    print("\n【测试2：添加/更新键值对（put方法）】")
    # 添加新键值对
    ht.put("name", 18)
    ht.put("age", 25)
    ht.put("score", 95)
    ht.put("city", 10010)
    print("添加4个键值对后，哈希表状态：")
    print(ht)

    # 更新已有键的值
    print("\n更新 'name' 的值为 20，'score' 的值为 98：")
    ht.put("name", 20)
    ht.put("score", 98)
    print("更新后哈希表状态：")
    print(ht)

    # 3. 测试 get 方法（查询存在的键 + 不存在的键）
    print("\n【测试3：查询键值对（get方法）】")
    test_keys = ["name", "age", "score", "city", "gender"]
    for key in test_keys:
        value = ht.get(key)
        if value is not None:
            print(f"查询 '{key}' → 成功，值为：{value}")
        else:
            print(f"查询 '{key}' → 失败，键不存在")

    # 4. 测试 delete 方法（删除存在的键 + 不存在的键）
    print("\n【测试4：删除键值对（delete方法）】")
    # 删除存在的键
    print("删除 'age' 键：")
    ht.delete("age")
    print(ht)

    # 删除不存在的键（无报错，验证鲁棒性）
    print("\n尝试删除不存在的 'gender' 键（无报错）：")
    ht.delete("gender")
    print(ht)

    # 5. 测试 clear 方法（清空整个哈希表）
    print("\n【测试5：清空哈希表（clear方法）】")
    ht.clear()
    print("清空后哈希表状态：")
    print(ht)

    # 6. 清空后验证操作
    print("\n【测试6：清空后验证】")
    print(f"查询 'name' → {ht.get('name')}（预期None）")
    print(f"删除 'score' → 无报错（哈希表已空）")
    ht.delete("score")

    print("\n" + "=" * 60)
    print("            所有测试完成！")
    print("=" * 60)