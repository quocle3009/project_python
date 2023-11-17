def dao_nguoc_tu_dien(A):
    B = {diem: mon_hoc for mon_hoc, diem in A.items()}
    return B

def bai7_f():
    A = {"Toan" : 9, "Van" : 5, "Su" : 8, "Dia" : 7, "Hoa" : 6}
    B = dao_nguoc_tu_dien(A)
    print("Từ điển đã đảo ngược:", B)
# bai7_f()