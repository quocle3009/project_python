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

def dem_so_nguyen_to_nho_hon_n(n):
    count = 0
    for i in range(2, n):
        if la_so_nguyen_to(i):
            count += 1
    return count

def bai3_d():
    n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
    while n < 50 or n > 150:
        n = int(input("Nhập lại số tự nhiên n (50 <= n <= 150): "))
    count = dem_so_nguyen_to_nho_hon_n(n)
    print("Số các số nguyên tố nhỏ hơn", n, "là:", count)

# bai3_d()