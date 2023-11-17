def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def tinh_tong_va_in_so_nguyen_to(n):
    tong = 0
    so_nguyen_to = []
    for i in range(2, n):
        if la_so_nguyen_to(i):
            so_nguyen_to.append(i)
            tong += i
    print(f'Các số nguyên tố nhỏ hơn {n} là : {so_nguyen_to}')
    return tong

def bai2_a():
    n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
    while n < 50 or n > 150:
        n = int(input("Nhập lại số tự nhiên n (50 <= n <= 150): "))
    tong = tinh_tong_va_in_so_nguyen_to(n)
    print("Tổng các số nguyên tố nhỏ hơn", n, "là:", tong)

bai2_a()