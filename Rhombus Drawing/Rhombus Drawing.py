# First way
n = int(input('Enter Number: '))
for i in range(n):
    print((n-i)*' ' + (((i+1)*2)-1)*'*')
print(((2*n)+1)*'*')
for j in range(n):
    print((j+1)*' ' + (2*n-(((j+1)*2)-1))*'*')


# second way
# n = int(input('Enter Number: '))
# i = 0
# while i <= 2*n+1:
#     if i < n:
#         print(' ' * (n-i), end='')
#         print('*' * (2*i+1), end='')
#     else:
#         print(' ' * (i-n), end='')
#         print('*' * (4*n-2*i+1), end='')
#     i += 1
#     print()