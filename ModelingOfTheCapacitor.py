import math
import matplotlib.pyplot as plt

U = 0
print('напряжение: ')
U = float(input())  # 220

R = 0
print('внешний радиус: ')
R = float(input())  # 0.55

r = 0
print('расстояние между обкладками: ')
r = float(input())  # 0.2

l = 0
print('длина конденсатора: ')
l = float(input())  # 0.5

e = 1  # диэлэектрическая проницательность
v = 0
vx = 0
print('изначальная скорость электрона: ')
vx = float(input())  # 600000
vy = 0

q = 1.6 * 10 ** -19  # заряд
m = 9.11 * 10 ** -31  # масса

x = 0  # начальные координаты
y = (R-r) / 2  # по x и y

dt = 1 / 10 ** 11  # частота измерения


Vcords = []

size = 0
Ycords = []
Xcords = []
Acords = []
vyCords = []

while (x<=l):
    a = (q * (U / (math.log(R / r) * (r+y)))) / m
    v = (vx ** 2+vy ** 2) ** 0.5
    vy = vy+a * dt
    y = y+vy * dt
    x = x+vx * dt
    size += 1
    Acords.append(a)
    Vcords.append(v)
    Ycords.append(y)
    Xcords.append(x)
    vyCords.append(vy)

a = 0
# после вылета из конденсатора
for o in range(5000):
    y = y+vy * dt
    x = x+vx * dt
    size += 1
    Ycords.append(y)
    Xcords.append(x)
    Acords.append(a)
    vyCords.append(vy)
    Vcords.append(v)

time = [_ for _ in range(size)]
# plt.axis("equal")
plt.plot(Ycords, Xcords)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
plt.plot(time, Ycords)
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()
plt.plot(time, Vcords)
plt.xlabel("t")
plt.ylabel("v(t)")
plt.show()
plt.plot(time, Acords)
plt.xlabel("t")
plt.ylabel("a(t)")
plt.show()
plt.plot(time, Xcords)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()
