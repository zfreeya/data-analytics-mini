# def a (x):
#     print("欢迎来到黑马程序员！请出示您的健康吗以及72小时核酸证明，并配合测量体温！")
#     if x <= 37.5:
#         print(f"体温测量中，您的体温是：{x}度，体温正常请进！")
#     else:
#         print(f"体温测量中，您的体温是：{x}度，需要隔离！")
#
# a(37.3)
# a(39.3)
#
from xxsubtype import bench

#黑马ATM
money = 5000000
name = input("请输入姓名")
num = None

def inquire (hide_title) :
    """
    用于查询余额的函数
    :return:
    """
    if hide_title:
        print("------------查询余额------------")
        print(f"{name}，您好，您的余额剩余：{money}元。")
def save (save_money):
    """
    用于存款的函数
    :param save_money: 表示存款的数额
    :return:表示余额
    """
    print("------------存款------------")
    global money
    money += save_money
    print(f"{name},您好，您存款余额{save_money}元成功。")
    print(f"{name}，您好，您的余额剩余：{money}元。")
    inquire(False)
def take (take_money):
    """
    用于取款的函数
    :param take_money: 表示取款的数额
    :return: 表示余额
    """
    print("------------取款------------")
    global money
    money -= take_money
    if money < 0:
        print("余额不足，无法取款")
    else:
        print(f"{name},您好，您存款余额{take_money}元成功。")
        print(f"{name}，您好，您的余额剩余：{money}元。")
    inquire(False)
def main ():
    """
    主菜单函数
    :return: 跳转的菜单选择数字
    """
    print("------------主菜单------------")
    print(f"{name}您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")

    return input("请输入你的选择：")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        inquire(True)
        continue
    elif keyboard_input == "2":
        num = int(input("您想存多少钱："))
        save(num)
    elif keyboard_input == "3":
        num = int(input("您想取多少钱："))
        take(num)
    else:
        break




