from a import *
from b import *
from c import *
from d import *
from e import *
from f import *

def menu_bai7():
   menu = True
   while menu:
    print("\nMenu:")
    print("a. In ra điểm lớn nhất")
    print("b. In ra môn và điểm có điểm lớn nhất")
    print("c. In ra các điểm số chẵn")
    print("d. Tính trung bình tất cả các điểm")
    print("e. Tạo từ điển mới với các môn lớn hơn 7 điểm")
    print("f. Đảo ngược tự điển A, key thành value và ngược lại")
    print("0. Thoát")
    choice = (input("Chọn một lựa chọn (a-f): "))
    if choice == "0":
        break
    elif choice == "a":
        print("")
        bai7_a()
        print("===========================================")
        print("===========================================")
    elif choice == "b":
        print("")
        bai7_b()
        print("")
        print("===========================================")
        print("===========================================")
    elif choice == "c":
        print("")
        bai7_c()
        print("")
        print("===========================================")
        print("===========================================")
    elif choice == "d":
        print("")
        bai7_d()
        print("")
        print("===========================================")
        print("===========================================")
    elif choice == "e":
        print("")
        bai7_e()
        print("")
        print("===========================================")
        print("===========================================")
    elif choice == "f":
        print("")
        bai7_f()
        print("")
        print("===========================================")
        print("===========================================")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
    
menu_bai7()