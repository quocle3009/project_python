def tao_tu_dien_moi(A):
    B = {mon_hoc: diem for mon_hoc, diem in A.items() if diem > 7}
    return B

def bai7_e():
    A = {"Toan" : 9, "Van" : 5, "Su" : 8, "Dia" : 7, "Hoa" : 6}
    B = tao_tu_dien_moi(A)
    print("Từ điển mới với các môn lớn hơn 7 điểm:", B)
# bai7_e()