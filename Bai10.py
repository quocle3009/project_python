def nhap_so_nguyen(prompt):
    while True:
        try:
            so_nguyen = int(input(prompt))
            return so_nguyen
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

def tinh_phan_so(a, b):
    if b == 0:
        raise ValueError("Không thể chia cho 0.")
    return a / b

def main():
    try:
        a = nhap_so_nguyen("Nhập số nguyên a: ")
        b = nhap_so_nguyen("Nhập số nguyên b: ")
        phan_so = tinh_phan_so(a, b)
        print(f"Giá trị phân số {a}/{b} là: {phan_so}")

    except ValueError as ve:
        print(f"Lỗi: {ve}")


