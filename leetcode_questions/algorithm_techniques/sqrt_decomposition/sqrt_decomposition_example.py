class SqrtDecomposition:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.block_size = int(self.n**0.5)
        self.block_sum = [0] * (self.block_size + 1)  # 存储每个块的和

        # 预处理，计算每个块的和
        for i in range(self.n):
            block_index = i // self.block_size
            self.block_sum[block_index] += self.arr[i]

    def query_range_sum(self, left, right):
        total_sum = 0
        start_block = left // self.block_size
        end_block = right // self.block_size

        if start_block == end_block: # 左右端点在同一个块内
            for i in range(left, right + 1):
                total_sum += self.arr[i]
            return total_sum

        # 处理左端点所在块的剩余部分
        for i in range(left, (start_block + 1) * self.block_size):
            total_sum += self.arr[i]

        # 处理中间的完整块
        for i in range(start_block + 1, end_block):
            total_sum += self.block_sum[i]

        # 处理右端点所在块的起始部分
        for i in range(end_block * self.block_size, right + 1):
            total_sum += self.arr[i]

        return total_sum

    def update_value(self, index, value):
        block_index = index // self.block_size
        # 更新块的和
        self.block_sum[block_index] += value - self.arr[index]
        # 更新原数组
        self.arr[index] = value


# 示例代码
if __name__ == "__main__":
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    sqrt_decomp = SqrtDecomposition(test_array)

    print("Initial array:", test_array)
    print("Block sums:", sqrt_decomp.block_sum)

    # 查询区间 [2, 7] 的和 (5+7+9+11+13+15) = 60
    print("Range sum [2, 7]:", sqrt_decomp.query_range_sum(2, 7))

    # 更新索引 5 的值为 20 (11 -> 20)
    sqrt_decomp.update_value(5, 20)
    print("Updated array:", sqrt_decomp.arr)
    print("Updated block sums:", sqrt_decomp.block_sum)
    print("Range sum [2, 7] after update:", sqrt_decomp.query_range_sum(2, 7)) # (5+7+9+20+13+15) = 69 