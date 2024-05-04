# Модуль 1. Дополнительное практическое задание по модулю: "Базовые структуры данных."

# tuple, set, list, dict

# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Инициализация словаря, преобразование множества в список и сортировка списка
average_grades = dict()
students = list(students)
students.sort()

# Собственно наполнение словаря
for i in range(students.__len__()):
    average_grades.update({students[i]: sum(grades[i]) / grades[i].__len__()})

# Ну и вывод полученного словаря на консоль
print(average_grades)
