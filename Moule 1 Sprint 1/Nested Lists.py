

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
 
sorted_students = sorted(students, key=lambda x:x[1], reverse=True)
 
print(sorted_students[-2][0])
if sorted_students[-3][1] == sorted_students[-2][1]:
    print(sorted_students[-3][0])
else:
    print()


