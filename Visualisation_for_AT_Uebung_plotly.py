import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd

import numpy
from stl import mesh
# fig.add_trace( ... )
# fig.update_layout( ... )


def stl2mesh3d(stl_mesh):
    # stl_mesh is read by nympy-stl from a stl file; it is  an array of faces/triangles (i.e. three 3d points)
    # this function extracts the unique vertices and the lists I, J, K to define a Plotly mesh3d
    p, q, r = stl_mesh.vectors.shape #(p, 3, 3)
    # the array stl_mesh.vectors.reshape(p*q, r) can contain multiple copies of the same vertex;
    # extract unique vertices from all mesh triangles
    vertices, ixr = np.unique(stl_mesh.vectors.reshape(p*q, r), return_inverse=True, axis=0)
    I = np.take(ixr, [3*k for k in range(p)])
    J = np.take(ixr, [3*k+1 for k in range(p)])
    K = np.take(ixr, [3*k+2 for k in range(p)])
    return vertices, I, J, K

# Using an existing stl file:
my_mesh = mesh.Mesh.from_file('C:/Users/smhhborg/Downloads/Koerper1.stl')

vertices, I, J, K = stl2mesh3d(my_mesh)
x, y, z = vertices.T
colorscale = [[0, '#e5dee5'], [1, '#e5dee5']]
mesh3D = go.Mesh3d(
            x=x,
            y=y,
            z=z,
            i=I,
            j=J,
            k=K,
            color='lightpink',
            opacity=0.50,
            name='AT&T',
            showscale=False)


test_1, test_2, test_3 = [], [], []
test_4, test_5, test_6 = [], [], []

for a, b, c in zip(x, y, z):
    if c == 0:
        if b >= 110:
            test_1.append(a)
            test_2.append(b)
            test_3.append(c)
        else:
            test_4.append(a)
            test_5.append(b)
            test_6.append(c)

edge_1_x = [min(test_4), min(test_1)]
edge_1_y = [max(test_5), max(test_2)]
edge_1_z = [50, 50]
edge_2_x = [max(test_4), max(test_1)]
edge_2_y = [min(test_5), min(test_2)]
edge_2_z = [50, 50]
edge_3_x = [min(test_4), min(test_1)]
edge_3_y = [max(test_5), max(test_2)]
edge_3_z = [0, 0]
edge_4_x = [max(test_4), max(test_1)]
edge_4_y = [min(test_5), min(test_2)]
edge_4_z = [0, 0]
edge_5_x = [min(test_4), min(test_4)]
edge_5_y = [max(test_5), max(test_5)]
edge_5_z = [0, 50]

fig = go.Figure(data=[mesh3D,
                      go.Scatter3d(x=test_1, y=test_2, z=test_3, mode='lines', line=dict(color='black', width=10)),
                      go.Scatter3d(x=test_1, y=test_2, z=[(i_1 + 50) for i_1 in test_3], mode='lines', line=dict(color='black', width=10)),
                      go.Scatter3d(x=test_4, y=test_5, z=test_6, mode='lines', line=dict(color='black', width=10)),
                      go.Scatter3d(x=test_4, y=test_5, z=[(i_1 + 50) for i_1 in test_6], mode='lines', line=dict(color='black', width=10)),
                      go.Scatter3d(x=edge_1_x, y=edge_1_y, z=edge_1_z, mode='lines', line=dict(color='black', width=10)),
                      go.Scatter3d(x=edge_2_x, y=edge_2_y, z=edge_2_z, mode='lines', line=dict(color='black', width=10)),
                      go.Scatter3d(x=edge_3_x, y=edge_3_y, z=edge_3_z, mode='lines', line=dict(color='black', width=10)),
                      go.Scatter3d(x=edge_4_x, y=edge_4_y, z=edge_4_z, mode='lines', line=dict(color='black', width=10)),
                      go.Scatter3d(x=edge_5_x, y=edge_5_y, z=edge_5_z, mode='lines', line=dict(color='black', width=10))
                      ])
# fig = go.Figure(data=[mesh3D])
fig.show()
# from dash import Dash, dcc, html
#
# app = Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])
#
# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
# # Read data from a csv
# z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
# # Make data
# u = np.linspace(0, 2, 100)
# v = np.linspace(0, 2, 100)
# s = (100, 100)
# x = np.array([[0, 0], [1, 1], [1, 1]])
# y = np.array([[0, 1], [1, 2], [2, 3]])
# z = np.array([[0, 1], [1, 2.5], [2, 4]])
# x_bot = np.array([[1, 1], [2, 2]])
# y_bot = np.array([[1.2, 1.8], [1, 2]])
# z_bot = np.array([[0, 0], [0, 0]])
# x_top = np.array([[1, 1], [2, 2]])
# y_top = np.array([[1.2, 1.8], [1, 2]])
# z_top = np.array([[1, 1], [1, 1]])
# x_front = np.array([[1, 1], [1, 1]])
# y_front = np.array([[1.2, 1.8], [1.2, 1.8]])
# z_front = np.array([[0, 0], [1, 1]])
# x_back = np.array([[2, 2], [2, 2]])
# y_back = np.array([[1, 2], [1, 2]])
# z_back = np.array([[0, 0], [1, 1]])
# x_right = np.array([[1, 2], [1, 2]])
# y_right = np.array([[1.2, 1], [1.2, 1]])
# z_right = np.array([[0, 0], [1, 1]])
# x_left = np.array([[1, 2], [1, 2]])
# y_left = np.array([[1.8, 2], [1.8, 2]])
# z_left = np.array([[0, 0], [1, 1]])
# # x_right = np.array([[1, 2], [2, 1]]) # false
# # y_right = np.array([[1.2, 1], [1, 1.2]]) #false
# # z_right = np.array([[0, 0], [1, 1]]) #false
# # x_right = np.array([[1, 1], [1, 1]])
# # y_right = np.array([[1, 2], [2, 3]])
# # z_right = np.array([[1, 2.5], [2, 4]])
# x_arrow = np.array([[1, 0.5], [1, 0.5], [0.5, 0.5], [-0.5, -0.5]])
# y_arrow = np.array([[1.5, 1.5], [1.5, 1.5], [1.5, 1.5], [1.5, 1.5]])
# z_arrow = np.array([[0.5, 0], [0.5, 1], [0.25, 0.75], [0.25, 0.75]])
#
# a = np.array([[0, 0], [0, 0]])
# b = np.array([[0, 0], [1, 1]])
# c = np.array([[0, 1], [0, 1]])
#
# a1 = np.array([[1, 1], [1, 1]])
# b1 = np.array([[0, 0], [1, 1]])
# c1 = np.array([[0, 1], [0, 1]])
#
# a2 = np.array([[1, 0], [1, 0]])  # [x_vorne_unten, x_hinten_unten, x_vorne_oben, x_hinten_oben]
# b2 = np.array([[1, 1], [1, 1]])  # [y_vorne_unten, y_hinten_unten, y_vorne_oben, y_hinten_oben]
# c2 = np.array([[0, 0], [1, 1]])  # [z_vorne_unten, z_hinten_unten, z_vorne_oben, z_hinten_oben]
#
# a3 = np.array([[1, 0], [1, 0]])
# b3 = np.array([[0, 0], [0, 0]])
# c3 = np.array([[0, 0], [1, 1]])
#
# x4 = np.array([[0, 0], [1, 1]])
# y4 = np.array([[0, 1], [0, 1]])
# z4 = np.array([[0, 0], [0, 0]])
#
# x5 = np.array([[0, 0], [1, 1]])
# y5 = np.array([[0, 1], [0, 1]])
# z5 = np.array([[1, 1], [1, 1]])
#
# fig = go.Figure(data=[go.Surface(x=a, y=b, z=c, showscale=False),
#                       go.Surface(x=a1, y=b1, z=c1, showscale=False),
#                       go.Surface(x=a2, y=b2, z=c2, showscale=False),
#                       go.Surface(x=a3, y=b3, z=c3, showscale=False),
#                       go.Surface(x=x4, y=y4, z=z4, showscale=False),
#                       go.Surface(x=x5, y=y5, z=z5, showscale=False),
#                       go.Cone(x=[1], y=[1], z=[1], u=[1], v=[1], w=[0])])
#
# # fig.update_layout(title='Mt Bruno Elevation', autosize=False,
# #                   width=500, height=500,
# #                   margin=dict(l=65, r=50, b=65, t=90))
#
# fig.show()


#
# # fig = plt.figure()
# # ax = fig.add_subplot(projection='3d')
# #
# # # Make data
# # u = np.linspace(0, 2 * np.pi, 100)
# # v = np.linspace(0, np.pi, 100)
# # x = 10 * np.outer(np.cos(u), np.sin(v))
# # y = 10 * np.outer(np.sin(u), np.sin(v))
# # z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
# #
# # # Plot the surface
# # ax.plot_surface(x, y, z)
# #
# # # Set an equal aspect ratio
# # ax.set_aspect('equal')
# #
# # plt.show()
#
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# # Make data
# # u = np.linspace(0, 2, 100)
# # v = np.linspace(0, 2, 100)
# # s = (100, 100)
# # x = 10 * np.outer(u, v)
# # y = 10 * np.outer(u, v)
# # z = 10 * np.outer(u, 2*v)
# #
# # # Plot the surface
# # ax.plot_surface(x, y, z)
# #
# # # Set an equal aspect ratio
# # ax.set_aspect('equal')
# #
# # plt.show()
#
# # Make data
# u = np.linspace(0, 2, 100)
# v = np.linspace(0, 2, 100)
# s = (100, 100)
# x = np.array([[0, 0], [1, 1], [1, 1]])
# y = np.array([[0, 1], [1, 2], [2, 3]])
# z = np.array([[0, 1], [1, 2.5], [2, 4]])
# x_bot = np.array([[1, 1], [2, 2]])
# y_bot = np.array([[1.2, 1.8], [1, 2]])
# z_bot = np.array([[0, 0], [0, 0]])
# x_top = np.array([[1, 1], [2, 2]])
# y_top = np.array([[1.2, 1.8], [1, 2]])
# z_top = np.array([[1, 1], [1, 1]])
# x_front = np.array([[1, 1], [1, 1]])
# y_front = np.array([[1.2, 1.8], [1.2, 1.8]])
# z_front = np.array([[0, 0], [1, 1]])
# x_back = np.array([[2, 2], [2, 2]])
# y_back = np.array([[1, 2], [1, 2]])
# z_back = np.array([[0, 0], [1, 1]])
# x_right = np.array([[1, 2], [1, 2]])
# y_right = np.array([[1.2, 1], [1.2, 1]])
# z_right = np.array([[0, 0], [1, 1]])
# x_left = np.array([[1, 2], [1, 2]])
# y_left = np.array([[1.8, 2], [1.8, 2]])
# z_left = np.array([[0, 0], [1, 1]])
# # x_right = np.array([[1, 2], [2, 1]]) # false
# # y_right = np.array([[1.2, 1], [1, 1.2]]) #false
# # z_right = np.array([[0, 0], [1, 1]]) #false
# # x_right = np.array([[1, 1], [1, 1]])
# # y_right = np.array([[1, 2], [2, 3]])
# # z_right = np.array([[1, 2.5], [2, 4]])
# x_arrow = np.array([[1, 0.5], [1, 0.5], [0.5, 0.5], [-0.5, -0.5]])
# y_arrow = np.array([[1.5, 1.5], [1.5, 1.5], [1.5, 1.5], [1.5, 1.5]])
# z_arrow = np.array([[0.5, 0], [0.5, 1], [0.25, 0.75], [0.25, 0.75]])
# # Plot the surface
# ax.plot_surface(x_bot, y_bot, z_bot, color='gray', alpha=0.7)
# ax.plot_surface(x_top, y_top, z_top, color='gray', alpha=0.7)
# ax.plot_surface(x_front, y_front, z_front, color='gray', alpha=0.7)
# ax.plot_surface(x_back, y_back, z_back, color='gray', alpha=0.7)
# ax.plot_surface(x_right, y_right, z_right, color='gray')
# ax.plot_surface(x_left, y_left, z_left, color='gray')
# ax.plot_surface(x_arrow, y_arrow, z_arrow, color='red')
#
# # Set an equal aspect ratio
# ax.set_box_aspect([5, 5, 4])
# ax.set(xlim=[-1, 3], ylim=[-1, 3], zlim=[-1, 3])
# # ax.set_aspect('equal')
#
# plt.show()