# ============================================
# Day 4 进阶练习：面向对象编程（中）
# ============================================

# ==============================
# 第1题：三种方法对比
# ==============================
# 要求：定义一个 MathTool 类，包含三种方法
#
# 1. 实例方法 instance_method(self)：
#    打印 "实例方法被调用，self=xxx"
#
# 2. 类方法 class_method(cls)：用 @classmethod 装饰
#    打印 "类方法被调用，cls=xxx"
#
# 3. 静态方法 static_method()：用 @staticmethod 装饰
#    打印 "静态方法被调用"
#
# 提示：
#   class MathTool:
#       def instance_method(self):
#           print(f"实例方法，self={self}")
#
#       @classmethod
#       def class_method(cls):
#           print(f"类方法，cls={cls}")
#
#       @staticmethod
#       def static_method():
#           print("静态方法")
#
# 你的代码写在这里：
class MathTool:
    def __init__(self):
        pass
    def instance_method(self):
        print(f"实例方法被调用,self={self}")
    @classmethod
    def class_method(cls):
        print(f"类方法被调用，self={cls}")
    @staticmethod
    def static_method():
        print("静态方法")







# ==============================
# 第2题：类方法做"工厂函数"
# ==============================
# 要求：定义一个 Person 类
#   - __init__ 接收 name 和 age
#   - 定义类方法 from_string(cls, text)
#     接收 "小明,20" 这样的字符串
#     用 split(",") 拆开，创建并返回 Person 实例
#
# 期望调用：
#   p = Person.from_string("小明,20")
#   print(p.name, p.age)  # 输出：小明 20
#
# 提示：
#   @classmethod
#   def from_string(cls, text):
#       name, age = text.split(",")
#       return cls(name, int(age))
#
# 你的代码写在这里：
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,text):
        name,age=text.split(",")
        return(cls(name,int(age)))






# ==============================
# 第3题：私有属性与封装
# ==============================
# 要求：定义一个 Account 类
#   - __init__ 接收 owner 和初始 balance
#   - 余额用双下划线私有属性 self.__balance 保存
#   - 提供 3 个公开方法：
#       deposit(amount)  —— 存款，amount 必须大于 0，否则打印"金额必须大于0"
#       withdraw(amount) —— 取款，先检查 amount>0，再检查余额够不够
#       get_balance()    —— 返回当前余额（读取私有属性的唯一入口）
#
# 注意：私有属性外部不能直接访问（self.__balance 在外部访问会报错）
#
# 期望调用：
#   acc = Account("小明", 100)
#   acc.deposit(50)      # 余额变 150
#   acc.withdraw(200)    # 打印"余额不足"
#   acc.withdraw(-10)    # 打印"金额必须大于0"
#   print(acc.get_balance())  # 输出：150
#
# 你的代码写在这里：
class Account:
    def __init__(self,owner,balance):
        self.__owner=owner
        self.__balance=balance
    def deposit(self,amount):
        if amount<0:
            print("金额必须大于0")
            return
        self.__balance+=amount
    def withdraw(self,amount):
        if amount<0:
            print("金额必须大于0")
            return
        if self.__balance-amount<0 :
            print("余额不足")
            return
        self.__balance-=amount
    def get_balance(self):
        return self.__balance







# ==============================
# 第4题：@property 装饰器
# ==============================
# 要求：定义一个 Rectangle（矩形）类
#   - __init__ 接收 width 和 height
#   - 用 @property 把 area 变成"属性"（不加括号就能访问）
#     area = 宽 × 高
#   - 用 @property 把 width 变成只读属性
#   - 用 @width.setter 给 width 加校验：必须大于 0，否则 raise ValueError
#
# 期望调用：
#   r = Rectangle(3, 4)
#   print(r.area)        # 输出：12（注意：是 r.area 不是 r.area()）
#   r.width = 5
#   print(r.area)        # 输出：20
#   r.width = -1         # 报错 ValueError
#
# 提示：
#   class Rectangle:
#       def __init__(self, width, height):
#           self.__width = width
#           self.height = height
#
#       @property
#       def area(self):
#           return self.__width * self.height
#
#       @property
#       def width(self):
#           return self.__width
#
#       @width.setter
#       def width(self, value):
#           if value <= 0:
#               raise ValueError("宽度必须大于0")
#           self.__width = value
#
# 你的代码写在这里：
class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
    @property
    def area(self):
        return self._width*self._height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if value<=0:
            raise ValueError
        self._width=value







# ==============================
# 第5题：挑战——升级 Record 类
# ==============================
# 要求：给 Day 3 的 Record 类加封装
#   - amount 变成私有属性 __amount
#   - 用 @property 读取 amount
#   - 用 @amount.setter 校验：金额必须大于 0，否则 raise ValueError
#   - record_type 也做校验：只能是 "收入" 或 "支出"，否则 raise ValueError
#   - 保留 show 和 to_dict 方法（注意访问金额要用 self.amount，走 property）
#
# 期望调用：
#   r = Record("2026-10-14", "支出", 30, "餐饮", "午饭")
#   print(r.amount)       # 输出：30（走 property，能读）
#   r.amount = 50         # 合法，能改
#   r.amount = -10        # ValueError
#   r2 = Record("2026-10-14", "转账", 100, "其他", "")  # ValueError
#
# 提示：
#   class Record:
#       def __init__(self, date, record_type, amount, category, note):
#           self.date = date
#           self.record_type = record_type   # 赋值时会触发 setter 校验
#           self.amount = amount
#           self.category = category
#           self.note = note
#
#       @property
#       def amount(self):
#           return self.__amount
#
#       @amount.setter
#       def amount(self, value):
#           if value <= 0:
#               raise ValueError("金额必须大于0")
#           self.__amount = value
#
# 你的代码写在这里：
class Record:
    def __init__(self, date, record_type, amount, category, note):
        self.date = date
        self.record_type = record_type   # 走 setter，触发校验
        self.amount = amount             # 走 setter，触发校验
        self.category = category
        self.note = note

    @property
    def amount(self):
        return self._amount              # 私有名读数据

    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError("金额必须大于0")
        self._amount = value             # 私有名存数据

    @property
    def record_type(self):
        return self._record_type         # 私有名读数据

    @record_type.setter
    def record_type(self, value):
        if value != "收入" and value != "支出":
            raise ValueError("类型错误")
        self._record_type = value        # 私有名存数据

    def show(self):
        print(f"{self.date} | {self.record_type} | {self.amount}元 | {self.category} | {self.note}")

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
    print("=== Day 4 进阶练习测试 ===\n")

    # 第1题
    print("第1题：三种方法对比")
    try:
        m = MathTool()
        m.instance_method()
        MathTool.class_method()
        m.class_method()        # 实例也能调用类方法
        MathTool.static_method()
        m.static_method()       # 实例也能调用静态方法
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第2题
    print("第2题：类方法工厂函数")
    try:
        p = Person.from_string("小明,20")
        print(f"  name={p.name}, age={p.age}")
        assert p.name == "小明" and p.age == 20, "解析结果不对"
        p2 = Person.from_string("小红,18")
        assert p2.age == 18
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第3题
    print("第3题：私有属性与封装")
    try:
        acc = Account("小明", 100)
        acc.deposit(50)
        acc.withdraw(200)
        acc.withdraw(-10)
        bal = acc.get_balance()
        print(f"  最终余额：{bal}")
        assert bal == 150, f"余额应为150，实际{bal}"
        try:
            acc.__balance
            print("  ❌ 私有属性竟然能直接访问\n")
        except AttributeError:
            print("  ✅ 正确：私有属性无法外部直接访问\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第4题
    print("第4题：@property")
    try:
        r = Rectangle(3, 4)
        assert r.area == 12, f"面积应为12，实际{r.area}"
        r.width = 5
        assert r.area == 20, f"改宽后面积应为20，实际{r.area}"
        try:
            r.width = -1
            print("  ❌ 宽度为负数没有报错\n")
        except ValueError:
            print(f"  area={r.area}，width 校验正常触发 ValueError")
            print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第5题
    print("第5题：Record 类升级")
    try:
        r = Record("2026-10-14", "支出", 30, "餐饮", "午饭")
        assert r.amount == 30
        r.amount = 50
        assert r.amount == 50
        print(f"  修改后金额：{r.amount}")
        errors_caught = 0
        try:
            r.amount = -10
        except ValueError:
            errors_caught += 1
        try:
            r2 = Record("2026-10-14", "转账", 100, "其他", "")
        except ValueError:
            errors_caught += 1
        d = r.to_dict()
        assert d["金额"] == 50, f"to_dict 金额应为50，实际{d['金额']}"
        print(f"  to_dict：{d}")
        if errors_caught == 2:
            print("  ✅ 正确：金额和类型校验都生效\n")
        else:
            print(f"  ❌ 校验只触发了 {errors_caught}/2 次\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    print("=== 测试结束 ===")
