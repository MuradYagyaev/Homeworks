# Модуль 1 урок №5. "Неизменяемые и изменяемые объекты. Кортежи."
immutable_var = (1, 2, 3, ['огонь', 'вода', 'воздух'], True)
print(immutable_var)
# immutable_var[2] = 'Замена'     # TypeError: 'tuple' object does not support item assignment
immutable_var[3][1] = 'Стихия'    # Но при этом список внутри кортежа можно изменить
print(immutable_var)
mutable_list = ['Попугай', 'Муравьи', 'Мои питомцы', 13, 15]
print(mutable_list)
mutable_list[0] = 2024            # Списки можно изменять
mutable_list[3] = 4
print(mutable_list)
