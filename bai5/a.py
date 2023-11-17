def kiem_tra_xau_con(Str1, Str2):
    if Str2 in Str1:
        return True
    else:
        return False

def bai5_a():
    Str1 = input("Nhập xâu Str1: ")
    Str2 = input("Nhập xâu Str2: ")

    if kiem_tra_xau_con(Str1, Str2):
        print(f"Xâu {Str2} nằm trong xâu {Str1}.")
    else:
        print(f"Xâu {Str2} không nằm trong xâu {Str1}.")
bai5_a()