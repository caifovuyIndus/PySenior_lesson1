import logging

print(f'lesson8\n')

# logging.basicConfig(level=logging.INFO,
#                     filename='logs.txt', filemode='w',
#                     format='%(asctime)s:%(levelname)s:%(massage)s')
#
# value = 12
# delim = 0
#
# try:
#     logging.info('start app')
#
#     if delim == 0:
#         raise TypeError('delim == 0')
#
#     print(value / delim)
# except Exception as error:
#     logging.error(f'{error.__str__()}')
# finally:
#     logging.info('end app')

def sum_value(a: int, b: int):
    return a+b+1