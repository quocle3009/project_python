def case1():
    print("+" * 50)
    print("{:^50}".format("Các bài toán cơ bản"))
    print("+" * 50)
    print("{:<50}".format("1: Đổi °C sang °F"))
    print("{:<50}".format("2: Các lệnh có cấu trúc"))
    print("{:<50}".format("3: Hàm số"))
    print("{:<50}".format("4: Kiểu dữ liệu danh sách (list)"))
    print("{:<50}".format("5: Kiểu dữ liệu Xâu ký tự (String)"))
    print("{:<50}".format("6: Kiểu dữ liệu tập hợp (set)"))
    print("{:<50}".format("7: Kiểu dữ liệu Từ điển (dictionary)"))
    print("{:<50}".format("8: Module và Package"))
    print("{:<50}".format("9: Đọc v ghi tệp"))
    print("{:<50}".format("10: Ngoại lệ và xử lý ngoại lệ"))
    print("{:<50}".format("11: Lập trình hướng đối tượng"))
    print("+" * 50)
    while True:
        sub_choice = int(input("Nhập lựa chọn của bạn (0 để quay lại): "))
        if sub_choice == 0:
            print("Quay lại chọn chương trình chính.")
            break
        elif sub_choice == 1:
            c = float(input("Nhập độ C: "))
            print(f"Nhiệt độ ở độ Celsius là: {c}°C tương ứng với độ Fahrenheit là: {c*9/5+32}°F")
        elif sub_choice == 2:
            print("Bạn đã chọn Option 2 trong Case 1.")
        elif sub_choice == 3:
            print("Bạn đã chọn Option 3 trong Case 1.")
        else:
            print("Lựa chọn không hợp lệ.")

def case2():
    print("+" * 50)
    print("{:^50}".format("Lập trình với thư viện"))
    print("+" * 50)
    print("{:<50}".format("1: Thư viện Numpy"))
    print("{:<50}".format("2: Thư viện Matplotlib"))
    print("{:<50}".format("3: Thư viện Sympy"))
    print("+" * 50)
    while True:
        sub_choice = int(input("Nhập lựa chọn của bạn (0 để quay lại): "))
        if sub_choice == 0:
            print("Quay lại chọn chương trình chính.")
            break
        elif sub_choice == 1:
            print("Bạn đã chọn Option 1 trong Case 2.")
        elif sub_choice == 2:
            print("Bạn đã chọn Option 2 trong Case 2.")
        elif sub_choice == 3:
            print("Bạn đã chọn Option 3 trong Case 2.")
        else:
            print("Lựa chọn không hợp lệ.")

def case3():
    print("Bạn đã chọn Case 3:")
    while True:
        sub_choice = int(input("Nhập lựa chọn của bạn (0 để quay lại): "))
        if sub_choice == 0:
            print("Quay lại chọn chương trình chính.")
            break
        elif sub_choice == 1:
            print("Bạn đã chọn Option 1 trong Case 3.")
        elif sub_choice == 2:
            print("Bạn đã chọn Option 2 trong Case 3.")
        elif sub_choice == 3:
            print("Bạn đã chọn Option 3 trong Case 3.")
        else:
            print("Lựa chọn không hợp lệ.")

while True:
    print("+" * 50)
    print("{:^50}".format("ĐỒ ÁN PYTHON"))
    print("+" * 50)
    print("{:<50}".format("1: Các bài toán cơ bản"))
    print("{:<50}".format("2: Các bài toán với thư viện"))
    print("{:<50}".format("3: Bài nâng cao"))
    print("+" * 50)
    main_choice = int(input("Nhập lựa chọn của bạn (0 để thoát): "))

    if main_choice == 0:
        print("Kết thúc chương trình.")
        break
    elif main_choice == 1:
        case1()
    elif main_choice == 2:
        case2()
    elif main_choice == 3:
        case3()
    else:
        print("Lựa chọn không hợp lệ.")
