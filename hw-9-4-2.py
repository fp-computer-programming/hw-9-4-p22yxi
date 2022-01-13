# Yongdong Xi
def products(number_lst, value):
    for index, element in enumerate(number_lst):
        number_lst[index] = index * value
    return number_lst


print(products([1, 2, 3, 4, 5, 6, 8], 4))