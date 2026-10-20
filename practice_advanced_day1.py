# ============================================
# Day 1 进阶练习：Python 进阶基础（上）
# ============================================

# ==============================
# 第1题：*args 求和函数
# ==============================
# 要求：写一个函数 sum_all，可以接收任意数量的参数
# 返回所有参数的和
# 提示：用 *args 接收，然后遍历求和
#
# 期望调用：
#   print(sum_all(1, 2, 3))          # 输出：6
#   print(sum_all(10, 20, 30, 40))   # 输出：100
#
# 你的代码写在这里：
def sum_all(*arg):
    a=0
    for i in arg:
        a+=i
    return a




# ==============================
# 第2题：lambda + sorted 排序
# ==============================
# 要求：给学生列表按分数从高到低排序
# 每个学生是 (名字, 分数) 的元组
# 用 lambda 指定排序规则
#
# 提示：sorted(列表, key=lambda..., reverse=True)
#
# 期望输出：
#   [('小明', 95), ('小红', 88), ('小刚', 78)]
#
# 你的代码写在这里：
students = [("小明", 95), ("小红", 88), ("小刚", 78)]
students.sort(key=lambda s:s[1],reverse=True)

# ==============================
# 第3题：map 把每个数乘以10
# ==============================
# 要求：用 map + lambda 把列表中每个数乘以10
# 注意：map 返回的是迭代器，要用 list() 转成列表
#
# 提示：list(map(lambda x: ..., nums))
#
# 期望输出：
#   [10, 20, 30, 40, 50]
#
# 你的代码写在这里：
nums = [1, 2, 3, 4, 5]
tens=list(map(lambda x:x*10,nums))

# ==============================
# 第4题：filter 筛选偶数
# ==============================
# 要求：用 filter + lambda 筛选出列表中的偶数
# 注意：filter 返回的也是迭代器，要用 list() 转成列表
#
# 提示：list(filter(lambda x: x % 2 == 0, nums))
#
# 期望输出：
#   [2, 4, 6, 8, 10]
#
# 你的代码写在这里：
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
twos=list(filter(lambda x:x%2==0,nums2))

# ==============================
# 第5题：zip 合并成字典
# ==============================
# 要求：用 zip 把两个列表合并成一个字典
# names 是键，scores 是值
#
# 提示：dict(zip(列表1, 列表2))
#
# 期望输出：
#   {'小明': 90, '小红': 85, '小刚': 78}
#
# 你的代码写在这里：
names = ["小明", "小红", "小刚"]
scores = [90, 85, 78]
grades=dict(zip(names,scores))

# ==============================
# 完成后运行测试（不用改下面的代码）
# ==============================
if __name__ == "__main__":
    print("=== Day 1 进阶练习测试 ===\n")

    # 第1题
    try:
        r1 = sum_all(1, 2, 3)
        r2 = sum_all(10, 20, 30, 40)
        print(f"第1题：sum_all(1,2,3) = {r1}, sum_all(10,20,30,40) = {r2}")
        if r1 == 6 and r2 == 100:
            print("  ✅ 正确\n")
        else:
            print("  ❌ 结果不对\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第2题
    try:
        result = sorted(students, key=lambda s: s[1], reverse=True)
        print(f"第2题：排序结果 = {result}")
        if result == [("小明", 95), ("小红", 88), ("小刚", 78)]:
            print("  ✅ 正确\n")
        else:
            print("  ❌ 结果不对\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第3题
    try:
        result = list(map(lambda x: x * 10, nums))
        print(f"第3题：map结果 = {result}")
        if result == [10, 20, 30, 40, 50]:
            print("  ✅ 正确\n")
        else:
            print("  ❌ 结果不对\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第4题
    try:
        result = list(filter(lambda x: x % 2 == 0, nums2))
        print(f"第4题：filter结果 = {result}")
        if result == [2, 4, 6, 8, 10]:
            print("  ✅ 正确\n")
        else:
            print("  ❌ 结果不对\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第5题
    try:
        result = dict(zip(names, scores))
        print(f"第5题：zip结果 = {result}")
        if result == {"小明": 90, "小红": 85, "小刚": 78}:
            print("  ✅ 正确\n")
        else:
            print("  ❌ 结果不对\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")
