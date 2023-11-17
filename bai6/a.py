import random

def tao_tap_hop_A():
    A = []
    while len(A) < 100:
        A.append(random.randint(1, 1000))
    return A

def bai6_a():
    A = tao_tap_hop_A()
    print("Tập hợp 100 số ngẫu nhiên trong khoảng [1,1000] là:", A)
bai6_a()