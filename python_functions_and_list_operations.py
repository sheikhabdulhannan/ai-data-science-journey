
def analyze_marks(mark):
    total = 0
    highest  = mark[0]
    lowest = mark[0]
    for marks in mark:
        total += marks
        if marks > highest:
            highest = marks
        if marks < lowest:
            lowest = marks
    return total , highest , lowest
mark = [45,64,65,55]
total ,highest,lowest =  analyze_marks(mark)
print('total',total)
print('highest',highest)
print('lowest',lowest)




# varible packing and variable unpacking
coordinates = -40.7128, -74.0060 # packing values in a tuple
print(coordinates)

# unpacking
lat , lon =  coordinates
print(lat)
print(lon)


x = 5
y = 10
x,y = y,x # variable swapping
print(x,y)

first,second,*remaining = [10,20,30,40,50]
print(first)
print(second)
print(remaining)

 # python is in counting
first,*middle,last = [10,20,30,40,50]
print(first,middle,last)

a,b,c,*d = [10,20,30,40,50]
print(c)

name,age,*_ =  ['hannan',25,'dodctor','berlin']
print(name)

def add_there(a,b,c):
    return a+b+c
numbers = [5,10,15]
print(add_there(*numbers))

# create a fn anayl_number
# return total , number of even numbers , odd numbers
# numbers = [10,13,43,54,54]
def analyze_number(number):
    total = 0
    even = 0
    odd = 0  
    for numbers in number:
        total += numbers
        if numbers%2 == 0:
            even += 1
        else:
            odd += 1
    return total ,even , odd
number =[10,15,22,54,66,4]
total,even,odd = analyze_number(number)
print(total,even,odd)

 

def get_high_marks(makrks):
    highh_marks = []
    for mark in makrks:
        if mark >= 80:
            highh_marks.append(mark)
    return highh_marks      
marks = [43,34,34,4,3]
result = get_high_marks(marks)
print(result)


# write a function double_number
# fn takes a list as input
# fn number the list in return with every number double
# number = [2,4,6,8]
# output = [4,8,12,16]

def double_marks(numbers):
    double = []
    for number in numbers:
        double.append(number*2)
    return double
number = [2,3,4,5,6,6]
result = double_marks(number)
print(result) 

# wirte a function double_number
# fn takes a list as input
# fn number the list in return with every number doubled
#number = [2,4,6,8]
# output double_number
# docstring
def calculate_area(length , widh):

    ''' calculte and return the area of rectanangle '''
    return length * widh
print(calculate_area(10,5))

#print(calculate_area.__doc__) # to view the docstring