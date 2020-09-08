from Student_class import student

student_data = list()

repeat = 'y'
while repeat.lower() == 'y':
    data = {}
    data['name'] = input('\nEnter student\'s name: ')
    data['s_id'] = input('Enter student ID: ')
    count = int(input(f'Enter number of subjects chosen by student: '))
    for i in range(count):
        subject = input(f'Enter subject name ({i + 1}) : ')
        data[subject] = int(input(f'Enter {subject} marks: '))
    repeat = input('do you want continue (y/n): ')
    
    student_data.append(student(**data))

for i in student_data:
    calc_data = i.average()
    print(f'\nStudent\'s name: {i.name}')
    print(f'Student\'s ID: {i.s_id}')
    for j, k in vars(i).items():
        if type(k) is int:
            print(f'{i.name}\'s {j} marks: {k}')
    print(f'{i.name}\'s total marks: {calc_data[0]}')
    print(f'{i.name}\'s average marks: {calc_data[1]}')
