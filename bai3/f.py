from a import *
from b import *
from c import *
from d import *
from e import *

def menu_bai3():
   menu = True
   while menu:
    print("\nMenu:")
    print("a. Hàm trả lại số ước số thực sự của n")
    print("b. Hàm tả lại 1 nếu n là nguyên tố, ngược lại hàm trả về 0")
    print("c. Hàm đếm số các ước số là lẻ của n")
    print("d. Hàm đếm số các số nguyên tố nhỏ hơn n.")
    print("e. Hàm tính tổng tất cả các ước số thực sự của n.")
    print("0. Thoát")
    choice = (input("Chọn một lựa chọn (a-e): "))
    if choice == "0":
        break
    elif choice == "a":
        bai3_a()
        break
    elif choice == "b":
        bai3_b()
        break
    elif choice == "c":
        bai3_c()
        break
    elif choice == "d":
        bai3_d()
        break
    elif choice == "e":
        bai3_e()
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
    
menu_bai3()