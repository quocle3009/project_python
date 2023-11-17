def in_diem_so_chan(A):
    print("Các môn học có điểm số chắn là:")
    for mon_hoc, diem in A.items():
        if diem % 2 == 0:
            print(f"Môn học: {mon_hoc}, Điểm số: {diem}")

def bai7_c():
    A = {"Toan" : 9, "Van" : 5, "Su" : 8, "Dia" : 7, "Hoa" : 6}
    in_diem_so_chan(A)
# bai7_c()