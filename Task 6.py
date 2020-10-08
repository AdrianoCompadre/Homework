a = int(input('Enter the result for the first day, km: '))
b = int(input('Necessary result: '))
day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day += 1
print(day)
