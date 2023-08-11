

def get_psi(x1_const: float, x1: float):
    return x1 - x1_const


def get_psi1(fi: float, x10: float):
    return x10 - fi


def get_psi2(psi: float, k: float, x11: float):
    return psi + k*x11
