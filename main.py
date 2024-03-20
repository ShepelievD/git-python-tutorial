students_dictionary = {}

def add_to_student_dictionary(id, first_name, last_name, age):
    students_dictionary[id] = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age
    }

print(students_dictionary)

id = input('Введіть айді: ')
first_name = input('Введіть імʼя: ')
last_name = input('Введіть прізвище: ')
age = input('Введіть вік: ')

add_to_student_dictionary(id, first_name, last_name, age)

print(students_dictionary)
