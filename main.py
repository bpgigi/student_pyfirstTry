import os

import chapter01.draft

# print(os.getcwd())
# print(__file__)

# from chapter01.draft import EduManagement
# import chapter01.draft
#from chapter01.lesson01 import EduManagement
edu = chapter01.draft.EduManagement()
while True:
    edu.show()
    option = int(input("请输入要进行的操作"))
    match option:
        case 1:
            edu.add_student()
        case 2:
            edu.update_student()
        case 3:
            edu.delete_student()
        case 4:
            edu.search_student()
        case 5:
            edu.show_all_student()
        case 7:
            break
        case 6:
            edu.check_weather()
#怎么链接两个