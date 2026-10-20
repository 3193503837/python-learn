# ============================================
#  Day 13 练习题：文件操作 + 异常处理
# ============================================

# ---------- 第1题：写入文件 ----------
# 用 "w" 模式创建一个 poem.txt 文件
# 写入一首古诗《静夜思》，共4行：
#   床前明月光
#   疑是地上霜
#   举头望明月
#   低头思故乡
#
# 提示：with open("poem.txt", "w", encoding="utf-8") as f:
#       f.write("内容\n")   \n 表示换行

# 你的代码写在这里：
with open("poem.txt","w",encoding="utf-8") as f:
    f.write("窗前明月光\n")
    f.write("疑似地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")


# ---------- 第2题：读取文件 ----------
# 读取上面创建的 poem.txt
# 方式任选：read() / readlines() / for line in f
# 把内容逐行输出到屏幕
#
# 提示：with open("poem.txt", "r", encoding="utf-8") as f:

# 你的代码写在这里：
with open("poem.txt","r",encoding="utf-8")as f:
    for line in f.readlines():
        print(line.strip())



# ---------- 第3题：追加写入 ----------
# 用 "a" 模式在 poem.txt 末尾追加两行：
#   ——李白《静夜思》
#   （唐诗三百首）
# 然后再读出来验证一下
#
# 提示："a" = append 追加模式，不会清空原有内容

# 你的代码写在这里：
with open("poem.txt","a",encoding="utf-8")as f:
    f.write("——李白《静夜思》")
    f.write("(唐诗三百首)")
with open("poem.txt","r",encoding="utf-8")as f:
    content = f.read()
    print(content)
# ---------- 第4题：异常处理 ----------
# 写一个除法程序：
#   让用户输入两个数字
#   输出它们的商
#   用 try/except 处理两种错误：
#     1. ValueError：输入不是数字
#     2. ZeroDivisionError：除数为0
#
# 提示：
#   try:
#       可能出错的代码
#   except ValueError:
#       print("输入不是数字")
#   except ZeroDivisionError:
#       print("除数不能为0")

# 你的代码写在这里：
try:
    a=int(input("第一个数字:"))
    b=int(input("第二个数字:"))
    print(f"{a}/{b}={a/b}")
except ValueError:
    print("不是数字")
except ZeroDivisionError:
    print("除数不能为0")


# ---------- 第5题：智能记事本（挑战） ----------
# 做一个简单的记事本程序，功能：
#   1. 查看笔记（读取 note.txt 并显示）
#   2. 添加笔记（在 note.txt 末尾追加一行）
#   3. 退出程序
# 用 while 循环做菜单，用户选择功能
# 文件不存在时要处理 FileNotFoundError
#
# 提示：
#   while True:
#       print("1.查看 2.添加 3.退出")
#       choice = input("请选择：")
#       if choice == "1":
#           ...查看...
#       elif choice == "2":
#           ...添加...
#       elif choice == "3":
#           break

# 你的代码写在这里：
def check():
    try:
        with open("note.txt","r",encoding="utf-8")as f:
            for line in f.readlines():
                print(line.strip())
    except FileNotFoundError:
        print("文件不存在")
def add():
    with open("note.txt","a",encoding="utf-8")as f:
        a=input("")
        f.write(a)
while True:
    print("1:查看;2:添加;3:退出")
    choice=input("请选择:")
    if choice=="1":
        check()
    elif choice=="2":
        add()
    elif choice=="3":
        break

# ============================================
#  写完后运行：python practice_day13.py
#  然后告诉我检查
# ============================================
