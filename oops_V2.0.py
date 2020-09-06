class student:
    def __init__(self, name, s_id, **marks):
        self.name = name
        self.s_id= s_id
        for i, j in marks.items():
            setattr(self, i, j)
        
    def average(self):
        total = 0
        data = vars(self)
        for i in data.values():
            if type(i) is int:
                total += i
        average = total / (len(data.values()) - 2)
        return total, average
 

student_data = list()

repeat = 'y'
while repeat.lower() == 'y':
    data = {}
    data['name'] = input('Enter student\'s name: ')
    data['s_id'] = input('Enter student ID: ')
    count = int(input(f'Enter number of subjects chosen by student: '))
    for i in range(count):
        subject = input(f'Enter subject name ({i + 1}) : ')
        data[subject] = int(input(f'Enter {subject} marks: '))
    repeat = input('do you want continue (y/n): ')

    temp = student(**data)
    student_data.append(temp)

for i in student_data:
    calc_data = i.average()
    print(f'\nStudent\'s name: {i.name}')
    for j, k in vars(i).items():
        if type(k) is int:
            print(f'{i.name}\'s {j} marks: {k}')
    print(f'{i.name}\'s total marks: {calc_data[0]}')
    print(f'{i.name}\'s average marks: {calc_data[1]}')



 


        
            
        

