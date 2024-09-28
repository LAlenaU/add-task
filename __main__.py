grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
s_students = list(students) #список
s_students.sort()    #отсортирован по алфавиту
print(s_students)
a = sum(grades[0])/(len(grades[0])) #ср балл первый
b = sum(grades[1])/(len(grades[1])) #ср балл второй
c = sum(grades[2])/(len(grades[2])) #ср балл третий
d = sum(grades[3])/(len(grades[3])) #ср балл четвертый
e = sum(grades[4])/(len(grades[4])) #ср балл пятый
list_=[a,b,c,d,e]
print(list_)
add_task = {s_students[0]: list_[0], s_students[1]: list_[1],
            s_students[2]: list_[2], s_students[3]: list_[3],
            s_students[4]: list_[4]}
print(add_task)