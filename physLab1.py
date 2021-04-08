import math
import matplotlib.pyplot as plt

xcor = []
ycor = []

alpha = 0  # starting angle
print('угол старта(в градусах): ')
alpha = float(input())
alpha = alpha / 180 * math.pi

mr = 0  # rocket mass
print('масса ракеты(т): ')
mr = float(input())

mt = 0  # oil mass
print('масса топлива(т): ')
mt = float(input())

u = 0  # speed of gas
print('скорость истечения газа из сопла ракеты(м/с): ')
u = float(input())

av = 0  # gas burning rate
print('скорость сжигания топлива(т/с): ')
av = float(input())

# M = 0 #earth mass
print('масса земли / 10**24 (кг)')
M = float(input())
M *= 10 ** 24

tk = 0.0  # end time
print('время конечное(c)')
tk = int(input())

# consts
R = 6371000
G = 6.67 * 10 ** -11
dt = 0.1
M = 5.97 * (10 ** 24)
g = G * M / (R ** 2)


def massUpgrade(m):
    global av, mr, u
    if (m-av * 0.1>=mr):
        m = m-av * dt
    else:
        u = 0
    return m


m = mr+mt
a = 0
x = 0.0
y = 0.0
xcor.append(x)
ycor.append(y)
v = 0.0
t = 1
while (t / 10<=tk):

    m = massUpgrade(m)

    a = (av * u) / m-g * (R ** 2) / ((R+y) ** 2) * math.sin(alpha)

    v = v+a * dt
    xOld = x
    yOld = y

    y = y+v * math.sin(alpha) * dt
    x = x+v * math.cos(alpha) * dt
    alpha = alpha-g * (R ** 2) / ((R+y) ** 2) * math.cos(alpha) * dt / v

    if (t % 10 == 0):
        print('-' * 20)
        print('t=', t // 10)
        print('x= ', x, ' y= ', y)
        print('m=', m)
        print('angle=', alpha * 180 / math.pi)
        print('v=', v)
        print('vx=', (x-xOld) / dt)
        print('vy=', (y-yOld) / dt)

    xcor.append(x)
    ycor.append(y)

    # print(x,y)
    if (y<0):
        print('Crash!')
        break

    t += 1

plt.axis("equal")
plt.xlabel("x")  # ось абсцисс
plt.ylabel("y")  # ось ординат
plt.grid()  # включение отображение сетки
plt.plot(xcor, ycor)
plt.show()
