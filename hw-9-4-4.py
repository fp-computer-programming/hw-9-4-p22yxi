# Yongdong Xi
def sum_nums(num1, num2):
    if num1 == num2:
        print(num1)
    if num2 > num1:
        nums = num2 + 1 - num1
        total = ((num2 + num1) * nums) / 2 
        print(total)
    elif num2 < num1:  
        nums = num1 + 1 - num2
        total = ((num2 + num1) * nums) / 2 
        print(total)


sum_nums(3,3)
