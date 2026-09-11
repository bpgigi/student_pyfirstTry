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
with open("使用说明.txt","r",encoding="utf-8") as f:
    print(f.read())