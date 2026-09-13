import json

class Student:
    def __init__(self, name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    #没想到
    def __str__(self):
        #print(f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}")
        return f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}"
    #更没想到
    def __repr__(self):
        return self.__str__()
    #def update_score(self,name,c=None,m=None,e=None):   修改不用确定name
    def update_score(self,c=None,m=None,e=None):
        if c is not None:
            self.chinese=c
        if m is not None:
            self.math=m
        if e is not None:
            self.english=e
class EduManagement:
    def __init__(self):
        self.stu_list = [] #学生列表，里面存学生类
        self.load_data()  #启动edu就读data
    #将json的数据转为stu_list的对象数据？
    def load_data(self):
        try:  #没想到，如果没数据要报错，因为这个函数是在init初始化
            with open("stu_data.json","r",encoding="utf-8") as f:
                data = json.load(f)
                for stu_dict in data: #data是列表里是字典
                    #stu_dict.name = stu_dict.name
                    #将字典的各项数据转为对象
                    student = Student(
                        stu_dict["name"],
                        stu_dict["chinese"],
                        stu_dict["math"],
                        stu_dict["english"]
                    )
                    #将对象添加到总列表。因为业务逻辑是列表来做的，改动小
                    self.stu_list.append(student)
        except FileNotFoundError:
            print("未找到数据")
    def save_data(self):
        data = [] #stu_list里是对象，存json要的是字典
        for stu in self.stu_list:
            stu_dict = {
                "name": stu.name,
                "chinese": stu.chinese,
                "math": stu.math,
                "english": stu.english
            }
            data.append(stu_dict)
        with open("stu_data.json","w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
    def show(self):
        print("-"*20)
        print("1.添加学生成绩")
        print("2.修改学生成绩")
        print("3.删除学生成绩")
        print("4.查询学生成绩")
        print("5.展示全部学生成绩")
        print("6.退出系统")
        print("-" * 20)
    def add_student(self):
        n = input("请输入要添加的学生姓名")
        for s in self.stu_list:
            if s.name == n:
                print("学生存在，添加失败")
                return
        c = int(input("请输入学生语文成绩"))
        m = int(input("请输入学生数学成绩"))
        e = int(input("请输入学生英语成绩"))
        if 1 <= c <= 100 and 1 <= m <= 100 and 1 <= e <= 100:
            self.stu_list.append(Student(n, c, m, e))
            self.save_data()
        else:
            print("添加失败，成绩必须在1-100")
    def update_student(self):
        n = input("请输入要修改的学生姓名")
        for s in self.stu_list:
            if s.name == n:
                c = int(input("请输入修改后的语文成绩"))
                m = int(input("请输入修改后的数学成绩"))
                e = int(input("请输入修改后的英语成绩"))
                if 1 <= c <= 100 and 1 <= m <= 100 and 1 <= e <= 100:
                    s.chinese = c
                    s.math = m
                    s.english = e
                    self.save_data()
                    return
                else:
                    print("添加失败，成绩必须在1-100")
                    return
        print("该学生不存在！")
    def delete_student(self):
        name = input("请输入要删除的学生姓名")
        for s in self.stu_list:
            if s.name == name:
                self.stu_list.remove(s)
                #print(f"删除后学生列表：{self.stu_list}")
                with open("stu_data.json","w",encoding="utf-8") as f:
                    json.dump(self.stu_list,f,ensure_ascii=False,indent=4)
                return
        print("删除失败，未找到该学生")
    def search_student(self):
        name = input("请输入要查询的学生姓名")
        for s in self.stu_list:
            if s.name == name:
                print(s)
                return
        print("查询失败，未找到该学生")
    def show_all_student(self):
        for s in self.stu_list:
            print(s)

# if __name__ == "__main__":
    # edu =EduManagement()
    # edu.show()
    # edu.add_student()
    # edu.update()
    # print(os.getcwd())