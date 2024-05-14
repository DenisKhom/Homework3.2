#Функция с параметрами по умолчанию:
def print_params (a=14, b= 'МАЯ', c= True):
    print(a, b, c)

print_params()
print_params(25, 5, False)
print_params(a=34)
print_params(c='ПРАВДА')
print_params(b=25)
print_params (c = [1,2,3])

#Распаковка параметров:

values_list = ['I was born in', 1985, True]
print (values_list)
values_dict = {'a': '14.05.2024', 'b': 14, 'c': [1,2,3]}
print(values_dict)
print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры:

values_list2 = ['Я родился в', 1985]
print_params(*values_list2)


