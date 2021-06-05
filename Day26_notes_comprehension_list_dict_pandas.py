
# List comprehension
# new_list = [new_item for item in list]

# numbers = [1, 2, 3]
# new_list = [num + 1 for num in numbers]
# print(new_list)
#
# name = "Liwei"
# new_list = [alpha for alpha in name]
# print(new_list)
#
# range(1, 5)
# new_list = [num * 2 for num in range(1, 5)]
# print(new_list)
#
# names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) == 4]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)
#
# # Dictionary comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)
#
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [58, 76, 98]
# }
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# # for (key, value) in student_data_frame.items():
# #     print(key)
# #     print(value)
#
# for (index, row) in student_data_frame.iterrows():
#     # print(index)
#     # print(row)
#     # print(row.student)
#     # print(row.score)
#     # if row.student == "Angela":
#     #     print(row.score)
