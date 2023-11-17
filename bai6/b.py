import random

def tao_tap_hop_A():
    A = []
    while len(A) < 100:
        A.append(random.randint(1, 1000))
    return A
A = tao_tap_hop_A()
print("Tập hợp 100 số ngẫu nhiên trong khoảng [1,1000] là:", A)

def tao_tap_hop_B(A):
    B=(random.sample(A, 20))
    return B
def bai6_b():
    B = tao_tap_hop_B(A)
    print("Tập hợp 20 số ngẫu nhiên trong tập hợp A là:", B)
bai6_b()