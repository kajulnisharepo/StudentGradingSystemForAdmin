import statistics

# Global variables as in-memory
Student_DB_Dictionary = {'Alex': [92,76,88],'Sam': [89,92,93], 'Jeff': [90,92,93]}
welcomeStr = "Welcome to Grade Central \n"

adminsCredential = {"admin":"1234","staff":"Pass@123"}

def main():
    print(welcomeStr)
    selectedOption = chooseOptions()
    if selectedOption == '1':
        AddGrade()
    elif selectedOption == '2':
        RemoveStudent()
    elif selectedOption == '3':
        AverageGradeOfStudent()
    elif selectedOption == '4':
        GetAllStudentList()
    elif selectedOption == '5':
        AddNewStudent()
    elif selectedOption == '6':
        exit()
    else:
        print('Please Enter a valid choice was given! try again :( \n')        

def chooseOptions():
    print('[1] - Enter Grades')
    print('[2] - Remove Student')
    print('[3] - Student Average Grades')
    print('[4] - Get all Students list')
    print('[5] - Add New Student')
    print('[6] - Exit')
    print('')
    return input('What would you like to do today? (Enter a number) ')

def Authenticate():
    userNameForlogin = input('UserName: ')
    passwordForlogin = input('Password: ')

    if userNameForlogin in adminsCredential:
        if adminsCredential[userNameForlogin] == passwordForlogin:
            print('G\'day,',userNameForlogin,"!")
            while True:
                main()
        else:
            print('Invalid Password, Try again with correct one')
            Relogin()
    else:
        print('Invalid Credentials, Try again with correct one or Contact Support team')
        Relogin()

def Relogin():
    wantToTryAgain = input('Type \'Y\' to see login screen again! ')
    if wantToTryAgain.capitalize() == 'Y':
        Authenticate()

def AddGrade():    
    StudentName = input('StudentName: ').capitalize()
    Grade = input('Grade : ')   

    if StudentName in Student_DB_Dictionary:
        print('Adding Grade...\n ')
        Student_DB_Dictionary[StudentName].append(float(Grade))
    else:
        print('Student does not exist!')
    print(Student_DB_Dictionary)

def RemoveStudent():    
    StudentNameToRemove = input('What student to remove: ').capitalize()   
    print('removing student...\n ')
    if StudentNameToRemove in Student_DB_Dictionary:
        print('removing student...\n ')
        del Student_DB_Dictionary[StudentNameToRemove]
    else:
        print('Student does not exist!')      
    print(Student_DB_Dictionary)

def AddNewStudent():    
    StudentName = input('StudentName: ').capitalize()
    Grade1 = input('Grade 1: ')
    Grade2 = input('Grade 2: ')
    Grade3 = input('Grade 3: ')

    if StudentName not in Student_DB_Dictionary:
        print('Adding New Student...\n ')
        Student_DB_Dictionary[StudentName]=[(float(Grade1)),(float(Grade2)),(float(Grade3))]
    else:
        print('Student already exist!')
    print(Student_DB_Dictionary)
    
def AverageGradeOfStudent():      
    print('Student Average Grade...\n ')

    # Calculate and print the average scores
    print("Average Scores:\n --------------------\n")
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

Authenticate()
