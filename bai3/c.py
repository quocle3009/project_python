def dem_uoc_so_le(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            count += 1
    return count

def bai3_c():
    n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
    while n < 50 or n > 150:
        n = int(input("Nhập lại số tự nhiên n (50 <= n <= 150): "))
    count = dem_uoc_so_le(n)
    print("Số các ước số lẻ của", n, "là:", count)

# bai3_c()