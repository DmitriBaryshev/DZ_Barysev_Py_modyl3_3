# Задание 1
x = int(input('Введите любое целое число '))
y = int(input('Введите степень в которую возвести число '))
print('степень =', x**y)
# Задание 2
count = 0
for i in range(100, 1000):
    num = str(i)
    if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
        count += 1
print('Количество целых чисел в диапазоне =', count)
# Задание 3
count = 0
for num in range(100, 10000):
    if len(set(str(num))) == len(str(num)):
        count += 1
print('Количество целых чисел у которых все цифры разные =', count)
# Задание 4
n, m, a = int(input()), 1, 0
while n != 0:
    d, n = n % 10, n // 10
    if d not in {3, 6}:
        a, m = a + d * m, m * 10
print(a)