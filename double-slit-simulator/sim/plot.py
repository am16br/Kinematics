from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

def update_plot_3d(step, x, y, z_over_time, plot, ax):
    #print(f"Step {step + 1} from {steps}")
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, z_over_time[:,:,step], rstride=quality, cstride=quality, cmap=plt.cm.winter, linewidth=0, antialiased=True)

def create_animated_3d_plot(x, y, z_over_time, type_of_simulation):
    fig = plt.figure(figsize = (20, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(azim = 0, elev = 90)
    ax.set_zticks([])
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.autoscale(tight=True)

    plot = [ax.plot_surface(x, y, z_over_time[:,:,0], rstride=quality, cstride=quality, cmap=plt.cm.winter, linewidth=0, antialiased=True)]

    ani = FuncAnimation(fig, update_plot_3d, frames = steps, fargs = (x, y, z_over_time, plot, ax), blit = False)

    ani.save(f"{type_of_simulation}_-_animated_3d.gif", writer = PillowWriter(fps = steps // 2))

def update_plot_wall(step, wall_over_time, sum_over_time, plots, y):
    print(f"Step {step + 1} from {steps}")
    plots[0].set_data(y, wall_over_time[:, step])
    plots[1].set_data(y, sum_over_time[:, step])

    return [plots]

def create_animated_wall_plot(breadth, z_over_time, type_of_simulation):
    fig = plt.figure(figsize = (12, 6))
    ax = fig.add_subplot(111)
    ax.xaxis.set_ticklabels([])
    ax.xaxis.set_ticks([])

    y = np.arange(-breadth, breadth, 0.05)

    wall_over_time = z_over_time[:, -1, :]
    plt.ylim((-0.2, np.amax(wall_over_time) + 0.2))
    plt.ylabel("Intensity over Time")

    sum_over_time = np.zeros((len(y), steps))
    sum_over_time[:, 0] = wall_over_time[:, 0] / steps

    for step in range(1, steps):
        sum_over_time[:, step] = sum_over_time[:, step - 1] + wall_over_time[:, step] / steps

    plots = [ax.plot(y, wall_over_time[:, 0])[0], ax.plot(y, sum_over_time[:, 0])[0]]

    ani = FuncAnimation(fig, update_plot_wall,
                        frames = steps,
                        fargs = (wall_over_time, sum_over_time, plots, y),
                        blit = False)

    ani.save(f"{type_of_simulation}_-_animated_wall.gif", writer = PillowWriter(fps = steps // 3))

    plt.clf()
    ax = fig.add_subplot(111)
    ax.xaxis.set_ticklabels([])
    ax.xaxis.set_ticks([])
    plt.ylim((-0.2, np.amax(wall_over_time) + 0.2))
    plt.ylabel("Intensity over Time")
    plt.plot(sum_over_time[:, -1], color="orange")
    #plt.show()
    plt.savefig(f"{type_of_simulation}_-_wall_result.png")
