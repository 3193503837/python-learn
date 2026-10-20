# ============================================
#  Day 14 毕业项目：个人记账本
# ============================================
#  这个项目会用到你两周学的所有知识：
#    变量、循环、列表、字典、函数、文件操作、异常处理
#
#  功能清单：
#    1. 添加收入/支出记录
#    2. 查看所有记录
#    3. 统计（总收入、总支出、余额）
#    4. 按类型筛选记录
#    5. 删除指定记录
#    6. 数据保存到文件（下次打开还在）
#    7. 退出程序
#
#  数据格式：每条记录是一个字典
#    {
#        "date": "2026-10-05",   # 日期
#        "type": "income",        # 类型：income=收入，expense=支出
#        "amount": 100,           # 金额
#        "category": "工资",      # 分类
#        "note": "10月工资"       # 备注
#    }
#
#  所有记录放在一个列表里：records = [{}, {}, {}...]
#  保存到 records.json 文件中
# ============================================

import json     # json 模块：把列表/字典存成文件，再读回来

FILE_NAME = "records.json"   # 数据文件名

# ---------- 功能1：加载数据 ----------
# 程序启动时，从文件读取之前保存的数据
# 如果文件不存在，返回空列表
# 提示：
#   try:
#       with open(FILE_NAME, "r", encoding="utf-8") as f:
#           return json.load(f)
#   except FileNotFoundError:
#       return []
def load_data():
    # 你的代码写在这里：
    try:
        with open(FILE_NAME,"r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []



# ---------- 功能2：保存数据 ----------
# 把 records 列表保存到文件里
# 提示：json.dump(records, f, ensure_ascii=False, indent=2)
#       ensure_ascii=False 让中文正常显示
#       indent=2 让格式好看
def save_data(records):
    # 你的代码写在这里：
    with open(FILE_NAME,"w",encoding="utf-8") as f:
        json.dump(records,f,ensure_ascii=False,indent=2)


# ---------- 功能3：添加记录 ----------
# 让用户输入：日期、类型、金额、分类、备注
# 组装成字典，添加到 records 列表
# 然后保存到文件
def add_record(records):
    print("\n=== 添加记录 ===")
    # 你的代码写在这里：
    date=input("日期：")
    type=input("类型：")
    try:
        amount=float(input("金额："))
    except ValueError:
        print("不是数字")
        return
    category=input("分类：")
    note=input("备注：")
    record={
        "日期":date,
        "类型":type,
        "金额":amount,
        "分类":category,
        "备注":note
    }
    records.append(record)
    save_data(records)
    print("添加成功")



    # 提示步骤：
    #   1. input 收集 date / type / amount / category / note
    #   2. 把 amount 转成 float（用 try/except 处理输入错误）
    #   3. 组装成字典 record = {...}
    #   4. records.append(record)
    #   5. save_data(records) 保存
    #   6. print("添加成功！")



# ---------- 功能4：查看所有记录 ----------
# 遍历 records 列表，逐条打印
# 如果没有记录，提示"暂无记录"
def show_records(records):
    print("\n=== 所有记录 ===")
    # 你的代码写在这里：
    if len(records) == 0:
        print("暂无记录")
        return
    for i,r in enumerate(records,1):
        print(f"{i}:{r['日期']}|{r['类型']}|{r['金额']}|{r['分类']}|{r['备注']}")

    # 提示：
    #   if len(records) == 0:
    #       print("暂无记录")
    #       return
    #   for i, r in enumerate(records, 1):
    #       print(f"{i}. {r['date']} | {r['type']} | {r['amount']} | {r['category']} | {r['note']}")



# ---------- 功能5：统计 ----------
# 计算总收入、总支出、余额
def show_stats(records):
    print("\n=== 统计 ===")
    # 你的代码写在这里：
    total_income=0
    total_expense=0
    for i in records:
        if i["类型"]=="收入":
            total_income+=i["金额"]
        else:
            total_expense+=i["金额"]
    rest=total_income-total_expense
    print(f"总收入:{total_income}")
    print(f"总支出:{total_expense}")
    print(f"余额:{rest}")
    # 提示：
    #   total_income = 0
    #   total_expense = 0
    #   for r in records:
    #       if r["type"] == "income":
    #           total_income += r["amount"]
    #       else:
    #           total_expense += r["amount"]
    #   balance = total_income - total_expense
    #   print(f"总收入：{total_income}")
    #   print(f"总支出：{total_expense}")
    #   print(f"余额：{balance}")



# ---------- 功能6：按分类筛选 ----------
# 让用户输入分类名称，只显示该分类的记录
def filter_by_category(records):
    print("\n=== 按分类筛选 ===")
    cato=input("请输入分类:")
    found=False
    for i in records:
        if i["分类"]==cato:
            print(f"{i['日期']}|{i['类型']}|{i['金额']}||{i['备注']}")
            found=True
    if not found:
            print("没有找到该分类")
    # 你的代码写在这里：
    # 提示：
    #   cat = input("请输入分类：")
    #   found = False
    #   for r in records:
    #       if r["category"] == cat:
    #           print(f"{r['date']} | {r['type']} | {r['amount']} | {r['note']}")
    #           found = True
    #   if not found:
    #       print("没有找到该分类的记录")



# ---------- 功能7：删除记录 ----------
# 显示所有记录（带编号），让用户输入编号删除
def delete_record(records):
    print("\n=== 删除记录 ===")
    # 你的代码写在这里：
    show_records(records)
    if len(records)==0:
        return
    index=int(input("请输入要删除的编号:"))-1
    if 0<=index<len(records):
        records.pop(index)
        save_data(records)
        print("删除成功！")
    else:
        print("输入无效！")

    # 提示：
    #   先调用 show_records(records) 显示所有记录
    #   if len(records) == 0: return
    #   index = int(input("请输入要删除的编号：")) - 1
    #   if 0 <= index < len(records):
    #       records.pop(index)
    #       save_data(records)
    #       print("删除成功！")
    #   else:
    #       print("编号无效")
def change_record(records):
    print("\n===修改记录===")
    show_records(records)
    if len(records)==0:
        return
    i=int(input("请选择要修改的编号："))-1
    if 0<=i<len(records):
        a=input("请选择要修改的部分：")
        try:
            if a == "所有":
                date = input("日期：")
                type = input("类型：")
                try:
                    amount = float(input("金额："))
                except ValueError:
                    print("不是数字")
                    return
                category = input("分类：")
                note = input("备注：")
                record = {
                    "日期": date,
                    "类型": type,
                    "金额": amount,
                    "分类": category,
                    "备注": note
                }
                records[i] = record
            elif a == "金额":
                try:
                    change = float(input(""))
                    records[i][a] = change
                except ValueError:
                    print("不是数字")
                    return
            else:
                change = input("")
                records[i][a] = change
            save_data(records)
            print("修改成功!")
        except KeyError:
            print("输入错误")
            return
    else:
        print("所输入的记录编号不存在!")



# ---------- 主菜单 ----------
def main():
    records = load_data()    # 启动时加载数据

    while True:
        print("\n" + "="*30)
        print("       个人记账本")
        print("="*30)
        print("1. 添加记录")
        print("2. 查看所有记录")
        print("3. 统计")
        print("4. 按分类筛选")
        print("5. 删除记录")
        print("6.修改记录")
        print("0. 退出")
        print("="*30)

        choice = input("请选择（0-6）：")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_records(records)
        elif choice == "3":
            show_stats(records)
        elif choice == "4":
            filter_by_category(records)
        elif choice == "5":
            delete_record(records)
        elif choice=="6":
            change_record(records)
        elif choice == "0":
            save_data(records)
            print("已保存，再见！")
            break
        else:
            print("输入无效，请重新选择")


# ---------- 程序入口 ----------
if __name__ == "__main__":
    main()


# ============================================
#  完成后运行：python practice_day14.py
#  试试看能不能正常记账、保存、退出再打开数据还在
#  写完告诉我检查！
# ============================================
