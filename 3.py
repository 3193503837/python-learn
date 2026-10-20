class Record:
    def __init__(self, date, record_type, amount, category, note):
        self.date = date
        self.record_type = record_type   # 走 setter，触发校验
        self.amount = amount             # 走 setter，触发校验
        self.category = category
        self.note = note

    @property
    def amount(self):
        return self._amount              # 私有名读数据

    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError("金额必须大于0")
        self._amount = value             # 私有名存数据

    @property
    def record_type(self):
        return self._record_type         # 私有名读数据

    @record_type.setter
    def record_type(self, value):
        if value != "收入" and value != "支出":
            raise ValueError("类型错误")
        self._record_type = value        # 私有名存数据

    def show(self):
        print(f"{self.date} | {self.record_type} | {self.amount}元 | {self.category} | {self.note}")

    def to_dict(self):
        return {
            "日期": self.date,
            "类型": self.record_type,
            "金额": self.amount,
            "分类": self.category,
            "备注": self.note
        }
record1=Record(2026,"收入",10,"打工","无")
print(record1.to_dict())
print(record1._amount)
print(record1.amount)