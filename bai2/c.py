def tinh_tong_so_chan(n):
    tong = 0
    for i in range(2, n + 1, 2):
        tong += i
    return tong


def bai2_c():
    n = int(input("Nhập một số tự nhiên n (50 <= n <= 150): "))
    while n < 50 or n > 150:
        n = int(input("Nhập lại số tự nhiên n (50 <= n <= 150): "))
    tong_so_chan = tinh_tong_so_chan(n)
    print("Tổng các số chẵn từ 1 đến", n, "sử dụng vòng lặp for là:", tong_so_chan)
bai2_c()