n=int(input("enter the number:"))

n = 5

for i in range(n - 1):
    print(' ' * (n - i - 1) + '*')

print('*' * n)

for i in range(1, n):
    print(' ' * i + '*')
