#
# my_list=[1,2,3,4,5,6,7,8,9,10]
# index = 0
# my_list_2=[]
# my_list_3=[]
#
# while index < len(my_list):
#     element = my_list[index]
#     if element % 2 == 0:
#         my_list_2.append(element)
#     index +=1
#
#
# for element in my_list:
#     if element % 2 == 0:
#         my_list_3.append(element)
#
#
# print(my_list_2)
# print(my_list_3)


my_dict = {
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },
    "林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3
    },
    "张学友":{
        "部门":"科技部",
        "工资":4000,
        "级别":1
    },
    "刘德华":{
        "部门":"市场部",
        "工资":6000,
        "级别":2
    }
}

for name in my_dict:
    if my_dict[name]["级别"] == 1:
        name_dict = my_dict[name]
        name_dict["工资"] += 1000
        name_dict["级别"] = 2
        my_dict[name] = name_dict
print(my_dict)