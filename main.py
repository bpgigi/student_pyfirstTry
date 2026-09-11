from chapter01.lesson01 import EduManagement
edu = EduManagement()
#
# while True:
#     edu.show()
#     option = int(input("请输入要进行的操作"))
#     match option:
#         case 1:
#             edu.add_student()
#         case 2:
#             edu.update_student()
#         case 3:
#             edu.delete_student()
#         case 4:
#             edu.search_student()
#         case 5:
#             edu.show_all_student()
#         case 6:
#             break
# #怎么链接两个
# file = open("使用说明.txt","r",encoding="utf-8")
# print(file.read())
# file.close()
# with open("使用说明.txt","r",encoding="utf-8") as f:
#     print(f.read())
# file = open('使用说明.txt', 'r', encoding='utf-8')
# for line in file:
#     print(line, end='')
# file.close()
# file = open("使用说明.txt","r",encoding="utf-8")
# lines = file.readlines()
# for line in lines:
#     print(line,end="")
# file.close()
# file = open("学生信息.txt","a",encoding="utf-8")
# # file.write("\n")
# # file.write(input("\n请输入学生名字"))
# #file.write("\n",input("\n请输入学生名字"))
# #一下为gpt教我的
# # name = input("请输入学生名字")
# # file.write("\n" + name)
# # file.write("\n" + input("输入"))
# # file.write(f"\n{input("ad")}") --->单引号双引号匹配错误
# file.write(f"\n{input('ad')}")
# file.close()
# f = open("学生信息.txt","r",encoding="utf-8")
# print(f.read())

#异常
file = None
try:
    file = open('lesson01.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print("无法打开指定文件!")
except LookupError:
    print("指定了位置编码")
except UnicodeDecodeError:
    print("读取文件是解码错误")
finally:
    if file:
        file.close()

