"""测试记账本所有功能"""
import json
import sys
sys.path.insert(0, r"C:\Users\TvT\AppData\Roaming\TRAE SOLO CN\ModularData\ai-agent\work-mode-projects\6aab6d53c0c71ccc2d59ae27\python-learn")

# 先删除旧数据文件
import os
fname = r"C:\Users\TvT\AppData\Roaming\TRAE SOLO CN\ModularData\ai-agent\work-mode-projects\6aab6d53c0c71ccc2d59ae27\python-learn\records.json"
if os.path.exists(fname):
    os.remove(fname)

# 导入模块
import importlib.util
spec = importlib.util.spec_from_file_location("practice", r"C:\Users\TvT\AppData\Roaming\TRAE SOLO CN\ModularData\ai-agent\work-mode-projects\6aab6d53c0c71ccc2d59ae27\python-learn\practice_day14.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

records = mod.load_data()
print(f"初始记录数：{len(records)}（应为0）✅" if len(records)==0 else f"❌ 应为0，实际{len(records)}")

# 模拟添加记录
def mock_add(date, rtype, amount, category, note):
    inputs = [date, rtype, str(amount), category, note]
    original_input = __builtins__.input
    idx = [0]
    def fake_input(prompt=""):
        val = inputs[idx[0]]
        idx[0] += 1
        print(f"{prompt}{val}")
        return val
    __builtins__.input = fake_input
    try:
        mod.add_record(records)
    finally:
        __builtins__.input = original_input

print("\n--- 测试添加记录 ---")
mock_add("2026-10-01", "收入", 5000, "工资", "10月工资")
mock_add("2026-10-05", "支出", 35, "餐饮", "午饭")
print(f"记录数：{len(records)}（应为2）✅" if len(records)==2 else f"❌ 应为2，实际{len(records)}")

print("\n--- 测试查看记录 ---")
mod.show_records(records)

print("\n--- 测试统计 ---")
mod.show_stats(records)

print("\n--- 测试按分类筛选 ---")
original_input = __builtins__.input
__builtins__.input = lambda p="餐饮": (print(p + "餐饮"), "餐饮")[1]
mod.filter_by_category(records)
__builtins__.input = original_input

# 测试修改记录
print("\n--- 测试修改记录（修改金额） ---")
def fake_input_sequence(inputs_list):
    idx = [0]
    def fake(prompt=""):
        val = inputs_list[idx[0]]
        idx[0] += 1
        print(f"{prompt}{val}")
        return val
    return fake

__builtins__.input = fake_input_sequence(["1", "金额", "50"])
mod.change_record(records)
__builtins__.input = original_input

print(f"\n修改后第1条金额：{records[0]['金额']}（应为50.0）✅" if records[0]['金额']==50.0 else f"❌ 应为50.0，实际{records[0]['金额']}")

# 测试删除
print("\n--- 测试删除记录 ---")
__builtins__.input = fake_input_sequence(["2"])
mod.delete_record(records)
__builtins__.input = original_input

print(f"删除后记录数：{len(records)}（应为1）✅" if len(records)==1 else f"❌ 应为1，实际{len(records)}")

# 测试保存和加载
print("\n--- 测试保存和重新加载 ---")
mod.save_data(records)
records2 = mod.load_data()
print(f"重新加载后记录数：{len(records2)}（应为1）✅" if len(records2)==1 else f"❌ 应为1，实际{len(records2)}")
if len(records2) > 0:
    print(f"数据一致：{records[0] == records2[0]} ✅" if records[0]==records2[0] else "❌ 数据不一致")

print("\n🎉 所有测试完成！")
