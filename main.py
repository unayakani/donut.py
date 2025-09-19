import math
import matplotlib.pyplot as plt

PI = math.pi
N_DIV = 50
R1 = 1
R2 = 2
THETA = 2 * PI / N_DIV
PHI = 2 * PI / N_DIV

def torus():
    x, y, z = list(), list(), list()
    R = R2 + R1
    r = R1
    phi = 0
    for _ in range(N_DIV):
        theta = 0
        for _ in range(N_DIV):
            x.append(R * math.cos(phi) + r * math.cos(theta) * math.cos(phi))
            y.append(r * math.sin(theta))
            z.append(-R * math.sin(phi) - r * math.cos(theta) * math.sin(phi))
            theta += THETA
        phi += PHI
    return x, y, z

fig = plt.axes(projection="3d")
xo, yo, zo = torus()
while True:
    fig.clear()
    fig.set_xlim(-4, 4)
    fig.set_ylim(-4, 4)
    fig.set_zlim(-4, 4)
    theta = PI / 8
    x, y, z = list(), list(), list()
    for i, j, k in zip(xo, yo, zo):
        x.append(i)
        y.append(j * math.cos(theta) - k * math.sin(theta))
        z.append(j * math.sin(theta) + k * math.cos(theta))
    fig.scatter(x, y, z)
    plt.pause(0.01)
    xo, yo, zo = x.copy(), y.copy(), z.copy()
