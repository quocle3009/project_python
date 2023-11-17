def dem_so_lan_xuat_hien(Str1, Str2):
    count = start = 0
    while start < len(Str1):
        pos = Str1.find(Str2, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

def bai5_b():
    Str1 = input("Nhập xâu Str1: ")
    Str2 = input("Nhập xâu Str2: ")

    count = dem_so_lan_xuat_hien(Str1, Str2)
    if count == 0 :
        print(f"xâu {Str2} không nằm trong xâu {Str1}") 
    else:
        print(f"Xâu {Str2} xuất hiện trong xâu {Str1} {count} lần.")
bai5_b()