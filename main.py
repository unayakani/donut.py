import math
import matplotlib.pyplot as plt
import numpy as np

PI = math.pi
N_DIV = 28
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
        x_vl, y_vl, z_vl = list(), list(), list()
        for x, y, z in zip(xo, yo, zo):
                xn = x * (math.cos(theta)) ** 2 - y * math.cos(theta) * math.sin(theta) + z * math.sin(theta)
                yn = x * (math.sin(theta)) ** 2 * math.cos(theta) + x * math.cos(theta) * math.sin(theta) + y * (math.cos(theta)) ** 2 - y * (math.sin(theta)) ** 3 - z * math.sin(theta) * math.cos(theta)
                zn = x * (math.sin(theta)) ** 2 - x * (math.cos(theta)) ** 2 * math.sin(theta) + y * (math.sin(theta)) ** 2 * math.cos(theta) + y * math.sin(theta) * math.cos(theta) + z * (math.cos(theta)) ** 2
                x_vl.append(xn)
                y_vl.append(yn)
                z_vl.append(zn)

        # fig.scatter(x_vl, y_vl, z_vl)
        fig.plot_trisurf(x_vl, y_vl, z_vl, cmap="viridis")
        plt.pause(0.15)
        xo, yo, zo = x_vl.copy(), y_vl.copy(), z_vl.copy()
