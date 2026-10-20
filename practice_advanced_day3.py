# ============================================
# Day 3 进阶练习：面向对象编程（上）
# ============================================

# ==============================
# 第1题：创建第一个类
# ==============================
# 要求：定义一个 Dog 类
#   - __init__ 方法接收 name 和 age 两个参数
#   - 把它们存成实例属性 self.name 和 self.age
#   - 定义一个 bark 方法，打印 "汪汪！我是xxx"
#
# 提示：
#   class Dog:
#       def __init__(self, name, age):
#           self.name = name
#           self.age = age
#
#       def bark(self):
#           print(f"汪汪！我是{self.name}")
#
# 期望调用：
#   d = Dog("旺财", 3)
#   d.bark()   # 输出：汪汪！我是旺财
#
# 你的代码写在这里：
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"汪汪！我是{self.name}")





# ==============================
# 第2题：self 是谁？—— 多个实例互不影响
# ==============================
# 要求：定义一个 Student 类
#   - __init__ 接收 name 和 score
#   - 定义 show 方法，打印 "xxx 的成绩是 xx 分"
# 然后创建两个学生：
#   s1 = Student("小明", 90)
#   s2 = Student("小红", 85)
# 分别调用 s1.show() 和 s2.show()，确认互不影响
#
# 提示：self 在 s1.show() 时就是 s1，在 s2.show() 时就是 s2
#
# 期望输出：
#   小明 的成绩是 90 分
#   小红 的成绩是 85 分
#
# 你的代码写在这里：
class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def show(self):
        print(f"{self.name}成绩是{self.score}")
s1=Student("小明",90)
s2=Student("小红",85)
s1.show()
s2.show()






# ==============================
# 第3题：实例属性可以动态修改
# ==============================
# 要求：定义一个 BankAccount 类（银行账户）
#   - __init__ 接收 owner（户主）和 balance（余额，默认 0）
#   - 定义 deposit(amount) 方法：余额增加 amount，并打印当前余额
#   - 定义 withdraw(amount) 方法：余额减少 amount，并打印当前余额
#     （余额不足时打印"余额不足"，不扣钱）
#
# 期望调用：
#   acc = BankAccount("小明", 100)
#   acc.deposit(50)     # 输出：当前余额：150
#   acc.withdraw(200)   # 输出：余额不足
#   acc.withdraw(80)    # 输出：当前余额：70
#
# 提示：if amount > self.balance: print("余额不足") else: ...
#
# 你的代码写在这里：
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"当前余额：{self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("余额不足")
            return self.balance
        self.balance-=amount
        print(f"当前余额:{self.balance}")






# ==============================
# 第4题：类属性 vs 实例属性
# ==============================
# 要求：定义一个 Cat 类
#   - 类属性 species = "猫科"（写在类里、方法外面，所有猫共享）
#   - 实例属性 name（写在 __init__ 里，每只猫各自不同）
#   - 定义 introduce 方法，打印 "我是xxx，属于xxx"
#
# 期望调用：
#   c1 = Cat("咪咪")
#   c2 = Cat("喵喵")
#   c1.introduce()  # 输出：我是咪咪，属于猫科
#   c2.introduce()  # 输出：我是喵喵，属于猫科
#   print(Cat.species)  # 输出：猫科（不创建实例也能访问类属性）
#
# 提示：
#   class Cat:
#       species = "猫科"          # 类属性：缩进在 class 下，不在任何方法里
#       def __init__(self, name):
#           self.name = name      # 实例属性
#
# 你的代码写在这里：
class Cat:
    species="猫科"
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print(f"我是{self.name}，属于{self.species}")





# ==============================
# 第5题：挑战——用类重写记账本的"记录"
# ==============================
# 要求：定义一个 Record 类，表示一条记账记录
#   - __init__ 接收 date, record_type, amount, category, note 五个参数
#     （用 record_type 避免覆盖内置 type）
#   - 定义 show 方法，打印格式："2026-10-13 | 支出 | 30元 | 餐饮 | 午饭"
#   - 定义 to_dict 方法，返回字典：
#     {"日期": ..., "类型": ..., "金额": ..., "分类": ..., "备注": ...}
#
# 期望调用：
#   r = Record("2026-10-13", "支出", 30, "餐饮", "午饭")
#   r.show()        # 输出：2026-10-13 | 支出 | 30元 | 餐饮 | 午饭
#   print(r.to_dict())  # 输出：{'日期': '2026-10-13', ...}
#
# 提示：这是 Day 6-7 重构记账本的第一步——用对象代替字典
#
# 你的代码写在这里：
class Record():
    def __init__(self,date,record_type,amount,category,note):
        self.date=date
        self.record_type=record_type
        self.amount=amount
        self.category=category
        self.note=note
    def show(self):
        print(f"{self.date}|{self.record_type}|{self.amount}|{self.category}|{self.note}")
    def to_dict(self):
        return {
            "日期": self.date,
            "类型": self.record_type,
            "金额": self.amount,
            "分类": self.category,
            "备注": self.note
        }





# ============================================
#  完成后运行测试（不用改下面的代码）
# ============================================
if __name__ == "__main__":
    print("=== Day 3 进阶练习测试 ===\n")

    # 第1题
    print("第1题：创建 Dog 类")
    try:
        d = Dog("旺财", 3)
        assert d.name == "旺财" and d.age == 3, "属性不对"
        d.bark()
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第2题
    print("第2题：self 与多实例")
    try:
        s1 = Student("小明", 90)
        s2 = Student("小红", 85)
        s1.show()
        s2.show()
        assert s1.name == "小明" and s2.name == "小红", "两个实例数据混淆了"
        print("  ✅ 正确：两个实例互不影响\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第3题
    print("第3题：银行账户")
    try:
        acc = BankAccount("小明", 100)
        acc.deposit(50)       # 150
        acc.withdraw(200)     # 余额不足
        acc.withdraw(80)      # 70
        assert acc.balance == 70, f"余额应该是70，实际是{acc.balance}"
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第4题
    print("第4题：类属性 vs 实例属性")
    try:
        c1 = Cat("咪咪")
        c2 = Cat("喵喵")
        c1.introduce()
        c2.introduce()
        print(f"类属性：{Cat.species}")
        assert Cat.species == "猫科", "类属性不对"
        assert c1.species == "猫科", "实例也能访问类属性"
        assert c1.name != c2.name, "实例属性应该各自不同"
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第5题
    print("第5题：Record 类")
    try:
        r = Record("2026-10-13", "支出", 30, "餐饮", "午饭")
        r.show()
        d = r.to_dict()
        print(d)
        assert d == {"日期": "2026-10-13", "类型": "支出", "金额": 30,
                     "分类": "餐饮", "备注": "午饭"}, "to_dict 结果不对"
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    print("=== 测试结束 ===")
