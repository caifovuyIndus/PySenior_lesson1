print(f'lesson7\n')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('before', numbers)

# for i in range(len(numbers)):
#     numbers[i] = numbers[i]**2
#
# print('after', numbers)



def set_up_pow(value: int, result=0):
    pow = value
    result = 0
    delim = 2


    def up_pow(n):
        if n % delim != result:
            return n**pow
        return n


    return up_pow

def check_n(n):
    return n >= 5

up_square = set_up_pow(2)
up_cube = set_up_pow(3, 1)

numbers_square = [up_cube(n) for n in numbers if check_n(n)]
print('after', numbers_square)

