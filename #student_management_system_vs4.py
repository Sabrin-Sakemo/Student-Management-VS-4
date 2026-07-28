#student_management_system_vs4
#Author:Sabrin Nahar
#Date:27.07.2026
import json
try:
    with open('student.json','r')as f_name:
         students=json.load(f_name)
except FileNotFoundError:
     students=[]
while True:
    print("Welcome to Student Management System. How can we help you?")
    print(" 1.Add New Student", "\n" ,
          "2.Show All Student","\n",
          "3.Search Student","\n",
          "4.Delete Student","\n",
          "5.Update Student","\n",
          "6.Exit")
    try:
        choice=int(input("Choice:"))
        if choice==1:
                add_stu=input("Student Name:")
                i_d=input("Student ID:")
                sec=input("Section:")
                student={'name':add_stu,
                          'id':i_d,
                          'section':sec}
                students.append(student)
                with open('student.json','w') as f_name:
                      json.dump(students,f_name,indent=4)
                      print("Sucessfully Added")
        if choice==2: 
            with open('student.json','r')as f_name:
                 students=json.load(f_name)
                 students.sort(key=lambda student:student["name"])
                 for student in students:   
                      print("Student Name",":",student['name'])
                      print ("Id",":",student['id'])
                      print('Section',':',student['section'])
                      print("_"*30)
                      print()
        if choice==3:
            found=False
            ser=input("Student Name:").lower()
            with open('student.json') as f_name:
                  students=json.load(f_name)
                  for student in students:
                    if student['name'].lower().startswith(ser):
                        found=True
                        print("Student Name",":",student['name'])
                        print ("Id",":",student['id'])
                        print('Section',':',student['section'])
            
            if not found:
                 print("Student Not Found")
        if choice==4:
             found=False
             i_d=input("Enter ID:")
             with open('student.json') as f_name:
                  students=json.load(f_name)
                  for student in students: 
                    if student["id"]==i_d:
                            found=True
                            students.remove(student)
                            with open("student.json","w")as f_name:
                             json.dump(students,f_name,indent=4)
                             print("Student Remove")
                             break
                  if not found:
                    print("Please Enter Valid ID")
        if choice==5:
             found=False
             i_d=input("Enter ID:")
             with open("student.json") as f_name:
                  students=json.load(f_name)
                  for student in students:
                   if student["id"]==i_d:
                    found=True
                    student["name"]=input("Student New Name:")
                    student["id"]=input("Student New ID:")
                    student["section"]=input("New Section:")
                    with open('student.json','w')as f_name:
                        json.dump(students,f_name,indent=4)
                        print("Update Successfully")
             if not found:
                      print('Enter Valid ID')

        if choice==6:
            print('Thank You for Using')
            break
                            
    except ValueError: 
        print("Please Enter the Right One")