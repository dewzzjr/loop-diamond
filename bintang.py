
n = 4
# *
# **
# ***
# ****

# untuk membuat bagian atas
i = 0
while i < n:
    b = i + 1
    j = 0
    bintang = ''
    while j < b:
        bintang = bintang + "*"
        j += 1
    print(bintang)
    i += 1

# ****
# ***
# **
# *

# untuk membuat bagian bawah
n = 0
i = 4
while i > n:
    print(i)
    i -= 1
