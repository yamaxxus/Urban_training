name = 'immutable_var'
immutable_var_tuple = (1, 2, 3, 'a', 'b', 'c')
print(immutable_var_tuple)

#immutable_var_tuple[0] = 100
#при попытке изменения кортежа получаем ошибку, потому что кортеж должен быть неизменяемым, например когда требуется защитить элементы от изменений. Для изменения кортежа надо создать новый кортеж или перевести его в список, провести необходимые изменения и потом преобразовать полученный список обратно в кортеж. Пример ниже:
my_list = list(immutable_var_tuple)
my_list[0] = 100
immutable_var_new_tuple = tuple(my_list)
print(immutable_var_new_tuple)

mutable_list = [4, 5, 6, 'c', 'd', 'e']
mutable_list[-1] = 'modified'
print(mutable_list)
