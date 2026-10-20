# ============================================
# Day 5 进阶练习：面向对象编程（下）—— 继承与多态
# ============================================

# ==============================
# 第1题：继承的基本写法
# ==============================
# 要求：定义 Animal 父类和 Dog 子类
#   - Animal 有 __init__(self, name)，属性 self.name
#   - Animal 有方法 eat()，打印 "{name} 在吃东西"
#   - Dog 继承 Animal（class Dog(Animal):），不写任何新代码
#   - 创建 Dog("旺财")，调用 eat()
#
# 期望输出：
#   旺财 在吃东西
#
# 提示：子类括号里写父类名，就能白拿父类所有代码
#   class Dog(Animal):
#       pass          # 什么都不写也能继承一切
#
# 你的代码写在这里：
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name}在吃东西")
class Dog(Animal):
    pass

# ==============================
# 第2题：super().__init__() —— 扩展父类的构造方法
# ==============================
# 要求：定义 Student 继承 Person
#   - Person 的 __init__(self, name, age)
#   - Student 的 __init__(self, name, age, school)
#     前2个参数交给 super().__init__() 处理
#     school 自己保存
#
# 期望调用：
#   s = Student("小明", 20, "北京大学")
#   print(s.name, s.age, s.school)   # 输出：小明 20 北京大学
#
# 提示：
#   class Student(Person):
#       def __init__(self, name, age, school):
#           super().__init__(name, age)   # 父类的活交给父类干
#           self.school = school          # 自己的活自己干
#
# 你的代码写在这里：
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,school):
        super().__init__(name,age)
        self.school=school




# ==============================
# 第3题：方法重写（override）
# ==============================
# 要求：定义 Shape 父类和 Square、Circle 子类
#   - Shape 有方法 area(self)，返回 0
#   - Square 的 __init__(self, side)，重写 area 返回 side 的平方
#   - Circle 的 __init__(self, radius)，重写 area 返回 3.14 * radius ** 2
#
# 期望调用：
#   shapes = [Square(4), Circle(2)]
#   for s in shapes:
#       print(s.area())    # 输出：16 然后输出 12.56
#
# 提示：子类定义和父类同名的方法 = 重写，调用时用自己的版本
#
# 你的代码写在这里：
class Shape():
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2

# ==============================
# 第4题：魔术方法 __str__
# ==============================
# 要求：定义 Book 类，实现 __str__ 魔术方法
#   - __init__(self, title, price)
#   - __str__ 返回 "《title》售价X元"
#   - print(book) 时自动显示这个字符串（而不是 <__main__.Book object at ...>）
#
# 期望调用：
#   b = Book("Python入门", 59)
#   print(b)    # 输出：《Python入门》售价59元
#
# 提示：__str__ 必须返回字符串（return，不是 print）
#   def __str__(self):
#       return f"..."
#
# 你的代码写在这里：
class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    def __str__(self):
        return f"《{self.title}》售价{self.price}元"


# ==============================
# 第5题：挑战——AccountBook 类（重构记账本第二步）
# ==============================
# 要求：定义 AccountBook 类管理 Record 记录（最终重构的核心类！）
#   - __init__(self)：创建空列表 self._records = []
#   - add(self, record)：把 record 添加到 _records
#   - total(self, record_type)：返回指定类型（"收入"/"支出"）的金额总和
#   - balance(self)：返回总收入 - 总支出
#   - __str__：返回 f"账本共有 {len(self._records)} 条记录"
#
# 提示：record 是 Day 4 写的 Record 对象（这里用简化版测试）
#   - 取类型：record.record_type
#   - 取金额：record.amount
#   - total 里可以用循环累加，也可以一行 sum() 生成器：
#     sum(r.amount for r in self._records if r.record_type == record_type)
#
# 你的代码写在这里：
class AccountBook:
    def __init__(self):
        self.records=[]
    def add(self,record):
        self.records.append(record)
    def total(self,record_type):
        return sum(r.amount for r in self.records if r.record_type==record_type)
    def balance(self):
        sum1=sum(r.amount for r in self.records if r.record_type=="收入")
        sum2=sum(r.amount for r in self.records if r.record_type=="支出")
        return sum1-sum2
    def __str__(self):
        return f"账本共有 {len(self.records)} 条记录"


# ============================================
#  完成后运行测试（不用改下面的代码）
# ============================================
if __name__ == "__main__":
    print("=== Day 5 进阶练习测试 ===\n")

    # 第1题
    print("第1题：继承基本写法")
    try:
        d = Dog("旺财")
        d.eat()
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第2题
    print("第2题：super().__init__()")
    try:
        s = Student("小明", 20, "北京大学")
        assert s.name == "小明" and s.age == 20 and s.school == "北京大学"
        print(f"  name={s.name}, age={s.age}, school={s.school}")
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第3题
    print("第3题：方法重写")
    try:
        sq = Square(4)
        ci = Circle(2)
        assert sq.area() == 16, f"正方形面积应为16，实际{sq.area()}"
        assert abs(ci.area() - 12.56) < 0.01, f"圆形面积应为12.56，实际{ci.area()}"
        print(f"  正方形面积：{sq.area()}，圆形面积：{ci.area()}")
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第4题
    print("第4题：__str__ 魔术方法")
    try:
        b = Book("Python入门", 59)
        text = str(b)
        assert "Python入门" in text and "59" in text, f"输出格式不对：{text}"
        print(f"  print(book) 输出：{text}")
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # 第5题
    print("第5题：AccountBook 类")
    try:
        class R:
            def __init__(self, record_type, amount):
                self.record_type = record_type
                self.amount = amount

        book = AccountBook()
        assert str(book) == "账本共有 0 条记录", f"__str__ 不对：{book}"
        book.add(R("收入", 100))
        book.add(R("支出", 30))
        book.add(R("收入", 200))
        book.add(R("支出", 50))
        assert book.total("收入") == 300, f"总收入应为300，实际{book.total('收入')}"
        assert book.total("支出") == 80, f"总支出应为80，实际{book.total('支出')}"
        assert book.balance() == 220, f"余额应为220，实际{book.balance()}"
        print(f"  {book}")
        print(f"  总收入：{book.total('收入')}，总支出：{book.total('支出')}，余额：{book.balance()}")
        print("  ✅ 正确\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    print("=== 测试结束 ===")
