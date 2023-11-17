#Bài 1:Chuyển độ C qua độ F
def tinh_do_F(c):
    print(f"Nhiệt độ ở độ Celsius là: {c}°C tương ứng với độ Fahrenheit là: {c*9/5+32}°F")

#bài 2: Viết chương trình nhập một số tự nhiên n (n  [50, 150]) và tính các giá trị sau
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Nhập một số tự nhiên n trong khoảng [50, 150]
while True:
    n = int(input("Nhập một số tự nhiên n trong khoảng [50, 150]: "))
    if 50 <= n <= 150:
        break
    else:
        print("Số nhập không nằm trong khoảng yêu cầu. Vui lòng nhập lại.")

# a) Tính tổng và in ra các số nguyên tố nhỏ hơn n.
sum_primes = 0
print("Các số nguyên tố nhỏ hơn n:")
for i in range(2, n):
    if is_prime(i):
        sum_primes += i
        print(i, end=" ")
print(f"\nTổng các số nguyên tố nhỏ hơn n là: {sum_primes}")

# b) Tính tổng của tất cả các ước số của n.
sum_factors = 0
print(f"Các ước số của {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        sum_factors += i
        print(i, end=" ")
print(f"\nTổng các ước số của {n} là: {sum_factors}")

# c) Tính tổng các số chẵn từ 1 đến n bằng for và while.
sum_even_for = 0
for i in range(2, n + 1, 2):
    sum_even_for += i

sum_even_while = 0
i = 2
while i <= n:
    sum_even_while += i
    i += 2

print(f"Tổng các số chẵn từ 1 đến {n} (sử dụng vòng lặp for): {sum_even_for}")
print(f"Tổng các số chẵn từ 1 đến {n} (sử dụng vòng lặp while): {sum_even_while}")

