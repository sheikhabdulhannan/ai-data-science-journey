import json
def calculate_grade(marks):
     if marks>=90:
          return"A+"
     elif marks>=80:
          return"A"
     elif marks>=70:
          return"B"
     elif marks>=60:
          return"C"
     elif marks>=50:
          return"D"
     elif marks>=40:
          return"E"
     else:
          return"Fail"
def generate_student_id():
     next_id=len(student)+1
     return f"STU{next_id:03d}"
     
def load_data():  
     try:   
      with open ("data/students.json","r") as file:
          return json.load(file)
     except FileNotFoundError:
          return {}
student = load_data()

def save_data():
     with open ("data/students.json","w") as file:
          json.dump(student,file,indent=4)     
          

def show_menu():
    print("\n====STUDENT MANAGER====")
    print("1.add student")
    print("2.view student")
    print("3.check result")
    print("4.update marks")
    print("5.average marks")
    print("6.exit")
    print("7.topper")
    print("8.lowest")
    print("9.statics")
    print("10.search student")
    print("11.delete student")
    print("12.sort students by marks")
    print("13.search by roll number")
    print("14.update by roll number")

while True:
    show_menu()
    choice=input("enter your choice:")

    #add student

    if choice=="1":
         name = input("enter student name: ")
         if name in student:
              print("already exists")
         else:
            roll_number=input("enter roll number:") 
            duplicate=False
            for data in student.values():
                 if data["roll_number"]==roll_number:
                      duplicate=True
                      break
         if duplicate:
          print("roll number already exists!")
         else:             
            marks=int(input("enter marks:"))
            if marks < 0 or marks > 100:
                 print("enter marks between 0 to 100")
              
            else:
                 student_id=generate_student_id()
                 student[name] = {
                    "student_id": student_id,
                    "roll_number": roll_number,
                    "marks": marks,
                    
                 }
                 save_data()
                 print(f"{name}:sucessfully added!")
                 print("Student_Id:",student_id)

    # view student
    elif choice=="2":
         if not student:
               print("no student found!")
         else:
              for name,data in student.items():
                   print("name:",name)
                   print("roll_number:",data["roll_number"])
                   print("marks:",data["marks"])
                   print("student_id:",data["student_id"])
                    


     # check result  
    elif choice=="3":
         name = input("enter student name:")

         if name in student:
              data = student[name]
              marks = data["marks"]

              grade = calculate_grade(marks)


                   
              print("name:",name)
              print("student_id:",data["student_id"])
              print("roll_number:",data["roll_number"])
              print("marks:",marks)
              print("grade:",grade)   
                
         else:
               print("student not found")

     # update marks
    elif choice=="4":
         name=input("enter student name:")
         if name in student:
              new_marks=int(input("enter new_marks:"))
              if new_marks <0 or new_marks >100:
                   print("enter marks between 0 to 100")
              else: 
                  student[name]["marks"]=new_marks
                  save_data()
                  print("update marks succesfully")
         else:
               print("student not found!")

     # average marks
    elif choice=="5":
         if not student:
               print("no student found!")

         else:
              total_marks=0
              for data in student.values():
                   total_marks += data["marks"]


              total_student=len(student)
              average = total_marks / total_student

              print("average marks:",average)

     # tooper
    elif choice=="7":
         if not student:
               print("no student found!")
         else:
              topper=max(student,key=lambda name:student[name]["marks"])
              data=student[topper]

              print("topper:",topper)
              print("roll_number:",data["roll_number"])
              print("marks:",data["marks"])   
              print("student_id:",data["student_id"]) 

     # lowest
    elif choice=="8":
         if not student:
               print("no student found!")
         else:
              lowest=min(student,key=lambda name:student[name]["marks"])
              data=student[lowest]      

              print("lowest:",lowest) 
              print("roll_number:",data["roll_number"])
              print("marks:",data["marks"]) 
              print("student_id:",data["student_id"])   
              
    # statics
    elif choice=="9":
         if not student:
               print("no student found!")

         else:
              total_student=len(student)     
              pass_count=0
              fail_count=0

              for data in student.values():
                   marks = data["marks"]
                   if marks>=40:
                        pass_count+=1
                   else:
                        fail_count+=1
              total_marks=0
              for data in student.values():
                   total_marks += data["marks"]
              average= total_marks / total_student      


         print("Total Students :", total_student)
         print("Pass Students :", pass_count)
         print("Fail Students :", fail_count)
         print("Average Marks :", average)


    # search student
    elif choice=="10":
         if not student:
               print("no student found")
         else:
              name = input("enter student name:")
              if name in student:
                 data = student[name]
                 marks = data["marks"]    
                 grade = calculate_grade(marks)
                    
                 print("name:",name)
                 print("roll_number:",data["roll_number"])
                 print("student_id:",data["student_id"])
                 print("marks:",marks)
                 print("grade:",grade)
              
    #  delete student
    elif choice=="11":
         if not student:
              print("no student found")
         else:
              name = input("enter student name:")
              if name in student :
                   del student[name]
                   save_data()
                   print("student deleted succesfully")
              else:
                   print("student not found")     

    # sort student
    elif choice=="12":
         if not student:
              print("no student found")
         else:
              sorted_students=sorted(student.items(), key=lambda item: item[1]["marks"], reverse=True)    
              for name, data in sorted_students:
                   print("name:",name)
                   print("roll_number:",data["roll_number"])
                   print("student_id:",data["student_id"])
                   print("marks:",data["marks"])
                   print("-"*30)
     # search by roll number
    elif choice=="13":
         if not student:
              print("no student found")
         else:
              roll_number=input("enter roll number:")
              found=False

              for name, data in student.items():
                   if data["roll_number"]==roll_number:
                        marks=data["marks"]
                        grade=calculate_grade(marks)

                        print("name:",name)
                        print("student id:",data["student_id"])
                        print("roll number:",data["roll_number"])
                        print("marks:",marks)
                        print("grade:",grade)

                        found=True
                        break
                   if not found:
                        print("roll number not found")

     # update by roll number
    elif choice=="14":
         roll_number=input("enter roll number:")
         found=False

         for name,data in student.items():
              if data["roll_number"] == roll_number:
                 print("Current name:",name)
                 print("Current marks:",data["marks"])

                 new_name=input("enter new name:")
                 new_marks=int(input("enter new marks:"))

                 if new_marks < 0 or new_marks > 100:
                      print("enter marks between 0 to 100")
                 else:

                      student[new_name] = student.pop(name)
                      student[new_name]["marks"] = new_marks

                      save_data()
                      print("student update succesfully!")

                      found=True
                      break
         if not found:
          print("roll number not found")


