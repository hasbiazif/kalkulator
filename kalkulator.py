import math

def tambah(a, b):
    """mengembalikan hasil penjumlahan a + b """
    return a + b

def kurang(a, b):
    """mengembalikan hasil pengurangan a - b"""
    return a - b

def kali(a, b):
    """mengembalikan hasil kali a x b"""
    return a * b

def bagi(a, b):
    """mengembalikan hasil bagi a : b"""
    if b == 0:
        return "Error: Tidak bisa dibagi dengan 0"
    
    return a / b

def pangkat(a, b):
    """mengembalikan hasil pangkat a pangkat b"""
    return a ** b

def akar(a):
    """mengembalikan hasil akar a"""
    return math.sqrt(a)

def persen(a):
    """mengembalikan hasil persen a"""
    return a/100

def sin(a):
    """Mengembalikan sinus dari a (dalam derajat)."""
    return math.sin(math.radians(a))

def cos(a):
    """Mengembalikan cosinus dari a (dalam derajat)."""
    return math.cos(math.radians(a))

def tan(a):
    """Mengembalikan tangen dari a (dalam derajat)."""
    return math.tan(math.radians(a))

def log(a):
    """Mengembalikan logaritma dari a."""
    return math.log10(a)

def ln(a):
    """Mengembalikan logaritma natural dari a."""
    return math.log(a)

if __name__ == "__main__":
    print("10 + 4 =", tambah(10, 4))
    print("10 - 4 =", kurang(10, 4))
    print("10 x 4 =", kali(10, 4))
    print("10 : 0 =", bagi(10, 0))
    print("10 : 2 =", bagi(10, 2))
    print("2 ^ 3 =", pangkat(2, 3))
    print("akar 9 =", akar(9))
    print("50% =", persen(50))
    print("sin 30 =", sin(30))
    print("cos 60 =", cos(60))
    print("tan 45 =", tan(45))
    print("log 100 =", log(100))
    print("ln 1 =", ln(1)) 