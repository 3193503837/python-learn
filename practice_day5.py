# ============================================
#  Day 5 练习题：if / elif / else + input()
# ============================================

# ---------- 第1题：成年判断 ----------
# 用 input() 接收用户输入的年龄
# 转成整数，判断是否成年（>= 18）
# 成年输出"你已成年"，未成年输出"你还未成年"
#
# 提示：age = int(input("请输入年龄："))

# 你的代码写在这里：
age=int(input("请输入年龄："))
if age>=18 :
    print("你已经成年")
elif age<18 :
    print("你未成年")



# ---------- 第2题：成绩等级判断 ----------
# 用 input() 接收分数（0-100），转成整数
# 90-100 → A（优秀）
# 80-89  → B（良好）
# 70-79  → C（中等）
# 60-69  → D（及格）
# 0-59   → F（不及格）
# 其他   → 输入无效
#
# 提示：注意条件从大到小排列

# 你的代码写在这里：
grade = int(input("你的成绩为："))
if grade < 0 or grade > 100:
    print("输入无效！成绩必须在 0-100 之间")
else:
    if grade >= 90:
        print("A（优秀）")
    elif grade >= 80:
        print("B（良好）")
    elif grade >= 70:
        print("C（中等）")
    elif grade >= 60:
        print("D（及格）")
    else:
        print("F（不及格）")





# ---------- 第3题：闰年判断 ----------
# 用 input() 接收一个年份，转成整数
# 闰年规则：
#   能被4整除且不能被100整除 → 闰年
#   或者能被400整除 → 闰年
# 输出"XX年是闰年"或"XX年不是闰年"
#
# 提示：用 and / or 组合条件
# 公式：(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 你的代码写在这里：
year=int(input("年份："))
is_leap=(year%4==0 and year%100!=0) or (year%400==0)
if is_leap==True:
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")


# ---------- 第4题：简易计算器 ----------
# 用 input() 接收两个数字和一个运算符（+ - * /）
# 根据运算符进行对应的计算
# 输出结果，比如：5 + 3 = 8
#
# 提示：
# num1 = float(input("请输入第一个数："))
# op = input("请输入运算符（+ - * /）：")
# num2 = float(input("请输入第二个数："))
# 然后用 if/elif/else 判断 op 是什么运算

# 你的代码写在这里：
num1=float(input("请输入第一个数:"))
op=input("请输入运算符:")
num2=float(input("请输入第二个数:"))
if op=="+":
    print(f"{num1}+{num2}={num1 + num2}")
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)




# ---------- 第5题：BMI 健康计算器（挑战） ----------
# 用 input() 接收身高（米）和体重（公斤）
# 计算 BMI = 体重 / (身高 * 身高)
# 根据BMI判断：
#   BMI < 18.5      → 偏瘦
#   18.5 <= BMI < 24 → 正常
#   24 <= BMI < 28   → 偏胖
#   BMI >= 28        → 肥胖
# 输出："你的BMI是XX.XX，属于XX"
#
# 提示：注意 BMI 是浮点数，保留两位小数可以用 round(bmi, 2)

# 你的代码写在这里：
h=eval(input("请输入身高（米）："))
w=eval(input("请输入体重（公斤）："))
BMI=w/(h*h)
print(f"你的BMI是{BMI}")
if BMI<18.5:
    print("偏瘦")
elif 18.5<BMI<24:
    print("正常")
elif 24<BMI<28 :
    print("偏胖")
elif BMI>=28 :
    print("肥胖")
# ============================================
#  写完后运行：python practice_day5.py
#  然后告诉我检查，或者贴输出给我看
# ============================================
