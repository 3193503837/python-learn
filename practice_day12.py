# ============================================
#  Day 12 练习题：函数定义与使用
# ============================================

# ---------- 第1题：问候函数 ----------
# 定义一个函数 say_hello(name)
# 功能：输出 "你好，xxx！欢迎学习Python"
# 调用3次，分别传入 "小明"、"小红"、"小刚"
#
# 提示：def 函数名(参数):

# 你的代码写在这里：
def say_hello(name):
    print(f"你好,{name}!欢迎学习Python")
say_hello("小红")

# ---------- 第2题：长方形面积 ----------
# 定义一个函数 area(width, height)
# 功能：计算长方形面积并返回结果
# 调用 area(5, 3) 和 area(10, 8)，输出结果
#
# 提示：return 返回结果
#       调用时用变量接住：result = area(5, 3)

# 你的代码写在这里：
def area(width,height):
    return width*height
result_1=area(5,3)
result_2=area(10,8)
print(result_1)
print(result_2)
# ---------- 第3题：判断偶数 ----------
# 定义一个函数 is_even(n)
# 功能：如果 n 是偶数返回 True，否则返回 False
# 调用测试：is_even(10)、is_even(7)，输出结果
#
# 提示：用 n % 2 == 0 判断
#       return True 或 return False

# 你的代码写在这里：
def is_even(n):
    return n%2==0
a=is_even(10)
b=is_even(7)
print(a)
print(b)

# ---------- 第4题：默认参数 ----------
# 定义一个函数 greet(name, greeting="你好")
# 功能：输出 "{greeting}，{name}！"
# 调用：
#   greet("小明")             # 用默认问候语
#   greet("小红", "早上好")    # 指定问候语
#   greet("小刚", "晚上好")    # 指定问候语
#
# 提示：def greet(name, greeting="你好"):

# 你的代码写在这里：
def greet(name,greeting="你好"):
    print(f"{greeting},{name}!")
greet("小明")
greet("小红","早上好")
greet("小刚","晚上好")

# ---------- 第5题：猜数字游戏函数版（挑战） ----------
# 定义一个函数 guess_game(max_num=100)
# 功能：随机生成 1 到 max_num 的数字，让用户猜
#   - 猜大了提示"大了"
#   - 猜小了提示"小了"
#   - 猜对了提示"恭喜，猜了X次"
# 调用 guess_game(50)   # 猜 1-50 的数字
# 调用 guess_game()     # 用默认值 100
#
# 提示：import random
#       random.randint(1, max_num)
#       while True + break
#       计数器统计次数

# 你的代码写在这里：
def guess_game(max_num=100):
    import random
    a=random.randint(1,max_num)
    count=0
    while True:
        num=int(input("请输入数字:"))
        count+=1
        if num>a:
            print("大了")
        elif num<a:
            print("小了")
        else:
            print(f"恭喜，猜对了，猜了{count}次")
            break
guess_game(50)

# ============================================
#  写完后运行：python practice_day12.py
#  然后告诉我检查
# ============================================
