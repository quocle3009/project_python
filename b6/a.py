import random

def tao_tap_hop_A():
    A = set()
    while len(A) < 100:
        A.add(random.randint(1, 1000))
    return A

# def bai