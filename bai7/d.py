def tinh_trung_binh_diem(A):
    tong_diem = sum(A.values())
    so_luong_diem = len(A)
    trung_binh = tong_diem / so_luong_diem
    return trung_binh

def bai7_d():
    A = {"Toan" : 9, "Van" : 5, "Su" : 8, "Dia" : 7, "Hoa" : 6}
    trung_binh = tinh_trung_binh_diem(A)
    print("Điểm trung bình:", trung_binh)
# bai7_d()