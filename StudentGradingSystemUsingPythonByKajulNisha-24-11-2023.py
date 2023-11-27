# Project Name: Student Grading System
# Description
'''
Description

Create a student grading system using Python that has the following functionalities:
1. Entering the Grades of a student
2. Removing a student from the system
3. Calculating the average grades of students
The user should be able to select whether he/she wants to remove a student, enter grades for a
student or find the average grades.
Also, perform the following as part of this project:

There should be a log-in system to allow only admin access to the grading system.
Make sure you use dictionaries and lists for storing student’s data.
Use Python functions as much as you can

Hint: Statistics module might be helpful
'''
import statistics
Student_DB_Dictionary = {'Alex': [92,76,88],'Sam': [89,92,93]}

def chooseOptions():
    print('[1] - Enter Grades')
    print('[2] - Remove Student')
    print('[3] - Student Average Grades')
    print('[4] - Get all Students list')
    print('[5] - Exit')
    print('')
    return input('What would you like to do today? (Enter a number) ')

def Operations():
    '''
    print('==============================\n')
    print('Welcome to Grade Central \n')
    print('==============================\n')
    '''
    return chooseOptions()

def AddStudent():    
    StudentName = input('StudentName: ').capitalize()
    Grade = input('Grade (comma seperated): ')   

    print('Adding Grade...\n ')

    Student_DB_Dictionary[StudentName]=[Grade]
   
    
    print('StudentName: ',StudentName)
    print('Grade: ',Grade)
    print(Student_DB_Dictionary)    
    

def RemoveStudent():    
    StudentNameToRemove = input('What student to remove: ').capitalize()   
    print('removing student...\n ')
    del Student_DB_Dictionary[StudentNameToRemove]    
    print(Student_DB_Dictionary)
    

def AverageGradeOfStudent():      
    print('Student Average Grade...\n ')

    # Calculate and print the average scores
    print("Average Scores:")
    for student, scores in Student_DB_Dictionary.items():
        average_score = statistics.mean(scores)
        print(f"{student}: {average_score:.2f}")
        
def GetAllStudentList():      
    print('Fetching all students record...\n')
    print('Total No. Of. Students =',len(Student_DB_Dictionary))    
    print('``````````````````````````````')

    # Print the header    
    print("Name\t\tGrades")

    # Iterate over the dictionary and print each student's scores
    for student, scores in Student_DB_Dictionary.items():
        print(f"{student}:\t\t{scores[0]}\t{scores[1]}\t{scores[2]}")
    

def ConfirmationForFurtherProcess():
    wantToContinue = input('------------ \n Want to continue... (Choose y-yes/n-no) ').capitalize()
    if wantToContinue == 'Y':
        mainFunction('N')        
    if wantToContinue == 'N':
        print('\n ---------------- \n Thanks for visiting!')

    
def mainFunction(isFirstTime='Y'):
    if isFirstTime=='Y':
        print('==============================\n')
        print('Welcome to Grade Central \n')
        print('==============================\n')
    else:
        print('______________________\n')
        
    userSelectedChoice = Operations()
    print(userSelectedChoice)
    if userSelectedChoice=='1':
        AddStudent()
    elif userSelectedChoice=='2':
        RemoveStudent()
    elif userSelectedChoice=='3':
        AverageGradeOfStudent()
    elif userSelectedChoice=='4':
        GetAllStudentList()
    else:
        Operations()
    ConfirmationForFurtherProcess()
    
mainFunction()

