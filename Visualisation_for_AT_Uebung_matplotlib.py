import matplotlib.pyplot as plt
import numpy as np


# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# # Make data
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 100)
# x = 10 * np.outer(np.cos(u), np.sin(v))
# y = 10 * np.outer(np.sin(u), np.sin(v))
# z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
#
# # Plot the surface
# ax.plot_surface(x, y, z)
#
# # Set an equal aspect ratio
# ax.set_aspect('equal')
#
# plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data
# u = np.linspace(0, 2, 100)
# v = np.linspace(0, 2, 100)
# s = (100, 100)
# x = 10 * np.outer(u, v)
# y = 10 * np.outer(u, v)
# z = 10 * np.outer(u, 2*v)
#
# # Plot the surface
# ax.plot_surface(x, y, z)
#
# # Set an equal aspect ratio
# ax.set_aspect('equal')
#
# plt.show()

# Make data
u = np.linspace(0, 2, 100)
v = np.linspace(0, 2, 100)
s = (100, 100)
x = np.array([[0, 0], [1, 1], [1, 1]])
y = np.array([[0, 1], [1, 2], [2, 3]])
z = np.array([[0, 1], [1, 2.5], [2, 4]])
x_bot = np.array([[1, 1], [2, 2]])
y_bot = np.array([[1.2, 1.8], [1, 2]])
z_bot = np.array([[0, 0], [0, 0]])
x_top = np.array([[1, 1], [2, 2]])
y_top = np.array([[1.2, 1.8], [1, 2]])
z_top = np.array([[1, 1], [1, 1]])
x_front = np.array([[1, 1], [1, 1]])
y_front = np.array([[1.2, 1.8], [1.2, 1.8]])
z_front = np.array([[0, 0], [1, 1]])
x_back = np.array([[2, 2], [2, 2]])
y_back = np.array([[1, 2], [1, 2]])
z_back = np.array([[0, 0], [1, 1]])
x_right = np.array([[1, 2], [1, 2]])
y_right = np.array([[1.2, 1], [1.2, 1]])
z_right = np.array([[0, 0], [1, 1]])
x_left = np.array([[1, 2], [1, 2]])
y_left = np.array([[1.8, 2], [1.8, 2]])
z_left = np.array([[0, 0], [1, 1]])
# x_right = np.array([[1, 2], [2, 1]]) # false
# y_right = np.array([[1.2, 1], [1, 1.2]]) #false
# z_right = np.array([[0, 0], [1, 1]]) #false
# x_right = np.array([[1, 1], [1, 1]])
# y_right = np.array([[1, 2], [2, 3]])
# z_right = np.array([[1, 2.5], [2, 4]])
x_arrow = np.array([[1, 0.5], [1, 0.5], [0.5, 0.5], [-0.5, -0.5]])
y_arrow = np.array([[1.5, 1.5], [1.5, 1.5], [1.5, 1.5], [1.5, 1.5]])
z_arrow = np.array([[0.5, 0], [0.5, 1], [0.25, 0.75], [0.25, 0.75]])
# Plot the surface
ax.plot_surface(x_bot, y_bot, z_bot, color='gray', alpha=0.7)
ax.plot_surface(x_top, y_top, z_top, color='gray', alpha=0.7)
ax.plot_surface(x_front, y_front, z_front, color='gray', alpha=0.7)
ax.plot_surface(x_back, y_back, z_back, color='gray', alpha=0.7)
ax.plot_surface(x_right, y_right, z_right, color='gray')
ax.plot_surface(x_left, y_left, z_left, color='gray')
ax.plot_surface(x_arrow, y_arrow, z_arrow, color='red')

# Set an equal aspect ratio
ax.set_box_aspect([5, 5, 4])
ax.set(xlim=[-1, 3], ylim=[-1, 3], zlim=[-1, 3])
# ax.set_aspect('equal')

plt.show()