from Student_Achievement_Management_System.menu import show_menu
from Student_Achievement_Management_System.student_info import *


def main():
    infos = []
    while True:
        show_menu()
        s = input("请选择:")
        if s == 'q':
            return  # 退出
        elif s == '1':
            infos += input_student()
            # infos.extend(input_student())
        elif s == '2':
            output_student(infos)
        elif s == '3':
            delete_student(infos)
        elif s == '4':
            modify_student_score(infos)
        elif s == '5':
            output_student_score_desc(infos)
        elif s == '6':
            output_student_score_asc(infos)
        elif s == '7':
            output_student_age_desc(infos)
        elif s == '8':
            output_student_age_asc(infos)


main()  # 从主函数开始
