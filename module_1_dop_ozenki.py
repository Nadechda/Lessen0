grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_sort=sorted(students)

grades_=[]
for i in grades:
    s=sum(i)/len(i)
    grades_.append(s)

print(dict(zip(student_sort,grades_)))