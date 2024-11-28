students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
str_students = ', '.join(students)
str_subjects = ', '.join(subjects)
text = f'Students {str_students} study these subjects: {str_subjects}'
print(text)