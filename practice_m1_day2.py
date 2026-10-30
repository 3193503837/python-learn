# ============================================
# 第 1 月 · Day 2 练习：多线程 threading
# ============================================
# 今天的目标：搞懂"让多个任务看起来同时在跑"到底是怎么做到的
#   - 线程怎么创建、怎么等它跑完（join）
#   - 为什么共享变量会算错（竞态条件）→ 用锁修好
#   - 守护线程是什么
#   - 实战：用多线程并发读取多个账单文件

import threading
import time
import json
import os
from concurrent.futures import ThreadPoolExecutor

# ==============================
# 示例：线程的基本用法（看懂即可，不用改）
# ==============================
# Thread(target=函数, args=(参数元组,))  把函数丢给一个新线程去跑
# t.start()  启动线程（立刻返回，不等函数跑完）
# t.join()   等这个线程跑完（阻塞主线程）

def demo_basic():
    print("--- 示例：start 与 join ---")

    def download(name, seconds):
        time.sleep(seconds)                    # 模拟网络/磁盘等待
        print(f"  {name} 下载完成")

    start = time.time()
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=download, args=(f"文件{i}", 0.3))
        threads.append(t)
        t.start()                              # 三个任务几乎同时开始等

    for t in threads:
        t.join()                               # 等全部结束

    elapsed = time.time() - start
    print(f"  总耗时 {elapsed:.2f} 秒（串行需要 0.9 秒左右）\n")


# ==============================
# 第1题：不 join 会怎样？
# ==============================
# 要求：补全 run_without_join()
#   - 创建 3 个线程，每个执行 download_one(i)（已给你写好）
#   - 只 start，不 join
#   - 函数直接 return 当前时间戳
#
# 期望现象：主线程马上返回，而 3 个子线程的"下载完成"在之后才打印
#         甚至可能整个程序已经结束了它们才打印（或根本没打印完）
#
# 提示：join 的作用就是"排队等它"。不 join，主线程不会等子线程。

def download_one(i):
    time.sleep(0.3)
    print(f"  [线程{i}] 下载完成")


def run_without_join():
    # 你的代码写在这里
    start = time.time()
    threads=[]
    for i in range(1, 4):
        t=threading.Thread(target=download_one,args=(i,))
        threads.append(t)
        t.start()
    times=time.time()-start
    print(f"总耗时:{times:.2f}秒")



# ==============================
# 第2题：用多线程压缩总耗时
# ==============================
# 要求：补全 concurrent_run(tasks)
#   - tasks 是 [(名字, 秒数), ...] 这样的列表，比如 [("A", 0.3), ("B", 0.3)]
#   - 每个任务用一个线程跑 download_one 里的 sleep（可复用 sleep_task）
#   - 全部 join 之后再返回总耗时（float，秒）
#
# 验收：3 个 0.3 秒的任务，返回值应 < 0.7（串行要 0.9）
#
# 提示：
#   start = time.time()
#   ... 创建并 start 所有线程 ...
#   ... 全部 join ...
#   return time.time() - start

def sleep_task(name, seconds):
    time.sleep(seconds)

arr=[]
def concurrent_run(tasks):
    # 你的代码写在这里
    pass
    start = time.time()
    for i,m in tasks:
        t=threading.Thread(target=sleep_task, args=(i,m))
        t.start()
        arr.append(t)
    for t in arr:
        t.join()
    times = time.time() - start
    return times



# ==============================
# 第3题：亲手制造一个 bug（竞态条件）
# ==============================
# 要求：补全 unsafe_increment(times)
#   - 全局变量 counter 初始为 0
#   - 创建 4 个线程，每个线程把 counter 加 times 次（times 默认 50000）
#   - 全部 join 后返回 counter
#   - 不要加锁！
#
# 期望现象：最终结果通常小于 4 * times
#   原因：counter += 1 在底层是"读 → 加 → 写"三步，
#        两个线程可能同时读到同一个旧值，导致其中一次加法被覆盖
#
# 提示：函数里要声明 global counter 才能修改全局变量

counter = 0


def add(times=50000):
    global counter
    for i in range(1,times+1):
        v=counter
        time.sleep(0.00001)        # 写成多少都一样：Windows 实际会睡约 0.6ms
        counter =v + int(1)

def unsafe_increment(times=50000):
    # 你的代码写在这里
    threads = []
    global counter
    counter = 0
    for i in range(4):
        t=threading.Thread(target=add, args=(times,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    return counter




# ==============================
# 第4题：加锁修复
# ==============================
# 要求：补全 safe_increment(times)，逻辑同第3题，但用 threading.Lock 保护
#   - 在函数内创建 lock = threading.Lock()
#   - 每次修改 counter 时 with lock:（或者 lock.acquire()/release()）
#   - 结果必须恰好等于 4 * times
#
# 提示：with lock: 只包住"读-加-写"这三步，不要包住整个循环
#       包太大就等于没并发了（虽然结果正确）
lock = threading.Lock()
def add_new(times=50000):
    global counter
    for i in range(1,times+1):
        with lock:
            v=counter
            time.sleep(0.00001)    # 和 add() 保持一致
            counter =v + int(1)

def safe_increment(times=50000):
    # 你的代码写在这里
    threads = []
    global counter
    counter = 0
    for i in range(4):
        t = threading.Thread(target=add_new, args=(times,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    return counter





# ==============================
# 第5题：守护线程
# ==============================
# 要求：补全 start_daemon()
#   - 创建一个线程，执行下面的 heartbeat()（无限循环，每 0.2 秒打印一次）
#   - 把这个线程设为守护线程（daemon=True，可以在创建时传参，也可以 t.daemon = True）
#   - start 之后返回这个线程对象（不要 join！）
#
# 期望现象：主线程结束时，这个"心跳"线程会被强制结束，程序不会卡住
# 对比：如果是普通线程（daemon=False），主线程会一直等它，程序永远不退出

def heartbeat():
    while True:
        print("  ♥ 心跳...")
        time.sleep(0.2)


def start_daemon():
    t=threading.Thread(target=heartbeat,daemon=True)
    t.start()
    return t                 # ⚠️ 少了这行：不写 return，函数返回 None


# ==============================
# 第6题：实战——并发读取多个账单文件
# ==============================
# 背景：记账本以后可能有几十个用户，每人一个 json 文件，
#       串行读太慢，用多线程并发读
#
# 要求：补全 read_all_concurrent(paths)
#   - paths 是 json 文件路径列表
#   - 为每个文件创建一个线程，执行 read_one(path)（已给你写好）
#   - 把每个线程的结果收集到同一个列表 results 里
#   - 全部 join 后返回 results
#
# 验收：3 个文件、每个 1 条记录，总金额应等于 3 条记录金额之和
#
# 思考（写进笔记）：多个线程往同一个 list 里 append，需要加锁吗？
#   答案是不需要——list.append 是原子操作（GIL 保护单个字节码级别操作）。
#   但 counter += 1 就需要，因为它是多步操作。

def read_one(path,results):
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
    # records 是"记录列表"，不是单条记录，不能直接 records["金额"]
    for r in records:
        results.append(r["金额"])      # append 是原子操作，多线程写不用加锁


def read_all_concurrent(paths):
    results = []
    threads = []
    for path in paths:
        t = threading.Thread(target=read_one, args=(path, results))
        threads.append(t)      # ⚠️ 忘了 append，下面的 join 就是空循环
        t.start()
    for t in threads:
        t.join()
    return sum(results)



def create_test_books():
    """测试用：生成 3 个账单 json 文件，返回路径列表（不用改）"""
    books = {
        "m1_book_a.json": [{"日期": "2026.10.01", "类型": "支出", "金额": 20.0, "分类": "餐饮", "备注": "无"}],
        "m1_book_b.json": [{"日期": "2026.10.02", "类型": "支出", "金额": 40.0, "分类": "交通", "备注": "无"}],
        "m1_book_c.json": [{"日期": "2026.10.03", "类型": "支出", "金额": 60.0, "分类": "购物", "备注": "无"}],
    }
    base = os.path.dirname(os.path.abspath(__file__))
    paths = []
    for name, records in books.items():
        path = os.path.join(base, name)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=4)
        paths.append(path)
    return paths


# ============================================
#  测试区（不用改下面的代码）
# ============================================
if __name__ == "__main__":
    print("=== Day 2 多线程练习 ===\n")

    demo_basic()


    # 第1题：不 join 的现象
    print("--- 第1题：不 join 会怎样 ---")
    t0 = time.time()
    run_without_join()
    print("  主线程已经执行完毕（注意看下面几行是不是才打印）")
    time.sleep(0.5)  # 给子线程一点时间把话说完
    print("")

    # 第2题：并发压缩耗时
    print("--- 第2题：并发跑 3 个 0.3 秒任务 ---")
    try:
        elapsed = concurrent_run([("A", 0.3), ("B", 0.3), ("C", 0.3)])
        assert elapsed is not None, "concurrent_run 还没有实现"
        assert elapsed < 0.7, f"耗时 {elapsed:.2f}s，说明还是串行跑的，检查是否真的用了线程"
        print(f"  ✅ 耗时 {elapsed:.2f}s，并发生效（串行需要 0.9s）")
    except AssertionError as e:
        print(f"  ❌ {e}")
    print("")

    # 第3题：竞态条件
    print("--- 第3题：无锁并发累加（期望出现偏差）---")
    counter = 0
    result = unsafe_increment(2000)          # 2000 次约 1.1 秒
    if result is None:
        print("  ❌ unsafe_increment 还没有实现")
    elif result == 8000:
        print(f"  ⚠️  这次恰好等于 8000（sleep 版不该出现，检查读-睡-写三步）")
    else:
        print(f"  ✅ 结果 {result} < 8000，成功复现竞态（少了 {8000 - result} 次，通常丢 3/4）")
    print("")

    # 第4题：加锁
    print("--- 第4题：加锁修复 ---")
    result = safe_increment(500)             # 加锁后变串行，500 次约 1.2 秒
    if result is None:
        print("  ❌ safe_increment 还没有实现")
    elif result == 2000:
        print(f"  ✅ 结果恰好 {result}，锁生效")
    else:
        print(f"  ❌ 结果 {result}，不是 2000，锁没有覆盖到所有修改")
    print("")

    # 第5题：守护线程
    print("--- 第5题：守护线程 ---")
    t = start_daemon()
    if t is None:
        print("  ❌ start_daemon 还没有实现")
    else:
        time.sleep(0.5)
        print(f"  主线程结束时心跳线程还活着：{t.is_alive()}")
        print(f"  是否守护线程：{t.daemon}（应为 True，程序不会因为它卡住）")
    print("")

    # 第6题：并发读账单
    print("--- 第6题：并发读取 3 个账单文件 ---")
    paths = create_test_books()
    total = read_all_concurrent(paths)
    if total is None:
        print("  ❌ read_all_concurrent 还没有实现")
    else:
        if abs(total - 120.0) < 0.01:
            print(f"  ✅ 总金额 {total}，与期望 120.0 一致")
        else:
            print(f"  ❌ 总金额 {total}，期望 120.0")
    print("")

    print("=== 测试结束 ===")
