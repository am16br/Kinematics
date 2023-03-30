import numpy as np
from matplotlib import pyplot as plt

xmin, xmax = 0, 10
ymin, ymax = -5, 5

xpoints, ypoints = 200, 200

x = np.linspace(xmin, xmax, xpoints)
y = np.linspace(ymin, ymax, ypoints)

xx, yy = np.meshgrid(x, y, sparse = False)

points = np.concatenate([xx.reshape(-1, 1), yy.reshape(-1, 1)], axis=-1)
points

source1=np.array([0, 0.5])
source2=np.array([0, -0.5])

points1 = points - source1
points2 = points - source2

A1= 4
A2= 4
k = 20

wave1 = A1*(np.sin( k * (points1[:, 0]**2 + points1[:, 1]**2)**0.5))
wave2 = A2*(np.sin( k * (points2[:, 0]**2 + points2[:, 1]**2)**0.5))

# superposition of two waves

A = (wave1 + wave2)
intensity = A**2

#  constructive, destructive

plt.figure(figsize=(7, 7))
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

plt.scatter(points[:, 0], points[:, 1], c = intensity, cmap=plt.cm.binary)

plt.scatter(*source1, c='red')
plt.scatter(*source2, c='red')

interval = 0.5
radius = np.linspace(xmin, xmax, int((xmax-xmin)/interval))
velocity = 0.02

from IPython.display import display, clear_output
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(7, 7))
plt.xlim(xmin, xmax-1)
plt.ylim(ymin, ymax)

cs1, cs2 = [], []

for r in radius:
  circle1=plt.Circle(source1, r, facecolor=(1, 0, 0, 0), edgecolor='red')
  cs1.append(ax.add_artist(circle1))

  circle2=plt.Circle(source2, r, facecolor=(1, 0, 0, 0), edgecolor='yellow')
  cs2.append(ax.add_artist(circle2))

plt.scatter(*source1, c='white')
plt.scatter(*source2, c='white')

for i in range(10000):
  [c.set_radius(radius[i]) for i, c in enumerate(cs1)]
  [c.set_radius(radius[i]) for i, c in enumerate(cs2)]
  radius = (radius + velocity)%(xmax-xmin)

  #clear_output(wait=True)
  #display(fig)
plt.show()
