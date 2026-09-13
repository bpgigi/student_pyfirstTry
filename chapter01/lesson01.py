# class Student:
#     def __init__(self, name,chinese,math,english):
#         self.name = name
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#     #没想到
#     def __str__(self):
#         #print(f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}")
#         return f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}"
#     #更没想到
#     def __repr__(self):
#         return self.__str__()
#     #def update_score(self,name,c=None,m=None,e=None):   修改不用确定name
#     def update_score(self,c=None,m=None,e=None):
#         if c is not None:
#             self.chinese=c
#         if m is not None:
#             self.math=m
#         if e is not None:
#             self.english=e
#
# class EduManagement:
#     def __init__(self):
#         # self.stu = []
#         self.stu_list = []
#
#     def show(self):
#         print("-"*20)
#         print("1.添加学生成绩")
#         print("2.修改学生成绩")
#         print("3.删除学生成绩")
#         print("4.查询学生成绩")
#         print("5.展示全部学生成绩")
#         print("6.退出系统")
#         print("-" * 20)
#         #option = int(input("请输入要进行的操作"))
#     #添加学生，名字不存在，成绩在0-100
#     #def add_student(self):
#     def add_student(self):
#         print(f"添加前学生列表：{self.stu_list}")
#         n = input("请输入学生名字")
#         # if n not in self.stu:
#         #     self.stu.append(n)
#         # else :
#         #     return
#         for s in self.stu_list:
#             if s.name == n:
#                 print("学生存在，添加失败")
#                 return
#
#         c = int(input("请输入学生语文成绩"))
#         m = int(input("请输入学生数学成绩"))
#         e = int(input("请输入学生英语成绩"))
#         if 1 <= c <= 100 and 1 <= m <= 100 and 1 <= e <= 100:
#             self.stu_list.append(Student(n,c,m,e))
#             print(f"添加后学生列表：{self.stu_list}")
#             stu_list = []
#             with open("stu_data.json", 'w') as f:
#                 for s in edu.stu_list:
#                     stu_dict = {
#                         "name": s.name,
#                         "chinese": s.chinese,
#                         "math": s.math,
#                         "english": s.english,
#                     }
#                     stu_list.append(stu_dict)
#             return
#         else:
#             print("添加失败，成绩必须在0-100！")
#
#     #def fix_student(self,name,chinese=None,math=None,english=None):
#     def update_student(self):
#         name = input("请输入要修改的学生姓名")
#         for s in self.stu_list:
#             if s.name == name:
#                 #没想到，输出学生修改前成绩
#                 print(s)
#                 c = int(input("请输入修改后学生语文成绩"))
#                 m = int(input("请输入修改后学生数学成绩"))
#                 e = int(input("请输入修改后学生英语成绩"))
#                 s.update_score(c,m,e)
#                 print(f"修改后学生成绩：{s}")
#                 return
#         print("未找到这名学生")
#     def delete_student(self):
#         name=input("请输入要删除的学生姓名")
#         for s in self.stu_list:
#             if s.name == name:
#                 self.stu_list.remove(s)
#                 print(f"删除后学生列表：{self.stu_list}")
#                 return
#         print("删除失败，未找到该学生")
#     def search_student(self):
#         name = input("请输入要查询的学生姓名")
#         for s in self.stu_list:
#             if s.name == name:
#                 print(s)
#                 return
#         print("查询失败，未找到该学生")
#     def show_all_student(self):
#         for s in self.stu_list:
#             print(s)
# # if __name__ == "__main__":
# #
# #     edu = EduManagement()
# #     # edu.show()
# #     # option = int(input("请输入要进行的操作"))
# #     # match option:
# #     #     case 1:
# #     #         edu.add_student()
# #     #     case 2:
# #     #         edu.update_student()
# #     #     case 3:
# #     #         edu.delete_student()
# #     #     case 4:
# #     #         edu.search_student()
# #     #     case 5:
# #     #         edu.show_all_student()
# #     #     case 6:
# #     #         print("再见。。。")
# #     while True:
# #         edu.show()
# #         option = int(input("请输入要进行的操作"))
# #         match option:
# #             case 1:
# #                 edu.add_student()
# #             case 2:
# #                 edu.update_student()
# #             case 3:
# #                 edu.delete_student()
# #             case 4:
# #                 edu.search_student()
# #             case 5:
# #                 edu.show_all_student()
# #             case 6:
# #                 break
# #     #怎么链接两个文件
# import json
# if __name__ == "__main__":
#     edu = EduManagement()
#     edu.show()
#     edu.add_student()
#     stu_list = []
#     with open("stu_data.json",'w') as f:
#         for s in edu.stu_list:
#             stu_dict = {
#                 "name" : s.name,
#                 "chinese" : s.chinese,
#                 "math" : s.math,
#                 "english" : s.english,
#             }
#             stu_list.append(stu_dict)
#             # json.dump(stu_list, f, ensure_ascii=False,indent=4)
#             # print(json.dumps(stu_list, ensure_ascii=False,indent=4))
#
#
#     # with open("stu_data.json",'r',encoding='utf-8') as f:
#     #     stu_list = json.load(f)
#     #     print(stu_list)