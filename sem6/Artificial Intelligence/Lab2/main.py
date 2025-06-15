import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

def gaussian(x, y, mu, sig, A):
    return np.exp(-A * ((x - mu[0])**2 + (y - mu[1])**2) / sig**2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

nr_points = 10000
x = np.random.normal(0, 0.2, nr_points)
y = np.random.normal(0, 0.2, nr_points)
z = [0] * nr_points

vz = []
for i in range (nr_points):
    vz.append(gaussian(x[i], y[i], [0, 0], 0.2, 0.5))
z_prim = []
for i in range(nr_points):
    z_prim.append(z[i] + vz[i])

ax.scatter(x, y, z, c='r', marker='.')
for i in range(1, nr_points):
    ax.plot([x[i], x[i]], [y[i], y[i]], [z[i], z_prim[i]], c='b')

deltaT = 0.1

def animate_particles():

    new_x = []
    new_y = []
    new_z = []
    for i in range(nr_points):
        new_x.append(x[i] + np.random.normal(0, 0.01))
        new_y.append(y[i] + np.random.normal(0, 0.01))
        new_z.append(z_prim[i] + vz[i] * deltaT)
    for i in range(1, nr_points):
        ax.plot([x[i], x[i]], [y[i], y[i]], [z[i], z_prim[i]], c='b')

iterations = 100
ani = animation.FuncAnimation(fig, animate_particles, iterations,
                                       interval=50, blit=False, repeat=True)

plt.show()