students = ['ali','sara','ahmed','ali'
'zoya','sara','hamza','ali']
print(len(students))

 #sets: a set is collection that stores unique elements . 
# duplicate values are automatically reduced to one occurence

students = {'ALI', 'sara', 'ahmed','ali','zoya','sara','hamza'}
print(students)

students[1]

numbeer_list = [10,20,10,30,40,50]
numbeer_set = {20,10,30,40,10,50,60}
print(numbeer_list)
print(numbeer_set)

a = {}
print(type(a))

b = set()
print(type(b))

a = {1,2,2,3,4,5,5,5}
b = set([4,4,4,5,6])
print(len(a))
print(len(b))

print(2 in a)
print(10 in b)

students = {'ali','sara'}
students.add('zoya')
students.add('ali')
print(len(students))

students.update(['furqan','Raza','Ahmed'])
print(students)

students.remove('sara')
print(students)

students.remove('Taha')
print(students)

students.discard('taha')
print(students)#

removed = students.pop()
print(removed)

courses = {'python','ai','datascirence'}
courses.add('cybersecurity')
courses.add('python')
courses.remove('ai')
print(courses)

registred = {'ali','sara','ahmed','zoya'}
name  = input('entee a student name: ')
if name in registred:
       print('student is registred')
else:
    print('student is not registred')    


for student in students:
    print(students)

python_students = {'ali','sara','ahmed','zoya'}
ai_students = {'sara','zoya','hamza','bilal'}

# union - combine both groups

all_students = ai_students | python_students
print(all_students)
# | (pipe )symbol is used for unioun sets
all_students = python_students.union(ai_students)
print(all_students)

 # intersection : find shared members
both_courses = python_students & ai_students
print(both_courses)
# & ampersand sing is used for finding intersection

both_courses = python_students.intersection(ai_students)
print(both_courses) 

# differnce -  find memebers is one group but not the other
python_only = python_students - ai_students
print(python_only)

# symmetric differce  - find members  who are exactly one  

one_courses_only  = python_students ^ ai_students
print(one_courses_only)

a = {1,2,3,4}
b = {3,4,5,6}
print(a|b) # unioun (every item without duplication)
print(a & b) # intersection (only common items)
print(a - b) # differance (items in a but not in b)
print(a ^ b) # symm diff (only not common items)


python_students = {'ali' , 'sara','zoya'}
ai_students = {'sara', 'zoya','hamza','bilal'}
all_student  = python_students | ai_students
python_only = python_students - ai_students
ai_only = ai_students - python_students
print(all_student)
print(python_only)
print(ai_only)
