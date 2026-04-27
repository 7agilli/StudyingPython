students = {
    'Mario': 7,
    'Cleide': 10,
    'Leandro': 8.5
}

def calcule_averate(students):
    average = sum(students.values()) / len(students)
    print(f'The avarage calculated of students is {average}')
    return students

def add_students(students, new_student, new_note):
    if new_student not in students:
       students[new_student] = new_note
       print("Student add sucessfly!")
       return students
    else: 
       print("The student already exist in this list!")
       return students
    
def remove_students(students, name):
    if name in students:
       students.pop(name)
       print(f'The student {name} removed sucessfly!')
       return students
    else:
       print('This student doesnt exist!')
       return students
    
def show_students(students):
   for name, note in students.items():
      print(f'{name}: {note}')

def find_students(students, name): 
   if name in students:
      print(f'{name}: {students[name]}')
   else:
      print('This student doesnot found!')






while True:
    
    choice = input("What's your wish in this moment? (Add student / Remove Student / Student's list / Calcule Average / Find / Exit): ")


    if choice == 'Add student': 
     new_student = input("What is a student name do you want add?: ")
     new_note = input("What's a student's note you want add?: ")
     students = students(students, new_student, new_note)

    elif choice == 'Remove student':
       name = input("What's a student name you want remove?: ")
       students = remove_students(students, name)

    elif choice == "Student's list":
       show_students(students)

    elif choice == "Calcule Average":
       calcule_averate(students)
    
    elif choice == 'Find':
       name = input("What's a student name?: ")
       find_students(students, name)
    elif choice == 'Exit':
       break
    
    else: 
       print('Command Invalid or wrong command. Try again!')
