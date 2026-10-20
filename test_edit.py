"""测试修改记录功能"""
import json

# 准备测试数据
test_records = [
    {"date": "2026-10-01", "type": "income", "amount": 5000, "category": "工资", "note": "10月工资"},
    {"date": "2026-10-05", "type": "expense", "amount": 35, "category": "餐饮", "note": "午饭"},
]

# 测试修改第1条记录
print("=== 修改前 ===")
for i, r in enumerate(test_records, 1):
    print(f"{i}: {r['date']} | {r['type']} | {r['amount']} | {r['category']} | {r['note']}")

# 模拟用户操作：修改编号2的记录
index = 2 - 1   # 用户输入2，减1变索引1
date = "2026-10-06"
type_ = "expense"
amount = 50.0
category = "餐饮"
note = "晚饭修改"

record = {
    "date": date,
    "type": type_,
    "amount": amount,
    "category": category,
    "note": note
}

test_records[index] = record

print("\n=== 修改后 ===")
for i, r in enumerate(test_records, 1):
    print(f"{i}: {r['date']} | {r['type']} | {r['amount']} | {r['category']} | {r['note']}")

# 验证结果
if test_records[1]["note"] == "晚饭修改" and test_records[1]["amount"] == 50.0:
    print("\n✅ 修改功能正确！")
else:
    print("\n❌ 修改功能有问题")

# 测试：输入无效编号会怎样？
print("\n=== 测试无效编号 ===")
try:
    test_records[999] = record   # 试试用不存在的索引
    print("❌ 居然没报错？不对")
except IndexError:
    print("✅ 无效编号会报 IndexError，需要加判断！")
