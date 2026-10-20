# ============================================
# Day 6 进阶练习：迭代器、生成器、上下文管理器
# ============================================
# 这是最后一个知识点模块，明天（Day 7）用全部所学重构记账本
# 今天的目标：搞懂"逐个产出数据"的三种方式 + with 背后的原理

# ==============================
# 第1题：自定义迭代器
# ==============================
# 要求：定义 CountDown 类，实现倒计时迭代器
#   - __init__(self, n)：保存起点 n，并设置 self.current = n
#   - __iter__(self)：返回自己（return self）
#   - __next__(self)：
#       若 self.current <= 0：raise StopIteration（告诉 for 循环"没了"）
#       否则：先记住 value = self.current，再 self.current -= 1，最后 return value
#
# 期望调用：
#   print(list(CountDown(3)))   # 输出：[3, 2, 1]
#
# 提示：for 循环会不停调用 __next__，直到抛出 StopIteration 才停
#   def __iter__(self):
#       return self
#   def __next__(self):
#       if self.current <= 0:
#           raise StopIteration
#       value = self.current
#       self.current -= 1
#       return value
#
# 你的代码写在这里：
class CountDown:
    def __init__(self,n):
        self.now=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.now<=0:
            raise StopIteration
        result=self.now
        self.now-=1
        return result

# ==============================
# 第2题：生成器函数（yield）
# ==============================
# 要求：定义生成器函数 count_down_gen(n)，效果和第1题一样，但用 yield
#   - 从 n 开始倒数，每数一个就 yield 一个
#
# 期望调用：
#   print(list(count_down_gen(3)))   # 输出：[3, 2, 1]
#
# 提示：只要函数里有 yield，它就不再是普通函数，而是"生成器函数"
#   调用它不会立刻执行，而是返回一个生成器；for 每次取值时才继续往下跑
#   def count_down_gen(n):
#       while n > 0:
#           yield n        # 吐出一个值，然后"暂停"在这里
#           n -= 1
#
# 你的代码写在这里：
def count_down_gen(n):
    while n>0:
        yield n
        n-=1


# ==============================
# 第3题：生成器表达式
# ==============================
# 要求：定义函数 even_square_sum()，返回 1~100 中所有偶数的平方和
#   - 必须用"生成器表达式"（不是列表推导）
#   - 生成器表达式就是把列表推导的 [] 换成 ()
#
# 期望调用：
#   print(even_square_sum())   # 输出：171700
#
# 提示：
#   列表推导（一次性生成整个列表）：[x*x for x in range(1,101) if x % 2 == 0]
#   生成器表达式（边算边用，省内存）：sum(x*x for x in range(1,101) if x % 2 == 0)
#
# 你的代码写在这里：
def even_square_sum():
    return sum(i**2 for i in range(1,101) if i%2==0)

# ==============================
# 第4题：上下文管理器（with 的原理）
# ==============================
# 要求：定义 Step 类，用来自动打印步骤的进入和退出
#   - __enter__(self)：打印 "进入步骤"，并 return "资源已就绪"
#   - __exit__(self, exc_type, exc_val, exc_tb)：打印 "退出步骤"
#
# 期望调用：
#   with Step() as r:
#       print(r)
#   # 输出：
#   #   进入步骤
#   #   资源已就绪
#   #   退出步骤
#
# 提示：with 的本质 —— 进入时自动调用 __enter__，退出时（即使报错也）调用 __exit__
#   你在 Day 13 写的 with open(...) 就是文件对象实现了这两个方法
#   def __enter__(self):
#       print("...")
#       return "..."
#   def __exit__(self, exc_type, exc_val, exc_tb):
#       print("...")
#
# 你的代码写在这里：
class Step:
    def __enter__(self):
        print("进入步骤")
        return "资源已就绪"
    def __exit__(self,exc_type,exc_value,traceback):
        print("退出步骤")

# ==============================
# 第5题：挑战——让 AccountBook 可以被 for 遍历
# ==============================
# 要求：定义 AccountBook 类，让它支持 for r in book 直接遍历记录
#   - __init__(self)：创建空列表 self.records = []
#   - add(self, record)：追加记录
#   - __iter__(self)：返回 iter(self.records)
#   - total(self, record_type)：返回指定类型的金额总和
#
# 期望：for r in book 能拿到每一条记录（Day 5 的账本只能 book.records 手动遍历）
#
# 提示：__iter__ 只要返回一个"能逐个取值的东西"就行
#   最简单：return iter(self.records)
#   （iter() 会把列表变成迭代器；有了它，for 和 sum() 都能直接用）
#
# 你的代码写在这里：
class AccountBook:
    def __init__(self):
        self.records=[]
        self.i=0
    def add(self,record):
        self.records.append(record)
    def __iter__(self):
        for r in self.records:
            yield r
    def total(self,record_type):
        return sum(r.amount for r in self if r.record_type==record_type)


# ============================================
#  完成后运行测试（不用改下面的代码）
# ============================================
if __name__ == "__main__":
    print("=== Day 6 进阶练习测试 ===\n")

    # 第1题
    print("第1题：自定义迭代器")
    try:
        result = list(CountDown(3))
        assert result == [3, 2, 1], f"结果应为[3, 2, 1]，实际{result}"
        print(f"  list(CountDown(3)) = {result}")
        # 再验证一遍：迭代器用完就"空"了
        result2 = list(CountDown(5))
        assert result2 == [5, 4, 3, 2, 1], f"结果不对：{result2}"
        print(f"  list(CountDown(5)) = {result2}")
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第2题
    print("第2题：生成器函数 yield")
    try:
        gen = count_down_gen(3)
        assert hasattr(gen, "__next__"), "count_down_gen 应该返回生成器"
        result = list(gen)
        assert result == [3, 2, 1], f"结果应为[3, 2, 1]，实际{result}"
        print(f"  list(count_down_gen(3)) = {result}")
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第3题
    print("第3题：生成器表达式")
    try:
        total = even_square_sum()
        assert total == 171700, f"结果应为171700，实际{total}"
        print(f"  even_square_sum() = {total}")
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第4题
    print("第4题：上下文管理器")
    try:
        with Step() as r:
            assert r == "资源已就绪", f"__enter__ 应返回'资源已就绪'，实际{r}"
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第5题
    print("第5题：AccountBook 可遍历")
    try:
        class R:
            def __init__(self, record_type, amount):
                self.record_type = record_type
                self.amount = amount

        book = AccountBook()
        book.add(R("收入", 100))
        book.add(R("支出", 30))
        book.add(R("收入", 200))

        amounts = [r.amount for r in book]          # for 遍历
        assert amounts == [100, 30, 200], f"遍历结果不对：{amounts}"
        assert book.total("收入") == 300, f"总收入应为300，实际{book.total('收入')}"
        # sum() 也能直接吃可迭代对象
        assert sum(r.amount for r in book) == 330, "sum 遍历求和不对"
        print(f"  for r in book → 金额列表 {amounts}")
        print(f"  总收入：{book.total('收入')}，全部合计：{sum(r.amount for r in book)}")
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    print("=== 测试结束 ===")
