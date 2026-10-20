# ============================================
#  Day 11 练习题：字符串进阶 + 集合
# ============================================

# ---------- 第1题：字符串方法练习 ----------
# 字符串：s = "  Hello World!  "
# 1. 输出去掉两边空格后的字符串
# 2. 输出全大写的字符串
# 3. 输出全小写的字符串
# 4. 把 "World" 替换成 "Python" 后输出
# 5. 判断字符串是否以 "Hello" 开头（注意有空格）
#
# 提示：strip() / upper() / lower() / replace() / startswith()

# 你的代码写在这里：
s=" Hello World"
print(s.strip())
print(s.upper())
print(s.lower())
print(s.replace("World","Python"))
print(s.strip().startswith("Hello"))


# ---------- 第2题：分割与拼接 ----------
# 字符串：s = "苹果,香蕉,橙子,葡萄"
# 1. 用逗号分割成列表
# 2. 输出列表
# 3. 用 " + " 把列表重新拼成字符串
# 4. 输出拼接后的字符串
#
# 提示：split(",")  分割
#       "连接符".join(列表)  拼接

# 你的代码写在这里：
s="苹果,香蕉,橙子,葡萄"
s=s.split(",")
print(s)
s="+".join(s)
print(s)


# ---------- 第3题：统计字符出现次数 ----------
# 字符串：s = "hello world hello python"
# 1. 统计字母 "o" 出现了几次
# 2. 统计字母 "l" 出现了几次
# 3. 用 for 循环遍历，统计每个字符出现的次数（用字典存结果）
#
# 提示：s.count("o")  可以直接查次数
#       字典方式：result[char] = result.get(char, 0) + 1

# 你的代码写在这里：
s="hello world hello python"
print(s.count("o"))
print(s.count("l"))
result={}
for char in s:
    result[char]=result.get(char,0)+1
print(result)


# ---------- 第4题：集合操作练习 ----------
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# 1. 给 set1 添加元素 6
# 2. 从 set2 删除元素 8
# 3. 输出两个集合的交集（都有的元素）
# 4. 输出两个集合的并集（合在一起去重）
# 5. 输出 set1 - set2 的差集（set1有set2没有）
#
# 提示：add() / remove()
#       & 交集  | 并集  - 差集

# 你的代码写在这里：
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set1.add(6)
set2.remove(8)
print(set1&set2)
print(set1|set2)
print(set1-set2)


# ---------- 第5题：列表去重 + 统计 ----------
# 列表：nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 1. 把列表转成集合去重
# 2. 输出去重后的元素（转成列表）
# 3. 输出去重后元素的个数
# 4. 用字典统计每个数字出现的次数
# 5. 输出出现次数最多的数字和次数
#
# 提示：set() 去重
#       统计用字典 + for 循环

# 你的代码写在这里：
nums=[3,1,4,1,5,9,2,6,5,3,5]
a=list(set(nums))
print(a)
print(len(a))
times={}
for num in nums:
    times[num]=times.get(num,0)+1
print(times)
max_num=None
max_time=0
for num,time in times.items():
    if time>max_time:
        max_time=time
        max_num=num
print(f"最多的数字是{max_num},出现了{max_time}次")
# ============================================
#  写完后运行：python practice_day11.py
#  然后告诉我检查
# ============================================
