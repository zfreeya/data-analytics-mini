# print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
# age=int(input("请输入你的年龄："))
# if age >= 18:
#     print("您已成年，游玩需要补票10元。")
# print("祝您游玩愉快。")
#
# print("欢迎来到黑马动物园")
# height=int(input("请输入你的身高（cm）："))
# if height > 120:
#     print("您的身高超过120cm，游玩需要购票10元。")
# else :
#     print("您的身高未超出120cm，可以免费游玩。")
# print("祝您游玩愉快。")
#
# number=2
# if int(input("请输入第一次猜想的数字：")) ==number:
#     print("恭喜第一次就猜对了。")
# elif int(input("不对，再猜一次："))==number:
#     print("恭喜第二次猜对了。")
# elif int(input("不对再猜最后一次："))==number:
#     print("恭喜猜对了。")
# else:print("很遗憾都没猜对，蠢猪。")
#
#
#
#
# age=int(input("请输入你的年龄："))
# time=int(input("请输入你的入职时间："))
# level=int(input("请输入你的等级："))
#
# if age >= 18:
#     if age < 30:
#         print("年龄符合标准")
#         if time > 2:
#             print("可以领取礼物")
#         elif level > 3:
#             print("可以领取礼物。")
#     else:
#             print("不符合条件，不能领取。")
#
# else:
#     print("不能领取。")


import random
from random import randint

number = randint(1,10)
print("一共有三次机会，每次猜不中，系统会提示大了或小了")
guess_1 = int(input("猜猜数字是多少:"))

if guess_1 != number:
    if guess_1 > number:
        print("大了")
    elif guess_1 < number:
        print("小了")
else:
    print("我靠这么聪明一次就猜对了！")

guess_2 = int(input("再猜一次："))
if guess_2 != number:
    if guess_2 > number:
        print("大了")
    elif guess_2 < number:
            print("小了")
    else:
        print("嘻嘻猜对了！")
guess_3 = int(input("还有最后一次机会："))
if guess_3 == number:
    print("第三次终于猜对了！")
else:
    print("蠢猪三次都猜错了！！")


