import pandas as pd

# 创建一个 DataFrame
data = {
    "姓名": ["小明", "小红", "小刚"],
    "成绩": [85, 92, 78],
    "年龄": [15, 16, 15]
}

df = pd.DataFrame(data)

print("这是一个 DataFrame：")
print(df)

# 简单统计
print("\n平均成绩：", df["成绩"].mean())
print("最高成绩：", df["成绩"].max())