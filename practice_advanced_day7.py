# ============================================
#  Day 7 毕业实战：用 OOP 重构记账本
# ============================================
#  目标：把 practice_day14.py 的"字典 + 函数"版记账本
#       重构成"类 + 方法"版 —— 本周学习的最终成果
#
#  架构：
#    Record 类      → 管"一条记录"（数据 + 校验）
#    AccountBook 类 → 管"整个账本"（增删改查 + 文件存取 + 统计）
#    main()         → 菜单交互
#
#  本周知识对照：
#    Record 的类型/金额校验   → Day 4 @property + setter
#    Record.from_dict 工厂    → Day 4 @classmethod
#    Record.__str__           → Day 5 魔术方法
#    AccountBook.__iter__     → Day 6 生成器 yield
#    AccountBook.save/load    → Day 13 with + json + 异常处理
#    （选做加分：给方法参数加 Day 2 的类型注解）
#
#  运行方式：
#    python practice_advanced_day7.py        → 跑自动测试（写第1-4步时用）
#    python practice_advanced_day7.py menu   → 启动记账本（写完第5步后用）
# ============================================

import json

FILE_NAME = "records_oop.json"    # 新版数据文件，不会覆盖你旧版的数据


# ==============================
# 第1步：Record 类 —— 一条记录（Day 4 版本的升级）
# ==============================
#  属性与校验：
#    date / category / note : 普通属性，直接赋值
#    record_type            : property 校验 —— 只能是 "收入" 或 "支出"
#    amount                 : property 校验 —— 必须大于 0
#
#  要求实现：
#    __init__(self, date, record_type, amount, category, note)
#        注意：类型和金额用【公开名】赋值（self.record_type = record_type）
#              这样创建对象时就触发 setter 校验（Day 4 的教训！）
#    __str__      → "2026-10-18 | 支出 | 30元 | 餐饮 | 午饭"
#    to_dict()    → {"日期": ..., "类型": ..., "金额": ..., "分类": ..., "备注": ...}
#    from_dict(d) → @classmethod 工厂：从字典创建 Record（读取文件时用）
#
#  提示（from_dict 参考写法）：
#      @classmethod
#      def from_dict(cls, d):
#          return cls(d["日期"], d["类型"], d["金额"], d["分类"], d["备注"])
#
# 你的代码写在这里：
class Record():
    def __init__(self,date,record_type,amount,category,note):
        self.date = date
        self.record_type = record_type
        self.amount = amount
        self.category = category
        self.note = note
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self,amount):
        if amount <= 0:
            raise ValueError("金额必须大于零")
        self._amount = amount
        return self._amount
    @property
    def record_type(self):
        return self._record_type
    @record_type.setter
    def record_type(self,record_type):
        if record_type!="收入" and record_type!="支出":
            raise ValueError("类型错误")
        self._record_type = record_type
    def __str__(self):
        return f"{self.date}|{self.record_type}|{self.amount}|{self.category}|{self.note}"
    def to_dict(self):
        return {
            "日期": self.date,
            "类型": self.record_type,
            "金额": self.amount,
            "分类": self.category,
            "备注": self.note
        }
    @classmethod
    def from_dict(cls,d):
        return cls(d["日期"],d["类型"],d["金额"],d["分类"],d["备注"])


# ==============================
# 第2步：AccountBook 类 —— 基础结构
# ==============================
#  要求实现：
#    __init__(self)          → self.records = []
#    add(self, record)       → 追加一条 Record
#    __len__(self)           → len(book) 直接返回记录条数
#    __iter__(self)          → 用 yield 实现（Day 6 的优化版），支持 for r in book
#    delete(self, index)     → 删除第 index 条（编号从 1 开始，和显示一致）
#                              编号合法：self.records.pop(index - 1) 并返回 True
#                              编号不合法（如 99 或 0）：返回 False，什么都不做
#
#  提示（__iter__ 参考写法）：
#      def __iter__(self):
#          for r in self.records:
#              yield r
#
# 你的代码写在这里：
class AccountBook:
    def __init__(self):
        self.records=[]
    def add(self,record):
        self.records.append(record)
    def __len__(self):
        return len(self.records)
    def __iter__(self):
        for r in self.records:
            yield r
    def delete(self,i):
        if i<=0 or i>len(self.records):
            print("没有这条记录")
            return False
        self.records.pop(i-1)
        return True

# ==============================
# 第3步：AccountBook —— 文件存取（save / load）
# ==============================
#  要求实现：
#    save(self, filename)
#      1. data = [r.to_dict() for r in self]   ← 注意遍历 self（Day 6 优化）
#      2. with open(filename, "w", encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False, indent=2)
#
#    load(self, filename)
#      1. 用 try/except 处理两种错误（Day 13 的知识点！）：
#           FileNotFoundError   → 文件不存在
#           json.JSONDecodeError → 文件内容损坏
#         出错时：self.records = []，然后 return（程序不能崩）
#      2. 成功时：self.records = [Record.from_dict(d) for d in data]
#         ← 读出来的是字典，必须用工厂方法转回 Record 对象
#
# 你的代码写在这里（写在 AccountBook 类里面）：
    def save(self,file_name):
        data=[r.to_dict() for r in self.records]
        with open(file_name,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
    def load(self,file_name):
        try:
            with open(file_name,"r",encoding="utf-8") as f:
                data=json.load(f)
                self.records=[Record.from_dict(d) for d in data]
        except FileNotFoundError:
            self.records=[]
            return
        except json.JSONDecodeError:
            self.records=[]
            return


# ==============================
# 第4步：AccountBook —— 统计功能
# ==============================
#  要求实现：
#    total(self, record_type)          → 指定类型的金额总和（用生成器表达式）
#    balance(self)                     → 余额 = 收入总和 - 支出总和
#    filter_by_category(self, category) → 返回该分类的所有记录（列表）
#
#  提示（Day 6 的组合技）：
#      def total(self, record_type):
#          return sum(r.amount for r in self if r.record_type == record_type)
#      ← 遍历 self 而不是 self.records：自己写的 __iter__ 自己也要用！
#
# 你的代码写在这里（写在 AccountBook 类里面）：
    def total(self,record_type):
        return sum(r.amount for r in self if r.record_type==record_type)
    def balance(self):
        total_1=sum(r.amount for r in self if r.record_type=="收入")
        total_2=sum(r.amount for r in self if r.record_type=="支出")
        balance=total_1-total_2
        return balance
    def filter_by_category(self,category):
        by_category=[]
        for r in self.records:
            if r.category==category:
                by_category.append(r)
        return by_category


# ==============================
# 第5步：菜单交互（测试全绿后再写，写完手动体验）
# ==============================
#  功能菜单：1.添加  2.查看全部  3.统计  4.按分类查找  5.删除  0.退出
#
#  提示1：类型要"重新要求"直到合法（while True + break）：
#      while True:
#          record_type = input("类型（收入/支出）：")
#          if record_type in ("收入", "支出"):
#              break
#          print("类型只能是 收入 或 支出")
#  提示2：金额用 try/except ValueError 重新要求（float 转换）
#  提示3：每次添加/删除后调用 book.save(FILE_NAME)，下次打开数据还在
#  提示4：查看全部前先判断空账本：if len(book) == 0
#  提示5：main() 已经写好，你只需补全 input_record / show_all / show_stats
#         以及菜单分支 4 和 5

def input_record():
    """收集用户输入，返回 Record 对象；类型/金额不合法会重新要求"""
    # 你的代码写在这里：
    date = input("日期：")
    while True:
        record_type = input("类型：")
        if record_type=="收入" or record_type=="支出":
            break
        print("类型只能是收入或支出")
    while True:
        try:
            amount = float(input("金额："))
            break
        except ValueError:
            print("金额必须是数字")
    category = input("分类：")
    note = input("备注：")
    return Record(date,record_type,amount,category,note)


def show_all(book):
    """打印所有记录（空账本先打印'暂无记录'再 return）"""
    # 你的代码写在这里：
    if len(book)==0:
        print("暂无记录")
        return
    for i,r in enumerate(book,1):
        print(f"{i}:{r}")



def show_stats(book):
    """打印总收入 / 总支出 / 余额"""
    # 你的代码写在这里：
    income=book.total("收入")
    expense=book.total("支出")
    balance=book.balance()
    print(f"总收入:{income}|总支出:{expense}|余额:{balance}")



def main():
    book = AccountBook()
    book.load(FILE_NAME)          # 启动时读数据（文件不存在也不会崩）
    print(f"已加载 {len(book)} 条记录")

    while True:
        print("\n===== OOP 记账本 =====")
        print("1.添加记录  2.查看全部  3.统计")
        print("4.按分类查找 5.删除记录  0.退出")
        choice = input("请选择：")

        if choice == "1":
            r = input_record()
            if r is not None:
                book.add(r)
                book.save(FILE_NAME)
                print("添加成功！")
        elif choice == "2":
            show_all(book)
        elif choice == "3":
            show_stats(book)
        elif choice == "4":
            # 你的代码写在这里：
            # 1. category = input("要查找的分类：")
            # 2. results = book.filter_by_category(category)
            # 3. 空列表打印"该分类暂无记录"，否则逐条 print(r)
            category=input("要查找的分类：")
            results=book.filter_by_category(category)
            if len(results)==0:
                print("该分类暂无记录")
            else:
                for r in results:
                    print(r)
        elif choice == "5":
            # 你的代码写在这里：
            # 1. show_all(book) 让用户看到编号
            # 2. index = int(input("要删除第几条："))  ← 记得 try/except ValueError
            # 3. book.delete(index) 成功后 book.save(FILE_NAME)
            show_all(book)
            try:
                i=int(input("要删除第几条："))
            except ValueError:
                print("编号必须是阿拉伯数字")
                continue
            if book.delete(i):
                book.save(FILE_NAME)
                print("删除成功")
            else:
                print("删除失败")

        elif choice == "0":
            book.save(FILE_NAME)
            print("数据已保存，再见！")
            break
        else:
            print("无效选择，请重新输入")


# ============================================
#  自动测试（不用改下面的代码）
# ============================================
def run_tests():
    print("=== Day 7 毕业项目测试 ===\n")

    # ---- 第1步：Record ----
    print("第1步：Record 类")
    try:
        r = Record("2026-10-18", "支出", 30, "餐饮", "午饭")
        assert r.amount == 30 and r.record_type == "支出"

        errors = 0
        try:
            r.amount = -5
        except ValueError:
            errors += 1
        try:
            Record("2026-10-18", "转账", 50, "其他", "")
        except ValueError:
            errors += 1
        assert errors == 2, f"校验应拦截2次，实际{errors}次"

        s = str(r)
        assert "支出" in s and "30" in s, f"__str__ 输出不对：{s}"

        d = r.to_dict()
        assert d["类型"] == "支出" and d["金额"] == 30 and d["日期"] == "2026-10-18"
        r2 = Record.from_dict(d)
        assert isinstance(r2, Record) and r2.amount == 30 and r2.record_type == "支出"
        print("  ✅ 通过\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # ---- 第2步：AccountBook 基础 ----
    print("第2步：AccountBook 基础（add / len / for / delete）")
    try:
        book = AccountBook()
        book.add(Record("2026-10-18", "收入", 3000, "工资", "10月工资"))
        book.add(Record("2026-10-18", "支出", 30, "餐饮", "午饭"))
        book.add(Record("2026-10-19", "支出", 500, "购物", "外套"))

        assert len(book) == 3, f"len(book) 应为3，实际{len(book)}"
        amounts = [r.amount for r in book]
        assert amounts == [3000, 30, 500], f"for 遍历结果不对：{amounts}"

        assert book.delete(2) is True, "delete(2) 应返回 True"
        assert len(book) == 2, f"删除后应为2条，实际{len(book)}"
        assert [r.amount for r in book] == [3000, 500], "删错记录了"
        assert book.delete(99) is False, "删除不存在的编号应返回 False"
        print("  ✅ 通过\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # ---- 第3步：文件存取 ----
    print("第3步：save / load")
    try:
        book = AccountBook()
        book.add(Record("2026-10-18", "收入", 3000, "工资", "10月工资"))
        book.add(Record("2026-10-18", "支出", 30, "餐饮", "午饭"))
        book.save("test_records.json")

        book2 = AccountBook()
        book2.load("test_records.json")
        assert len(book2) == 2, f"读回应有2条，实际{len(book2)}"
        first = list(book2)[0]
        assert isinstance(first, Record), "读回的应是 Record 对象（from_dict 生效）"
        assert first.amount == 3000 and first.record_type == "收入"

        book3 = AccountBook()
        book3.load("不存在的文件.json")   # 不应该崩
        assert len(book3) == 0, "读取不存在的文件应得到空账本"
        print("  ✅ 通过（可以打开 test_records.json 看看，中文应该正常显示）\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    # ---- 第4步：统计 ----
    print("第4步：total / balance / filter_by_category")
    try:
        book = AccountBook()
        book.add(Record("2026-10-18", "收入", 3000, "工资", "10月工资"))
        book.add(Record("2026-10-18", "支出", 30, "餐饮", "午饭"))
        book.add(Record("2026-10-19", "支出", 500, "购物", "外套"))
        book.add(Record("2026-10-19", "收入", 100, "兼职", "稿费"))

        assert book.total("收入") == 3100, f"总收入应为3100，实际{book.total('收入')}"
        assert book.total("支出") == 530, f"总支出应为530，实际{book.total('支出')}"
        assert book.balance() == 2570, f"余额应为2570，实际{book.balance()}"

        food = book.filter_by_category("餐饮")
        assert len(food) == 1 and food[0].amount == 30, "按分类查找结果不对"
        print("  ✅ 通过\n")
    except Exception as e:
        print(f"  ❌ 报错：{e}\n")

    print("=== 测试结束 ===")
    print("全绿后，补全第5步菜单，然后运行：python practice_advanced_day7.py menu")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "menu":
        main()        # python practice_advanced_day7.py menu → 启动记账本
    else:
        run_tests()   # python practice_advanced_day7.py → 跑自动测试
