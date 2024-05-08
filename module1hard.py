# Модуль 1. Дополнительное практическое задание по модулю: "Базовые структуры данных."

# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразование множества с именами учеников в список и сортировка списка
students = list(students)
students.sort()

# Инициализация списка средних оценок, расчет и заполнение значений
average_grades_list = []
for i in range(len(grades)):
    average_grades_list.append(sum(grades[i])/grades[i].__len__())

# Собственно наполнение словаря
average_grades_dic = dict(zip(students, average_grades_list))

# Ну и вывод полученного словаря на консоль
print(average_grades_dic)
