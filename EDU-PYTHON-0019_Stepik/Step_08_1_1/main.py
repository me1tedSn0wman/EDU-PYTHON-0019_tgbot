import functions
from data import my_dict
from classes import *

print('this is executable file')

if __name__ == '__main__':
    print('Код ниже не выполнится, если этот файл будет импортируемым модулем в другой исполняемый файл')
    print(functions.get_double_number(100))
    print(my_dict)
    MyClass()