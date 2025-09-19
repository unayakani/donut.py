import math
import plotly.express as px

R2 = 2
R1 = 1
N_DIV = 12
THETA = 2 * math.pi / N_DIV;

def circle():
    x_vals = []
    y_vals = []
    theta = 0
    for _ in range(N_DIV):
        x_vals.append(R1 * math.cos(theta))
        y_vals.append(R1 * math.sin(theta))
        theta += THETA
    return x_vals, y_vals

def circle_transpose(x_vals, y_vals):
    x_vals_transpose = list()
    y_vals_transpose = list()
    for i, j in zip(x_vals, y_vals):
        x_vals_transpose.append(i + R2 + R1)
        y_vals_transpose.append(j)
    return x_vals_transpose, y_vals_transpose

def torus(x_vals, y_vals):
    z_vals = list()
    new_x_vals = list()
    new_y_vals = list()
    for x, y in zip(x_vals, y_vals):
        for _ in range(N_DIV):
            new_x_vals.append(R2 * math.cos(x))
            new_y_vals.append(y)
            z_vals.append(R2 * math.sin(x))
    return new_x_vals, new_y_vals, z_vals

x, y, z = torus(*(circle_transpose(*(circle()))))

fig = px.scatter_3d(x=x, y=y, z=z)
fig.show()
