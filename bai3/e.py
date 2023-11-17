def tinh_tong_uoc_so_thuc_su(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def bai3_e():
    n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
    while n < 50 or n > 150:
        n = int(input("Nhập lại số tự nhiên n (50 <= n <= 150): "))
    tong = tinh_tong_uoc_so_thuc_su(n)
    print("Tổng các ước số thực sự của", n, "là:", tong)