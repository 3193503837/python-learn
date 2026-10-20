# ============================================
# Day 2 进阶练习：装饰器 / 深浅拷贝 / 类型注解
# ============================================

# ==============================
# 第1题：写一个计时装饰器
# ==============================
# 要求：写一个装饰器 timer，装饰函数后
# 调用函数时会自动打印执行时间
#
# 提示：
#   import time
#   def timer(func):
#       def wrapper(*args, **kwargs):
#           start = time.time()
#           result = func(*args, **kwargs)
#           end = time.time()
#           print(f"{func.__name__} 执行了 {end-start:.4f} 秒")
#           return result
#       return wrapper
#
# 用 @timer 装饰下面的 slow_func
# 调用 slow_func() 应该能看到执行时间
#
# 你的代码写在这里：





# 测试函数（用 @timer 装饰它）
def slow_func():
    total = 0
    for i in range(1000000):
        total += i
    return total


# ==============================
# 第2题：带参数的装饰器（重复执行 N 次）
# ==============================
# 要求：写一个装饰器 repeat(n)，让被装饰的函数执行 n 次
#
# 提示：带参数的装饰器需要多包一层
#   def repeat(n):
#       def decorator(func):
#           def wrapper(*args, **kwargs):
#               for _ in range(n):
#                   func(*args, **kwargs)
#           return wrapper
#       return decorator
#
# 用 @repeat(3) 装饰 say_hello
# 调用 say_hello("小明") 应该输出 3 次
#
# 你的代码写在这里：





# 测试函数（用 @repeat(3) 装饰它）
def say_hello(name):
    print(f"你好，{name}！")


# ==============================
# 第3题：浅拷贝 vs 深拷贝
# ==============================
# 要求：
#   1. 用 copy.copy() 创建浅拷贝 shallow
#   2. 用 copy.deepcopy() 创建深拷贝 deep
#   3. 修改原 data 的嵌套列表（data['hobbies'][0] = "游泳"）
#   4. 观察 shallow 和 deep 中 hobbies 是否跟着变
#
# 期望结果：
#   shallow['hobbies'] 和 data['hobbies'] 是同一个对象（id相同）
#   deep['hobbies'] 和 data['hobbies'] 是不同对象（id不同）
#
# 你的代码写在这里：

import copy

data = {
    "name": "小明",
    "age": 20,
    "hobbies": ["篮球", "音乐", "编程"]
}









# ==============================
# 第4题：类型注解
# ==============================
# 要求：给下面的函数加上类型注解
#   - name 参数是 str 类型
#   - scores 参数是 list[int] 类型（整数列表）
#   - 返回值是 dict 类型
#
# 提示：
#   def 函数名(参数: 类型) -> 返回类型:
#
# 你的代码写在这里（在下面函数上加注解）：

def student_info(name, scores):
    """返回学生信息字典"""
    return {
        "name": name,
        "total": sum(scores),
        "average": sum(scores) / len(scores)
    }


# ==============================
# 第5题：模块导入练习
# ==============================
# 要求：
#   1. 导入 math 模块
#   2. 导入 random 模块中的 randint 函数
#   3. 导入 datetime 模块并取别名为 dt
#
# 然后完成：
#   - 用 math.sqrt 计算 144 的平方根
#   - 用 randint 生成 1-100 的随机数
#   - 用 dt.datetime.now() 获取当前时间
#
# 你的代码写在这里：






# ============================================
#  完成后运行测试（不用改下面的代码）
# ============================================
if __name__ == "__main__":
    print("=== Day 2 进阶练习测试 ===\n")

    # 第1题
    print("第1题：计时装饰器")
    try:
        slow_func()
        print("  ✅ 装饰器执行成功（上面有时间输出就对了）\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第2题
    print("第2题：重复执行装饰器")
    try:
        say_hello("小明")
        print("  ✅ 执行成功（上面输出了 3 次就对了）\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第3题
    print("第3题：深浅拷贝")
    try:
        data['hobbies'][0] = "游泳"
        shallow_hobbies_changed = 'hobbies' in dir() and shallow['hobbies'][0] == "游泳"
        deep_hobbies_changed = 'deep' in dir() and deep['hobbies'][0] == "游泳"
        print(f"  原 data hobbies: {data['hobbies']}")
        if 'shallow' in dir():
            print(f"  浅拷贝 hobbies: {shallow['hobbies']}")
            print(f"  浅拷贝和原列表是同一个对象：{data['hobbies'] is shallow['hobbies']}")
        if 'deep' in dir():
            print(f"  深拷贝 hobbies: {deep['hobbies']}")
            print(f"  深拷贝和原列表是同一个对象：{data['hobbies'] is deep['hobbies']}")
        if 'shallow' in dir() and 'deep' in dir():
            if data['hobbies'] is shallow['hobbies'] and data['hobbies'] is not deep['hobbies']:
                print("  ✅ 正确：浅拷贝共享嵌套对象，深拷贝完全独立\n")
            else:
                print("  ❌ 结果不对：检查一下是不是都用了 deepcopy？\n")
        else:
            print("  ❌ 变量名不对，应该是 shallow 和 deep\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第4题
    print("第4题：类型注解")
    try:
        result = student_info("小红", [90, 85, 95])
        print(f"  函数返回：{result}")
        annotations = student_info.__annotations__
        print(f"  类型注解：{annotations}")
        if 'name' in annotations and 'scores' in annotations and 'return' in annotations:
            print("  ✅ 类型注解已添加\n")
        else:
            print("  ❌ 缺少类型注解\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第5题
    print("第5题：模块导入")
    try:
        import math
        from random import randint
        import datetime as dt
        print(f"  math.sqrt(144) = {math.sqrt(144)}")
        print(f"  randint(1, 100) = {randint(1, 100)}")
        print(f"  当前时间 = {dt.datetime.now()}")
        print("  ✅ 模块导入正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    print("=== 测试结束 ===")
