print("Start")

# tipe data
a = "Angga" # string
b = 3       # integer
c = False   # boolean
d = 6
e = "3"

# percabangan

if b <= 3 and d < 6:
    print("kondisi 1")
elif e == "d":
    print("kondisi 2")
elif e == "d":
    print("kondisi 3")
elif e == "3":
    print("kondisi 4")
elif e == "3":
    print("kondisi 5")
elif e == "d":
    print("kondisi 6")
else:
    print("kondisi salah")

# perulangan

listA = [ # list / slice / array
    "angga", 
    "hello", 
    "test", 
    3,
    True
]

mapA = { # map --> key dan value
    "test": 4,
    7: "angga"
}

for k in listA:
    print("this, " + str(k))


for v in mapA:
    print(map[v])

i = 0
while i < 5:
    print("Angga")
    i = i + 1
    print(i)

n = 4
# *
# **
# ***
# ****

i = 0
while i < n:
    print(i)

print("End")