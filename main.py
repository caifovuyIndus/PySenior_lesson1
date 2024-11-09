print(f'lesson7\n')

numbers = [1, 2, 3, 4, 5]
print('before', numbers)

# for i in range(len(numbers)):
#     numbers[i] = numbers[i]**2
#
# print('after', numbers)

def up_square(n):
    if n % 2 != 0:
        return n**2
    return n

def check_n(n):
    return n >= 5

numbers_square = [up_square(n) for n in numbers if check_n(n)]
print('after', numbers_square)