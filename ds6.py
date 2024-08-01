
dataList=[0,3,5,11,14,16,22,25,28,30,4,12,23]
print(sorted(dataList,reverse=True))

student_grades=[('Sarah',88),('Jack',80),('Nora',95)]
print(sorted(student_grades))
print(sorted(student_grades, key=lambda x:x[1],reverse=True))