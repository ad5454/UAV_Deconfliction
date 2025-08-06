import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import numpy as np


def plot_3d_trajectories(primary, simulations, conflicts):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot primary drone
    x_p = [wp['pos'][0] for wp in primary['waypoints']]
    y_p = [wp['pos'][1] for wp in primary['waypoints']]
    z_p = [wp['pos'][2] for wp in primary['waypoints']]
    ax.plot(x_p, y_p, z_p, c='blue', label='Primary Drone')
    ax.scatter(x_p, y_p, z_p, c='blue')

    # Plot simulated drones
    for sim in simulations:
        x_s = [wp['pos'][0] for wp in sim['waypoints']]
        y_s = [wp['pos'][1] for wp in sim['waypoints']]
        z_s = [wp['pos'][2] for wp in sim['waypoints']]
        ax.plot(x_s, y_s, z_s, '--', label=f"Sim Drone {sim['id']}", c='red')

    # Plot all conflict points
    for idx, conflict in enumerate(conflicts):
        x, y, z = conflict['location']
        ax.scatter(x, y, z, c='black', marker='x', s=100, label='Conflict Point' if idx == 0 else "")

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D UAV Conflict Detection')
    ax.legend()
    plt.tight_layout()
    plt.show()


def animate_and_save_flights(primary, simulations, conflicts, save_path="uav_deconfliction_4D_sim.mp4"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, 100)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('4D UAV Simulation')

    # Flatten waypoints
    drone_paths = {}
    for drone in [primary] + simulations:
        drone_paths[drone['id']] = [
            (wp['pos'][0], wp['pos'][1], wp['pos'][2], wp['t'][0])
            for wp in drone['waypoints']
        ]

    all_times = sorted(set([t for path in drone_paths.values() for _, _, _, t in path]))

    def update(frame):
        ax.clear()
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_zlim(0, 100)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'4D UAV Simulation - Time {frame}')

        # Plot full path as faint background
        for drone in [primary] + simulations:
            x_full = [wp['pos'][0] for wp in drone['waypoints']]
            y_full = [wp['pos'][1] for wp in drone['waypoints']]
            z_full = [wp['pos'][2] for wp in drone['waypoints']]
            style = '-' if 'sim' not in drone['id'] else '--'
            color = 'blue' if 'sim' not in drone['id'] else 'red'
            ax.plot(x_full, y_full, z_full, style, color=color, alpha=0.2)

        # Plot real-time trajectory
        for drone_id, path in drone_paths.items():
            xs, ys, zs = [], [], []
            for x, y, z, t in path:
                if t <= frame:
                    xs.append(x)
                    ys.append(y)
                    zs.append(z)
            if xs:
                style = '-' if 'sim' not in drone_id else '--'
                color = 'blue' if 'sim' not in drone_id else 'red'
                ax.plot(xs, ys, zs, style, color=color, label=drone_id)
                ax.scatter(xs[-1:], ys[-1:], zs[-1:], c=color, s=40)

        # Draw conflict points
        for conflict in conflicts:
            cx, cy, cz = conflict['location']
            ax.scatter(cx, cy, cz, c='black', marker='x', s=100)

        ax.legend()

    ani = animation.FuncAnimation(fig, update, frames=all_times, repeat=False)
    ani.save("uav_deconfliction_4D_sim.gif", writer='pillow', fps=1)
    plt.close()
