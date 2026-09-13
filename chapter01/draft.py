import json
import requests
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
    def to_dict(self):
        return {
            "name": self.name,
            "chinese": self.chinese,
            "math": self.math,
            "english": self.english
        }
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
        print("6.查询天气")
        print("7.退出系统")
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
                self.save_data()
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
    def check_weather(self):
        import json

        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        city_name = input("请输入要查询的城市名字")
        params = {
            "name": city_name,
            "count": 1,
            "language": "zh"
        }
        try:
            geo_response = requests.get( geo_url, params=params,timeout=5)
            geo_response.raise_for_status()
        except requests.exceptions.ReadTimeout as e:
            print("超时",e)
            return
        except requests.exceptions.HTTPError:
            print("服务器返回错误")
            return
        except requests.exceptions.RequestException:
            print("网络请求失败")
            return
        try:
            geo_data = geo_response.json()
        except json.decoder.JSONDecodeError as e:
            print("服务器返回的数据不是合法 JSON",e)
            return
        #print(geo_data)
        if "results" not in geo_data:
            print("城市不存在")
            return

        city = geo_data["results"][0]  # --->全部信息，不只是city这个
        #print(json.dumps(city, ensure_ascii=False, indent=4))
        # print(f"城市：{city['name']}")
        # print(city["id"])
        # print(city["latitude"])
        # print(city["longitude"])
        latitude = city["latitude"]
        longitude = city["longitude"]
        print("维度：", latitude)
        print("经度", longitude)

        #第二次api，查天气
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m"
        }
        weather_response = requests.get( weather_url, params=weather_params)
        weather_data = weather_response.json()
        # print(weather_data)
        # print(type(weather_data))
        # print(json.dumps(weather_data, ensure_ascii=False, indent=4))
        temperature = weather_data["current"]["temperature_2m"]
        # print(weather_data["temperature_2m"])
        print(f"{city_name}当前温度：{temperature}°C")
    def upload_student(self,student):
        url = "https://jsonplaceholder.typicode.com/posts"
        try:
            response = requests.post(url, json=student,timeout=5)
            response.raise_for_status()
            print(requests.status_codes)
            data = response.json()
            print("添加成功")
        except requests.exceptions.ReadTimeout as e:
            print("超时",e)
            return
        except requests.exceptions.RequestException as e:
            print("网络错误",e)
            return


 if __name__ == "__main__":
    edu =EduManagement()
    stu = Student("dxy",23,34,56)
    edu.upload_student(stu)
