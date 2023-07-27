# student_list = ["Kate","Michael"]
# for i, name in enumerate(student_list, start=1):
#    print(i,name)

drop = [print(*enum_student) for enum_student in enumerate(student_list, start=1)]
