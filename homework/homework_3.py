# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)
#
#
# import random
# num=random.randint(1,100)
# guess = int(input("猜猜数字是多少："))
# i=0
#
# while guess!=num:
#     if guess < num:
#         print("小了")
#     else:
#         print("大了")
#     i += 1
#     guess = int(input("猜猜数字是多少："))
#
# print("恭喜你猜对了！")
# print("你已经猜了", i, "次")
#

# i = 1
# while i <= 9:
#
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={j*i}\t",end='' )
#         j += 1
#     i += 1
#     # 换行
#     print()
#

# i = 0
# name = "itheima is a brand of itcast"
# for x in name:
#     if x == "a":
#         i += 1
# print(i)

# num=0
# for x in range(1,100):
#     if x%2==0:
#         num += 1
# print(num)
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}\t",end='')
#     print()
#
#

import random
money = 10000

for worker in range(1,21):
    num = random.randint(0, 10)
    if num >= 5:
        money -= 1000
        print(f"向员工{worker}发放工资1000元，账户余额还剩{money}元。")
        if money == 0:
            break

    else:
        print(f"员工{worker}，绩效分{num}，低于5，不发工资，下一位。")


print("工资发完了，下个月再发吧。")
