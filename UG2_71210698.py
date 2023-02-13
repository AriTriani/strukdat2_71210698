import timeit as tm
from matplotlib import pyplot as plt

#iteratif
def Bilprima1(i):
    x,y = 0,1
    for i in range(i):
        x,y = y, x+y
    return x

#rekursif
def Bilprima2(i):  
    if i <= 1:
        return i
    else:
        return Bilprima2(i-1) + Bilprima2(i-2)

Jarak = range(1,101)
Waktu = []
for i in Jarak:
    start = tm.default_timer()
    A = Bilprima1(i)
    B = "{:.10f}" .format(tm.default_timer() - start)
    Waktu.append(B)

plt.plot(Jarak, Waktu)
plt.ylabel("Time .sec")
plt.show()