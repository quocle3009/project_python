def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def tao_day_C(A, B):
    C = [uscln(a, b) for a, b in zip(A, B)]
    return C

def bai4():
    A = [12, 18, 30]
    B = [18, 24, 45]

    C = tao_day_C(A, B)
    print(f"Dãy A: {A}")
    print(f"Dãy B: {B}")
    print(f"Dãy C: {C}")
bai4()