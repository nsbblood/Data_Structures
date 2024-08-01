student_pet_count_list=[0,1,0,2,3,1,0,0,2,0,2,1,0,2,0,3,4,1,2,1,0,0,2,0,0]

student_pet_count_list[2]=3
student_pet_count_list[3]=student_pet_count_list[3]+1
student_pet_count_list[-1]=student_pet_count_list[-1]+2

student_pet_count_list.append(4)

ITEM_AT_INDEX_THREE=student_pet_count_list[3]
#print(student_pet_count_list[100])
ITEM_THREE_FROM_BACK=student_pet_count_list[-3]


NUM_OF_STUDENTS=len(student_pet_count_list)
print(NUM_OF_STUDENTS)

SUM=0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
    SUM=SUM + INDIVIDUAL_PET_COUNT

print(SUM)

AVERAGE= SUM/NUM_OF_STUDENTS
print(AVERAGE)