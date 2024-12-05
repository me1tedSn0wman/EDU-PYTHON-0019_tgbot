
def custom_filter(somelist : list) -> bool:
    sumEllements = 0;

    for element in somelist:
        if type(element) is int:
            if element % 7 == 0:
                sumEllements += element

    if sumEllements<=83:
        return True
    else:
        return False


some_list = [7, 14, 28, 32, 32, 56]

print(custom_filter(some_list))

some_list = [7, 14, 28, 32, 32, '56']

print(custom_filter(some_list))