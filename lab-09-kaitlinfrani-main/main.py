# -*- coding: utf-8 -*-
"""
Kaitlin Frani
CPSC 223P-01
Wed Apr 14, 2021
kaitlinfrani@fullerton.edu
"""
import sys

#setting up list dictionaries for attendance and grades
attendanceList = [{'Student' : 'Paul McCartney', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'John Lennon', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'George Harrison', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'Ringo Starr', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'Robert Plant', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'Jimmy Page', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'John Bonham', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'John Paul Jones', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'Trey Anastasio', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'Jon Fishman', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'Mike Gordon', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""},
                  {'Student' : 'Page McConnell', 'January 25' : "", 'February 1' : "",
                   'February 8' : "", 'February 15' : "", 'February 22' : "", 'March 1' : "",
                   'March 8' : "", 'March 15' : "", 'March 22' : "", 'March 29' : "",
                   'April 5' : "", 'April 12' : "", 'April 19' : "", 'April 26' : "", 
                   'May 3' : "", 'May 10' : ""}]

gradeList = [{'Student' : "Paul McCartney", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "John Lennon", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "George Harrison", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "Ringo Starr", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "Robert Plant", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "Jimmy Page", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "John Bonham", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "John Paul Jones", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "Trey Anastasio", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "Jon Fishman", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "Mike Gordon", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""},
             {'Student' : "Page McConnell", 'Assignment 1' : "", 'Assignment 2' : "", 'Assignment 3' : "",
              'Assignment 4' : "", 'Midterm' : "", 'Final' : ""}]

#Output choices, let user type in input
while True:
    menu_choice = input("What do you want to do?\n1 - List all students\n2 - List all grades\
                 \n3 - List attendance\n4 - Submit a grade\n5 - Take attendance\nQ - Quit\n\n> ").upper()
    
    def choice1():
        attendanceFile = open("attendance.txt", "r")
        next(attendanceFile)
        students = attendanceFile.read().replace(",","")
        print(students)
        attendanceFile.close()
    
    def choice2():
        #with open("grades.txt", "r") as gradeFile:
        for i in gradeList:
            print(i['Student'])
            print('Assignment 1:', i['Assignment 1'])
            print('Assignment 2:', i['Assignment 2'])
            print('Assignment 3:', i['Assignment 3'])
            print('Assignment 4:', i['Assignment 4'])
            print('Midterm:', i['Midterm'])
            print('Final:', i['Final'], "\n")
    
    def choice3():
        with open("attendance.txt", "r") as attendanceFile:
            attendance_list = []
            for line in attendanceFile:
                stripped_line = line.strip()
                line_list = stripped_line.split(",")
                attendance_list.append(line_list)
            print("Which student?")
            for index, line in enumerate(attendance_list[1:]):
                index += 1
                print(index,"-", ''.join(line))
            #user chooses which student
            student = input()
            
            #repeat this for each choice 1-12
            if student == "1":
                for i in attendanceList:
                    if i['Student'] == 'Paul McCartney':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "2":
                for i in attendanceList:
                    if i['Student'] == 'John Lennon':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "3":
                for i in attendanceList:
                    if i['Student'] == 'George Harrison':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "4":
                for i in attendanceList:
                    if i['Student'] == 'Ringo Starr':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "5":
                for i in attendanceList:
                    if i['Student'] == 'Robert Plant':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "6":
                for i in attendanceList:
                    if i['Student'] == 'Jimmy Page':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "7":
                for i in attendanceList:
                    if i['Student'] == 'John Bonham':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "8":
                for i in attendanceList:
                    if i['Student'] == 'John Paul Jones':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "9":
                for i in attendanceList:
                    if i['Student'] == 'Trey Anastasio':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "10":
                for i in attendanceList:
                    if i['Student'] == 'Jon Fishman':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "11":
                for i in attendanceList:
                    if i['Student'] == 'Mike Gordon':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
            if student == "12":
                for i in attendanceList:
                    if i['Student'] == 'Page McConnell':
                        print(i['Student'])
                        #going to return the dictionary's key-value pairs by using items function
                        for key, value in i.items():
                            if key == 'Student':
                                pass
                            else:
                                print(key + ':', value)
                                
    def choice4():
        """
        choose from list of assignments then show the grade of that assignment 
        for each student
    
        Returns
        -------
        choice options of what assignment they want to look at
    
        """
        #look into with open
        with open("grades.txt", "r") as gradeFile:
            gradeFile.seek(9)
            #turn file to list to access and iterate through
            grade_list = []
            for line in gradeFile:
                stripped_line = line.strip()
                line_list = stripped_line.split(", ")
                grade_list.append(line_list)
            print("Which assignment?")
            #need to iterate through how many assignments there are and add options
            #1 - Assignment 1....
            #2 - Assignment 2....
            for index, line in enumerate(grade_list[0]):
                index += 1
                print(index, "-", line)
            menu_choice = input("> ")
            #with open("grades.txt", "r") as gradeFile:
            if menu_choice == "1":
                #assignment_list = []
                #for line in gradeFile:
                 #   stripped_line = line.strip()
                  #  line_list = stripped_line.split(",")
                   # assignment_list.append(line_list)
                for i in gradeList:
                    for key, value in i.items():
                        if key == 'Student':
                            student = i[key]
                        if key == 'Assignment 1':
                            grade = input(("Grade for " + student + " for Assignment 1 > "))
                            i[key] = grade
            if menu_choice == "2":
                #assignment_list = []
                #for line in gradeFile:
                 #   stripped_line = line.strip()
                  #  line_list = stripped_line.split(",")
                   # assignment_list.append(line_list)
                for i in gradeList:
                    for key, value in i.items():
                        if key == 'Student':
                            student = i[key]
                        if key == 'Assignment 2':
                            grade = input(("Grade for " + student + " for Assignment 1 > "))
                            i[key] = grade
            if menu_choice == "3":
               # assignment_list = []
                #for line in gradeFile:
                 #   stripped_line = line.strip()
                  #  line_list = stripped_line.split(",")
                   # assignment_list.append(line_list)
                for i in gradeList:
                    for key, value in i.items():
                        if key == 'Student':
                            student = i[key]
                        if key == 'Assignment 3':
                            grade = input(("Grade for " + student + " for Assignment 1 > "))
                            i[key] = grade
            if menu_choice == "4":
                #assignment_list = []
                #for line in gradeFile:
                 #   stripped_line = line.strip()
                  #  line_list = stripped_line.split(",")
                   # assignment_list.append(line_list)
                for i in gradeList:
                    for key, value in i.items():
                        if key == 'Student':
                            student = i[key]
                        if key == 'Assignment 4':
                            grade = input(("Grade for " + student + " for Assignment 1 > "))
                            i[key] = grade
            if menu_choice == "5":
                #assignment_list = []
                #for line in gradeFile:
                 #   stripped_line = line.strip()
                  #  line_list = stripped_line.split(",")
                   # assignment_list.append(line_list)
                for i in gradeList:
                    for key, value in i.items():
                        if key == 'Student':
                            student = i[key]
                        if key == 'Midterm':
                            grade = input(("Grade for " + student + " for Assignment 1 > "))
                            i[key] = grade
            if menu_choice == "6":
                #assignment_list = []
                #for line in gradeFile:
                 #   stripped_line = line.strip()
                  #  line_list = stripped_line.split(",")
                   # assignment_list.append(line_list)
                for i in gradeList:
                    for key, value in i.items():
                        if key == 'Student':
                            student = i[key]
                        if key == 'Final':
                            grade = input(("Grade for " + student + " for Assignment 1 > "))
                            i[key] = grade
        overwrite_file = "Student, Assignment 1, Assignment 2, Assignment 3, Assignment 4, Midterm, Final"
        for i in gradeList:
            overwrite_file = overwrite_file + "\n"
            for key, value in i.items():
                overwrite_file = overwrite_file + value + ","
        with open("grades.txt", "w") as gradeFile:
            gradeFile.write(overwrite_file)
                            
    def choice5():
        #use seek to go to 9th character
        with open("attendance.txt", "r") as attendanceFile:
            attendanceFile.seek(9)
            attendance_list = []
            print("Which date?")
            for line in attendanceFile:
                stripped_line = line.strip()
                line_list = stripped_line.split(", ")
                attendance_list.append(line_list)
            for index, line in enumerate(attendance_list[0]):
                index += 1
                print(index,"-", line)
            menu_choice = input("> ")
            if menu_choice == "1":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "January 25":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "1":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "January 25":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "2":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "February 1":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "3":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "February 8":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "4":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "February 15":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "5":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "February 22":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "6":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "March 1":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "7":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "March 8":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "8":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "March 15":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "9":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "March 22":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "10":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "March 29":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "11":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "April 5":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "12":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "April 12":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "13":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "April 19":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "14":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "April 26":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "15":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "May 3":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
            if menu_choice == "16":
                for i in attendanceList:
                    for key, value in i.items():
                        if key == "Student":
                            student = i[key]
                        if key == "May 10":
                            attendance = input("Student " + student + " (p/a) > ")
                            if attendance == "p":
                                i[key] = "Present"
                            if attendance == "a":
                                i[key] = "Absent"
        overwrite_file = "Student, January 25, February 1, February 8, February 15, February 22, March 1,"\
                          "March 8, March 15, March 22, March 29, April 5, April 12, April 19, April 26, May 3, May 10"
        for i in attendanceList:
            overwrite_file = overwrite_file + "\n"
            for key, value in i.items():
                overwrite_file = overwrite_file + value + ","
        with open("attendance.txt", "w") as attendanceFile:
            attendanceFile.write(overwrite_file)
            
        
    #choice 1: output all the names of the students
    if menu_choice == "1":
        choice1()
    
    #choice 2: output the grades for each assignment/test for each student
    elif menu_choice == "2":
        choice2()
    
    #choice 3: choose from list of students, then show attendance for each date
    elif menu_choice == "3":
        choice3()
    
    #choice 4: choose from list of assignments then show the grade of that 
    #assignment for each student
    #for grades use percentages like 87.5, they can be strings
    
    elif menu_choice == "4":
        choice4()
    
    #choice 5: choose from list of class dates, then show attendance for each student
    elif menu_choice == "5":
        choice5()
    
    #choice Q: exit program
    elif menu_choice == "Q":
        sys.exit()
        
    else:
        print("Wrong choice. Try again.")
    
    
