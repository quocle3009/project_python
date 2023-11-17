def la_so_nguyen_to(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    i = 3
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 2
    return 1

def bai3_b():
    n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
    while n < 50 or n > 150:
        n = int(input("Nhập lại số tự nhiên n (50 <= n <= 150): "))
    ket_qua = la_so_nguyen_to(n)
    if ket_qua == 1:
        print(f"{ket_qua}, {n} là số nguyên tố.")
    else:
        print(f"{ket_qua}, {n} là không phải là số nguyên tố.")

# bai3_b()