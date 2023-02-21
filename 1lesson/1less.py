n = int(input("введите трёзначное число:"))
c = n % 10
a = n // 100
b = n // 10 % 10
print(a + b + c)