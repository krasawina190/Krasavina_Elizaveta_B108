class Student():
    students = []
    def __init__(self, surname, name, patronymic, grade, parent_mom, parent_dad):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.grade = grade
        self.parents_mom = parent_mom
        self.parents_dad = parent_dad
        Student.students.append(self)

class Grades():
    names= []
    def __init__(self, name_of_class, teacher_of_math, teacher_of_history):
        self.name_of_class = name_of_class
        self.teacher_of_math = teacher_of_math
        self.teacher_of_history = teacher_of_history
        Grades.names.append(self)



fifth = Grades('5А', 'Анна Петровна', 'Анжела Анатольевна')
sixth = Grades('6Б', 'Елена Викторовна', 'Ангелина Максимовна')
seventh = Grades('7В', 'Анна Петровна', 'Анастасия Игоревна')

ivanov = Student('Иванов', 'Иван', 'Иванович', '5А', 'Лидия Петровна', 'Иван Иванович')
Petrov = Student('Петров', 'Петр', 'Сергеевич', '5А', 'Елена Васильевна', 'Сергей Сергеевич')
Sidorov = Student('Сидоров', 'Максим', 'Андреевич', '6Б', 'Анастасия Петровна', 'Андрей Викторович')
Vryasova = Student('Врясова', 'Елизавета', 'Андреевна', '6Б', 'Екатерина Ивановна', 'Андрей Ильич')
Raskina = Student('Раскина', 'Екатерина', 'Николаевна', '7В', 'Диана Рустемовна', 'Николай Николаевич')
Agapov = Student('Агапов', 'Максим', 'Валерьевич', '7В', 'Алина Владимировна', 'Валерий Петрович')

for i in Grades.names:   #Получить полный список всех классов школы
    print(i.name_of_class)

input_class = input("Введите класс: ")
for i in Student.students:
    if input_class == i.grade:
        print(i.surname, " ", i.name[0], '.', i.patronymic[0], '.', sep="")  #Получить список всех учеников в указанном классе


input_student = input("Введите фамилию ученика: ")  #Узнать ФИО родителей указанного ученика
for i in Student.students:
    if input_student == i.surname:
        print("мама: ", i.surname[0], i.parents_mom[0], i.parents_mom.split(' ')[1][0], ' папа: ', i.surname[0], i.parents_dad[0], i.parents_dad.split(' ')[1][0], sep = "")


input_class_2 = input("Введите класс: ")  #Получить список всех Учителей, преподающих в указанном классе
for i in Grades.names:
    if input_class_2 == i.name_of_class:
        print("Список всех Учителей, преподающих в указанном классе: ", i.teacher_of_math, ", ", i.teacher_of_history, sep= "")
