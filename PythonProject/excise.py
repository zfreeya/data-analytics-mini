from tkinter.font import names

students=[
    {"name":"xx","age":"12","score":"99"},
    {"name":"yy","age":"16","score":"90"},
    {"name":"zz","age":"15","score":"80"},
    {"name":"aa","age":"18","score":"85"},
    {"name":"bb","age":"14","score":"95"}
]

for stu in students:
    print(stu["name"],"的分数是",stu["score"])

total=0
for stu in students:
    total += int(stu["score"])

avg = total/len(students)
print("平均数是",avg)

top_student=max(students,key=lambda x:x["score"])
print("最高分是",top_student["name"],top_student["score"])

def top_student(students):

