# ============================================
#  Day 9 练习题：列表进阶 + 元组
# ============================================

# ---------- 第1题：排序练习 ----------
# 列表：nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 1. 输出原始列表
# 2. 升序排序后输出
# 3. 降序排序后输出
# 4. 输出最大值、最小值、总和
#
# 提示：sort() 会修改原列表；sorted() 返回新列表，不修改原列表
#       max() / min() / sum() 内置函数

# 你的代码写在这里：
nums=[3,1,4,1,5,9,2,6,5,3,5]
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# ---------- 第2题：enumerate 遍历 ----------
# 列表：fruits = ["苹果", "香蕉", "橙子", "葡萄", "芒果"]
# 用 enumerate() 输出每个元素的序号和名称，格式：
#   第1个水果是：苹果
#   第2个水果是：香蕉
#   ...
#
# 提示：for i, fruit in enumerate(fruits, 1):
#       i 从 1 开始计数

# 你的代码写在这里：
fruits=["苹果","香蕉","橙子","葡萄","芒果"]
for i,fruit in enumerate(fruits,1):
    print(f"第{i}个水果是：{fruit}")

# ---------- 第3题：列表推导式 ----------
# 用列表推导式生成 1-20 中所有偶数的平方，存入列表 squares
# 例如：[4, 16, 36, ... , 400]
#
# 提示：[x**2 for x in range(2, 21, 2)]
#       或者：[x**2 for x in range(1, 21) if x % 2 == 0]

# 你的代码写在这里：
squares=[i**2 for i in range(1,21) if i%2==0]
print(squares)
# ---------- 第4题：元组练习 ----------
# 1. 创建元组：info = ("小明", 20, 1.75, True)
# 2. 输出元组
# 3. 输出第2个元素
# 4. 尝试修改第2个元素（看看会不会报错）
# 5. 把元组转成列表，修改后再转回元组
#
# 提示：tuple() 和 list() 可以互相转换

# 你的代码写在这里：
info=("小明",20,1,1.75,True)
print(info)
print(info[1])
t=list(info)
t[1]=200
info=tuple(t)
print(info)

# ---------- 第5题：成绩统计系统 ----------
# 列表：scores = [85, 92, 78, 60, 95, 88, 72, 81, 90, 65]
# 完成以下功能：
#   1. 输出最高分、最低分、平均分（保留1位小数）
#   2. 输出及格人数（>=60）和及格率
#   3. 按分数从高到低排序输出
#   4. 用 enumerate 输出排名（第1名：XX分 ...）
#
# 提示：及格人数用 for 循环统计，或者列表推导式 len([s for s in scores if s>=60])

# 你的代码写在这里：
scores=[85,92,78,60,95,88,72,81,90,65]
max_=max(scores)
min_=min(scores)
avg=sum(scores)/len(scores)
a=0
print(f"最高分:{max_}  最低分:{min_}  平均分:{avg:.1f}")
for i in scores:
    if i>=60:
        a+=1
rate=a/len(scores)
print(f"及格人数为:{a}")
print(f"及格率：{rate:.1f}")
scores.sort(reverse=True)
print(f"由高到低：{scores}")
for m,score in enumerate(scores,1):
    print(f"第{m}名：{score}")

# ============================================
#  写完后运行：python practice_day9.py
#  然后告诉我检查
# ============================================
