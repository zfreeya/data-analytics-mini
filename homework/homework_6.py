f = open("D:/bili.txt","r",encoding="UTF-8")
new_list = f.readlines()
new_list_2 = [line for line in new_list if "测试" not in line]
f.close()

f = open("D:/bili.txt.bak","w",encoding="UTF-8")
f.writelines(new_list_2)
f.close()