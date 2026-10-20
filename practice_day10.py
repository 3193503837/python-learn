# ============================================
#  Day 10 练习题：字典（dict）
# ============================================

# ---------- 第1题：创建字典 ----------
# 创建一个字典 student，包含以下信息：
#   name = "小明", age = 20, height = 1.75, is_student = True
# 1. 输出整个字典
# 2. 输出 name 和 height
# 3. 用 get() 输出 weight（不存在时显示"未填写"）
#
# 提示：dict["key"] 或 dict.get("key", "默认值")

# 你的代码写在这里：
student= {"name":"小明","age":20,"height":1.75,"is_student":True}
print(student)
print(student["name"],student["height"])
print(student.get("weight","未填写"))
# ---------- 第2题：增删改查 ----------
# 初始字典：book = {"title": "Python入门", "author": "张三", "price": 50}
# 1. 新增 publisher = "清华大学出版社"
# 2. 修改 price = 65
# 3. 删除 author
# 4. 判断 "price" 是否在字典中，输出结果
# 5. 每一步操作后 print() 输出字典
#
# 提示：dict[新键]=值, del dict[键], 键 in dict

# 你的代码写在这里：
book={"title":"Python入门","author":"张三","price":50}
book["publisher"]="清华大学出版社"
book["author"]="李四"
del book["author"]
if "price" in book:
    print("有price这个键")
print(book)
# ---------- 第3题：遍历字典 ----------
# 字典：scores = {"语文": 85, "数学": 92, "英语": 78, "物理": 90}
# 1. 用 items() 遍历，输出格式：语文：85分
# 2. 输出所有科目（keys）
# 3. 输出所有分数（values）
# 4. 计算总分和平均分（保留1位小数）
#
# 提示：for key, value in dict.items()
#       sum(dict.values()) 可以直接求和

# 你的代码写在这里：
scores={"语文":85,"数学":92,"英语":78,"物理":90}
for key,value in scores.items():
    print(f"{key}:{value}分")
for key in scores.keys():
    print(key)
for value in scores.values():
    print(value)
a=sum(scores.values())
b=len(scores.keys())
print(f"总分：{a}")
print(f"平均分：{a/b:.1f}")
# ---------- 第4题：商品价格查询 ----------
# 字典：prices = {"苹果": 5, "香蕉": 3, "橙子": 4, "葡萄": 8}
# 1. 让用户输入一个水果名
# 2. 如果存在，输出价格
# 3. 如果不存在，输出"抱歉，没有该水果"
# 4. 输出所有水果列表供用户参考
#
# 提示：用 in 判断键是否存在
#       用 dict.keys() 列出所有水果

# 你的代码写在这里：
fruits={"苹果":5,"香蕉":3,"橙子":4,"葡萄":8}
fruit=input("水果：")
if fruit in fruits:
    print(f"价格：{fruits[fruit]}")
else:
    print("抱歉，没有该水果")
for key,value in fruits.items():
    print(f"{key}:{value}")


# ---------- 第5题：通讯录系统（挑战） ----------
# 用嵌套字典做一个简易通讯录：
# contacts = {
#     "小明": {"phone": "123456789", "city": "北京"},
#     "小红": {"phone": "987654321", "city": "上海"}
# }
# 1. 输出所有联系人名字
# 2. 输入名字，查到则输出电话和城市，查不到提示"无此人"
# 3. 新增一个联系人"小刚"，信息自定
# 4. 删除联系人"小红"
# 5. 每步操作后 print() 输出通讯录
#
# 提示：contacts["小明"]["phone"]  先找联系人，再找字段

# 你的代码写在这里：
contact={"小明":{"phone":"123456789","city":"北京"},
         "小红":{"phone":"987654321","city":"上海"}
         }
print(contact.keys())
name=input("查询联系人:")
if name in contact:
    print(f"电话:{contact[name]['phone']},城市:{contact[name]['city']}")
else:
    print("查无此人")
contact["小刚"]={"phone":"445566777","city":"茂名"}
del contact["小红"]
print(contact)


# ============================================
#  写完后运行：python practice_day10.py
#  然后告诉我检查
# ============================================
