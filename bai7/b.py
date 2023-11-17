def in_mon_hoc_diem_lon_nhat(A):
    mon_hoc = max(A, key=A.get)
    diem_lon_nhat = A[mon_hoc]
    print("Môn học có điểm lớn nhất:", mon_hoc, "với điểm số:", diem_lon_nhat)
def bai7_b():
    A = {"Toan" : 9, "Van" : 5, "Su" : 8, "Dia" : 7, "Hoa" : 6}
    in_mon_hoc_diem_lon_nhat(A)
# bai7_b()