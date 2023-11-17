import pickle

class NhanVien:
    def __init__(self, hoten, tuoi, luong):
        self.hoten = hoten
        self.tuoi = tuoi
        self.luong = luong

def nhap_du_lieu_NV():
    so_luong_NV = int(input("Nhập số lượng nhân viên: "))
    danh_sach_NV = []
    for _ in range(so_luong_NV):
        hoten = input("Nhập họ tên: ")
        tuoi = int(input("Nhập tuổi: "))
        luong = float(input("Nhập lương: "))
        nv = NhanVien(hoten, tuoi, luong)
        danh_sach_NV.append(nv)
    return danh_sach_NV

def sap_xep_theo_tuoi(danh_sach_NV):
    return sorted(danh_sach_NV, key=lambda x: x.tuoi, reverse=True)

def ghi_vao_tap_tin(danh_sach_NV, ten_tap_tin):
    with open(ten_tap_tin, 'wb') as file:
        pickle.dump(danh_sach_NV, file)

def doc_tu_tap_tin(ten_tap_tin):
    with open(ten_tap_tin, 'rb') as file:
        danh_sach_NV = pickle.load(file)
    return danh_sach_NV

def in_danh_sach_NV(danh_sach_NV):
    for nv in danh_sach_NV:
        print(f"Ho ten: {nv.hoten}, Tuoi: {nv.tuoi}, Luong: {nv.luong}")
def main():
    # Chương trình chính
    danh_sach_NV = nhap_du_lieu_NV()

    # Câu c)
    danh_sach_NV_sap_xep = sap_xep_theo_tuoi(danh_sach_NV)
    print("\nDanh sach nhan vien sau khi sap xep theo tuoi:")
    in_danh_sach_NV(danh_sach_NV_sap_xep)

    # Câu d)
    ghi_vao_tap_tin(danh_sach_NV, 'NhanVien.txt')
    print("\nDanh sach nhan vien da duoc ghi vao file 'NhanVien.txt'.")

    # Câu e)
    danh_sach_NV_tu_tap_tin = doc_tu_tap_tin('NhanVien.txt')
    print("\nDanh sach nhan vien doc tu file 'NhanVien.txt':")
    in_danh_sach_NV(danh_sach_NV_tu_tap_tin)
