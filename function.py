def tambah(a, b, c=0, d=0 ):
    if a == 0:
        print("hasil b")
        return b + c + d
    elif b == 0:
        print("hasil a")
        return a + c + d

    return a + b + c + d

def cetak(p):
    if p == 1:
        print("angka 1")
        return
    tulisan = str(p) # casting
    print("Hasilnya adalah " + tulisan)
    return

# 5! = 5 * 4! = 5 * 4 * 3 * 2 * 1 = 120
# 2! = 2 * 1! = 2
# 3! = 3 * 2! = 3 * 2 * 1 = 6
# 1! = 1 * 0! = 1
# 0! = 1 = 1
# n! = n * (n-1)!
# rekursif
def faktorial(n):
    #base case
    if n == 0:
        return 1
    if n == 1:
        return 1
    #normal case
    return n * faktorial(n-1)

hasil = faktorial(100)
cetak(hasil)