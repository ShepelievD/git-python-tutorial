students_dictionary = {}

def add_to_student_dictionary(id, first_name, last_name, age):
    students_dictionary[id] = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age
    }

print(students_dictionary)

add_to_student_dictionary(1, 'Dmytro', 'Shepeliev', 25)

print(students_dictionary)
