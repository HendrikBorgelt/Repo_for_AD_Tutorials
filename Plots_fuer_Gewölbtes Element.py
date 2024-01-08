# import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from stl import mesh

import Funktionen_Differentielles_Element as fd
import Funktionen_Differentielles_Element_Torus as fdt
import Funktionen_Pfeil as fp
import Funktionen_Moment as fm
import Funktionen_Kraftfelder as fk
import Funktionen_GewoelbtesElement as fge
import BasisFunktionen as bf
import copy


mesh_differential_torus_element = mesh.Mesh.from_file('./meshes/Differentielles_Element_eines_Torus.stl')
mesh_torus_segment = mesh.Mesh.from_file('./meshes/Torussegment.stl')
mesh_hollow_torus = mesh.Mesh.from_file('./meshes/Hohl_Torus.stl')
mesh_half_tank_shell = mesh.Mesh.from_file('./meshes/Halber_Boden.stl')
mesh_half_torus_element = mesh.Mesh.from_file('./meshes/Halber_Torus.stl')
mesh3D_Differential_element_1 = fge.create_mesh3d_for_torus_element([mesh_differential_torus_element, mesh_torus_segment,
                                                                    mesh_hollow_torus, mesh_half_tank_shell,
                                                                    mesh_half_torus_element],
                                                                   1, [0, 0, 0], 0, 0, 0, [])


# mesh_differential_element_1 = mesh.Mesh.from_file('./meshes/Differentielles_Element_eines_Torus.stl')
#
# vertices, I, J, K = bf.stl2mesh3d(mesh_differential_element_1)
# x, y, z = vertices.T
#
# mesh3D_base_body_1 = go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K,
#                                color='grey', opacity=0.60, showscale=False, visible=True,
#                                contour=dict(show=True, width=16))
# fig = go.Figure(data=mesh3D_base_body_1)
# inner_line_left = []
# outer_line_left = []
# inner_line_right = []
# outer_line_right = []
# inner_line_upper = []
# inner_line_lower = []
# outer_line_upper = []
# outer_line_lower = []
# upper_left_line = []
# upper_right_line = []
# lower_left_line = []
# lower_right_line = []
#
# for i_1, i_2, i_3 in zip(x, y, z):
#     if i_1 == 0:
#         if 19.5**2 <= abs((i_2+56.569)**2+(i_3-56.569)**2) <= 20.5**2:
#             outer_line_left.append([i_1, i_2, i_3])
#         else:
#             inner_line_left.append([i_1, i_2, i_3])
#
#     elif 6 <= i_1 <= 7:
#         if 19.5**2 <= abs((i_2+56.569)**2+(i_3-56.569)**2) <= 20.5**2:
#             outer_line_right.append([i_1, i_2, i_3])
#         else:
#             inner_line_right.append([i_1, i_2, i_3])
#     # elif max(inner_line_right[2, :]) <= i_2 <= max(inner_line_left[2, :]):
#     #     inner_line_upper.append([i_1, i_2, i_3])
# for i_4, i_5, i_6 in zip(x, y, z):
#     if max([i_9[1] for i_9 in inner_line_left]) <= i_5 <= max([i_8[1] for i_8 in inner_line_right]):
#         inner_line_upper.append([i_4, i_5, i_6])
#     elif min([i_9[2] for i_9 in inner_line_left]) <= i_6 <= min([i_8[2] for i_8 in inner_line_right]):
#         inner_line_lower.append([i_4, i_5, i_6])
#     elif max([i_9[2] for i_9 in outer_line_left]) <= i_6 <= max([i_8[2] for i_8 in outer_line_right]):
#         outer_line_upper.append([i_4, i_5, i_6])
#     elif min([i_9[1] for i_9 in outer_line_left]) <= i_5 <= min([i_8[1] for i_8 in outer_line_right]) and i_6 <= 64.6:
#         outer_line_lower.append([i_4, i_5, i_6])
#     if max([i_9[1] for i_9 in inner_line_left]) == i_5 or max([i_9[1] for i_9 in outer_line_left]) == i_5:
#         upper_left_line.append([i_4, i_5, i_6])
#     elif max([i_9[1] for i_9 in inner_line_right]) == i_5 or max([i_9[1] for i_9 in outer_line_right]) == i_5:
#         upper_right_line.append([i_4, i_5, i_6])
#     elif min([i_9[1] for i_9 in inner_line_left]) == i_5 or min([i_9[1] for i_9 in outer_line_left]) == i_5:
#         lower_left_line.append([i_4, i_5, i_6])
#     elif min([i_9[1] for i_9 in inner_line_right]) == i_5 or min([i_9[1] for i_9 in outer_line_right]) == i_5:
#         lower_right_line.append([i_4, i_5, i_6])
#
# line_color = 'black'
# plty_linewidth = 2
# font_size = 16
#
# mesh3D_inner_line_left = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_left], y=[i_1[1] for i_1 in inner_line_left], z=[i_1[2] for i_1 in inner_line_left],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_line_left = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_left], y=[i_1[1] for i_1 in outer_line_left], z=[i_1[2] for i_1 in outer_line_left],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_inner_line_right = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_right], y=[i_1[1] for i_1 in inner_line_right], z=[i_1[2] for i_1 in inner_line_right],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_line_right = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_right], y=[i_1[1] for i_1 in outer_line_right], z=[i_1[2] for i_1 in outer_line_right],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_inner_line_upper = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_upper], y=[i_1[1] for i_1 in inner_line_upper], z=[i_1[2] for i_1 in inner_line_upper],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_inner_line_lower = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_lower], y=[i_1[1] for i_1 in inner_line_lower], z=[i_1[2] for i_1 in inner_line_lower],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_line_upper = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_upper], y=[i_1[1] for i_1 in outer_line_upper], z=[i_1[2] for i_1 in outer_line_upper],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_line_lower = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_lower], y=[i_1[1] for i_1 in outer_line_lower], z=[i_1[2] for i_1 in outer_line_lower],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_upper_left_line = go.Scatter3d(x=[i_1[0] for i_1 in upper_left_line], y=[i_1[1] for i_1 in upper_left_line], z=[i_1[2] for i_1 in upper_left_line],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_upper_right_line = go.Scatter3d(x=[i_1[0] for i_1 in upper_right_line], y=[i_1[1] for i_1 in upper_right_line], z=[i_1[2] for i_1 in upper_right_line],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_lower_left_line = go.Scatter3d(x=[i_1[0] for i_1 in lower_left_line], y=[i_1[1] for i_1 in lower_left_line], z=[i_1[2] for i_1 in lower_left_line],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_lower_right_line = go.Scatter3d(x=[i_1[0] for i_1 in lower_right_line], y=[i_1[1] for i_1 in lower_right_line], z=[i_1[2] for i_1 in lower_right_line],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
#
# # mesh3D_Differential_element_1 = fdt.create_mesh3d_for_dif_element_torus(mesh_differential_element_1, 1, [0, 0, 0], 0, 0, 0, frame=True)
# mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Torussegment.stl')
# # front_line_upper =
# vertices_1, I_1, J_1, K_1 = bf.stl2mesh3d(mesh_straight_arrow_1)
# x_1, y_1, z_1 = vertices_1.T
# mesh3D_base_body_2 = go.Mesh3d(x=x_1, y=y_1, z=z_1, i=I_1, j=J_1, k=K_1,
#                                color='darkgrey', opacity=0.80, showscale=False, visible=True,
#                                contour=dict(show=True, width=16))
# outer_line_left_1 = []
# inner_line_left_1 = []
# outer_line_right_1 = []
# inner_line_right_1 = []
# mesh3d_line_to_center_upper_left = go.Scatter3d(x=[i_1[0] for i_1 in upper_left_line], y=[i_1[1] for i_1 in upper_left_line], z=[i_1[2] for i_1 in upper_left_line],
#                                 mode='lines', line=dict(color='red', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
#
# for i_10, i_11, i_12 in zip(x_1, y_1, z_1):
#     if i_10 == 0:
#         if 19.5**2 <= abs((i_11+56.569)**2+(i_12-56.569)**2) <= 20.5**2:
#             outer_line_left_1.append([i_10, i_11, i_12])
#         else:
#             inner_line_left_1.append([i_10, i_11, i_12])
#     elif -11.8 <= i_11/i_10 <= -10.4:
#         if 19.5**2 <= abs((i_11+56.569)**2+(i_12-56.569)**2) <= 20.5**2:
#             outer_line_right_1.append([i_10, i_11, i_12])
#         else:
#             inner_line_right_1.append([i_10, i_11, i_12])
#
# inner_line_left_1_lower_inner = []
# inner_line_left_1_lower_outer = []
# inner_line_left_1_upper_inner = []
# inner_line_left_1_upper_outer = []
# inner_line_left_1_upper_outer_upper = []
# inner_line_left_1_upper_outer_lower = []
#
# outer_line_left_1_lower_inner = []
# outer_line_left_1_lower_outer = []
# outer_line_left_1_upper_inner = []
# outer_line_left_1_upper_outer = []
# outer_line_left_1_upper_outer_upper = []
# outer_line_left_1_upper_outer_lower = []
#
# inner_line_right_1_lower_inner = []
# inner_line_right_1_lower_outer = []
# inner_line_right_1_upper_inner = []
# inner_line_right_1_upper_outer = []
# inner_line_right_1_upper_outer_upper = []
# inner_line_right_1_upper_outer_lower = []
#
# outer_line_right_1_lower_inner = []
# outer_line_right_1_lower_outer = []
# outer_line_right_1_upper_inner = []
# outer_line_right_1_upper_outer = []
# outer_line_right_1_upper_outer_upper = []
# outer_line_right_1_upper_outer_lower = []
#
# for i_13, i_14, i_15 in inner_line_left_1:
#     if i_14 + 56.569 <= 0:
#         if i_15 - 56.569 >= 0:
#             if i_15 >= 66:
#                 inner_line_left_1_upper_outer_upper.append([i_13, i_14, i_15])
#             else:
#                 inner_line_left_1_upper_outer_lower.append([i_13, i_14, i_15])
#         else:
#             inner_line_left_1_lower_outer.append([i_13, i_14, i_15])
#
#     else:
#         if i_15 - 56.569 >= 0:
#             inner_line_left_1_upper_inner.append([i_13, i_14, i_15])
#         else:
#             inner_line_left_1_lower_inner.append([i_13, i_14, i_15])
#
# for i_13, i_14, i_15 in outer_line_left_1:
#     if i_14 + 56.569 <= 0:
#         if i_15 - 56.569 >= 0:
#             if i_15 >= 66:
#                 outer_line_left_1_upper_outer_upper.append([i_13, i_14, i_15])
#             else:
#                 outer_line_left_1_upper_outer_lower.append([i_13, i_14, i_15])
#         else:
#             outer_line_left_1_lower_outer.append([i_13, i_14, i_15])
#
#     else:
#         if i_15 - 56.569 >= 0:
#             outer_line_left_1_upper_inner.append([i_13, i_14, i_15])
#         else:
#             outer_line_left_1_lower_inner.append([i_13, i_14, i_15])
#
# for i_13, i_14, i_15 in inner_line_right_1:
#     if i_14 + 56.32 <= 0:
#         if i_15 - 56.32 >= 0:
#             if i_15 >= 66:
#                 inner_line_right_1_upper_outer_upper.append([i_13, i_14, i_15])
#             else:
#                 inner_line_right_1_upper_outer_lower.append([i_13, i_14, i_15])
#         else:
#             inner_line_right_1_lower_outer.append([i_13, i_14, i_15])
#
#     else:
#         if i_15 - 56.32 >= 0:
#             inner_line_right_1_upper_inner.append([i_13, i_14, i_15])
#         else:
#             inner_line_right_1_lower_inner.append([i_13, i_14, i_15])
#
# for i_13, i_14, i_15 in outer_line_right_1:
#     if i_14 + 56.32 <= 0:
#         if i_15 - 56.32 >= 0:
#             if i_15 >= 66:
#                 outer_line_right_1_upper_outer_upper.append([i_13, i_14, i_15])
#             else:
#                 outer_line_right_1_upper_outer_lower.append([i_13, i_14, i_15])
#         else:
#             outer_line_right_1_lower_outer.append([i_13, i_14, i_15])
#
#     else:
#         if i_15 - 56.32 >= 0:
#             outer_line_right_1_upper_inner.append([i_13, i_14, i_15])
#         else:
#             outer_line_right_1_lower_inner.append([i_13, i_14, i_15])
#
# inner_left_circle = (list(reversed(inner_line_left_1_upper_outer_lower)) + inner_line_left_1_lower_outer + inner_line_left_1_lower_inner
#                      + list(reversed(inner_line_left_1_upper_inner)) + list(reversed(inner_line_left_1_upper_outer_upper))
#                      )
# outer_left_circle = (list(reversed(outer_line_left_1_upper_outer_lower)) + outer_line_left_1_lower_outer + outer_line_left_1_lower_inner
#                         + list(reversed(outer_line_left_1_upper_inner)) + list(reversed(outer_line_left_1_upper_outer_upper))
#                         )
# inner_right_circle = (inner_line_right_1_upper_outer_lower + list(reversed(inner_line_right_1_lower_outer)) + list(reversed(inner_line_right_1_lower_inner))
#                         + inner_line_right_1_upper_inner + inner_line_right_1_upper_outer_upper
#                         )
# outer_right_circle = (outer_line_right_1_upper_outer_lower + list(reversed(outer_line_right_1_lower_outer)) + list(reversed(outer_line_right_1_lower_inner))
#                         + outer_line_right_1_upper_inner + outer_line_right_1_upper_outer_upper
#                         )
# connection_line_left_upper = [inner_left_circle[-1]] + [outer_left_circle[-1]]
# connection_line_left_lower = [inner_left_circle[0]] + [outer_left_circle[0]]
# connection_line_right_upper = [inner_right_circle[-1]] + [outer_right_circle[-1]]
# connection_line_right_lower = [inner_right_circle[0]] + [outer_right_circle[0]]
# connection_line_outer_lower = [outer_left_circle[0]] + [outer_right_circle[0]]
# connection_line_outer_upper = [outer_left_circle[-1]] + [outer_right_circle[-1]]
# connection_line_inner_lower = [inner_left_circle[0]] + [inner_right_circle[0]]
# connection_line_inner_upper = [inner_left_circle[-1]] + [inner_right_circle[-1]]
#
# points_for_line_to_center_upper_left = [connection_line_left_upper[0]]+[[0, 0, 0]]
# points_for_line_to_center_upper_right = [connection_line_right_upper[0]]+[[0, 0, 0]]
# points_for_line_to_center_lower_left = [connection_line_left_lower[0]]+[[0, -56.569, 56.569]]
# points_for_line_to_center_lower_right = [connection_line_right_lower[0]]+[[4.93, -56.353, 56.569]]
#
# line_for_outer_circle_in_z = np.sin(np.pi*np.linspace(45,135, 180)/180)*100
# line_for_outer_circle_in_y = -np.cos(np.pi*np.linspace(45,135, 180)/180)*100
# line_for_inner_circle_in_z = np.sin(np.pi*np.linspace(45,135, 180)/180)*98.5
# line_for_inner_circle_in_y = -np.cos(np.pi*np.linspace(45,135, 180)/180)*98.5
# points_for_outer_circle = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 180), line_for_outer_circle_in_y, line_for_outer_circle_in_z)]
# points_for_inner_circle = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 180), line_for_inner_circle_in_y, line_for_inner_circle_in_z)]
#
# line_for_partial_outer_torus_right_shell_in_z = np.sin(np.pi*np.linspace(0,45, 90)/180)*20 + 56.569
# line_for_partial_outer_torus_right_shell_in_y = -np.cos(np.pi*np.linspace(0,45, 90)/180)*20 - 56.569
# line_for_partial_inner_torus_right_shell_in_z = np.sin(np.pi*np.linspace(0,45, 90)/180)*18.5 + 56.569
# line_for_partial_inner_torus_right_shell_in_y = -np.cos(np.pi*np.linspace(0,45, 90)/180)*18.5 - 56.569
# points_for_partial_outer_torus_right_shell = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 90), line_for_partial_outer_torus_right_shell_in_y, line_for_partial_outer_torus_right_shell_in_z)]
# points_for_partial_inner_torus_right_shell = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 90), line_for_partial_inner_torus_right_shell_in_y, line_for_partial_inner_torus_right_shell_in_z)]
#
# line_for_partial_outer_torus_left_shell_in_z = np.sin(np.pi*np.linspace(135,180, 90)/180)*20 + 56.569
# line_for_partial_outer_torus_left_shell_in_y = -np.cos(np.pi*np.linspace(135,180, 90)/180)*20 + 56.569
# line_for_partial_inner_torus_left_shell_in_z = np.sin(np.pi*np.linspace(135,180, 90)/180)*18.5 + 56.569
# line_for_partial_inner_torus_left_shell_in_y = -np.cos(np.pi*np.linspace(135,180, 90)/180)*18.5 + 56.569
# points_for_partial_outer_torus_left_shell = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 90), line_for_partial_outer_torus_left_shell_in_y, line_for_partial_outer_torus_left_shell_in_z)]
# points_for_partial_inner_torus_left_shell = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 90), line_for_partial_inner_torus_left_shell_in_y, line_for_partial_inner_torus_left_shell_in_z)]
#
# points_for_inner_shell_right = [[0, -75.069, 56.569], [0, -75.069, 0]]
# points_for_outer_shell_right = [[0, -76.569, 56.569], [0, -76.569, 0]]
# points_for_inner_shell_left = [[0, +75.069, 56.569], [0, +75.069, 0]]
# points_for_outer_shell_left = [[0, +76.569, 56.569], [0, +76.569, 0]]
#
# full_torus_right_line_outer_z = np.sin(np.pi*np.linspace(0,360, 360)/180)*20 + 56.569
# full_torus_right_line_outer_y = -np.cos(np.pi*np.linspace(0,360, 360)/180)*20 - 56.569
# full_torus_right_line_inner_z = np.sin(np.pi*np.linspace(0,360, 360)/180)*18.5 + 56.569
# full_torus_right_line_inner_y = -np.cos(np.pi*np.linspace(0,360, 360)/180)*18.5 - 56.569
# points_full_torus_right_line_outer = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 360), full_torus_right_line_outer_y, full_torus_right_line_outer_z)]
# points_full_torus_right_line_inner = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 360), full_torus_right_line_inner_y, full_torus_right_line_inner_z)]
# full_torus_left_line_outer_z = np.sin(np.pi*np.linspace(0,360, 360)/180)*20 + 56.569
# full_torus_left_line_outer_y = -np.cos(np.pi*np.linspace(0,360, 360)/180)*20 + 56.569
# full_torus_left_line_inner_z = np.sin(np.pi*np.linspace(0,360, 360)/180)*18.5 + 56.569
# full_torus_left_line_inner_y = -np.cos(np.pi*np.linspace(0,360, 360)/180)*18.5 + 56.569
# points_full_torus_left_line_outer = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 360), full_torus_left_line_outer_y, full_torus_left_line_outer_z)]
# points_full_torus_left_line_inner = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 360), full_torus_left_line_inner_y, full_torus_left_line_inner_z)]
#
# # line_for_torus_upper = [[0, -56.569, 56.569], [0, -56.569, 0]]
# # line_for_torus_lower = [[0, -56.569, 56.569], [0, -56.569, 0]]
#
# mesh3D_outer_line_left_1 = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_left_1], y=[i_1[1] for i_1 in outer_line_left_1], z=[i_1[2] for i_1 in outer_line_left_1],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_inner_line_left_1 = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_left_1], y=[i_1[1] for i_1 in inner_line_left_1], z=[i_1[2] for i_1 in inner_line_left_1],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_line_right_1 = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_right_1], y=[i_1[1] for i_1 in outer_line_right_1], z=[i_1[2] for i_1 in outer_line_right_1],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_inner_line_right_1 = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_right_1], y=[i_1[1] for i_1 in inner_line_right_1], z=[i_1[2] for i_1 in inner_line_right_1],
#                                 mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
#
# mesh3D_inner_left_circle = go.Scatter3d(x=[i_1[0] for i_1 in inner_left_circle], y=[i_1[1] for i_1 in inner_left_circle], z=[i_1[2] for i_1 in inner_left_circle],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_left_circle = go.Scatter3d(x=[i_1[0] for i_1 in outer_left_circle], y=[i_1[1] for i_1 in outer_left_circle], z=[i_1[2] for i_1 in outer_left_circle],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_inner_right_circle = go.Scatter3d(x=[i_1[0] for i_1 in inner_right_circle], y=[i_1[1] for i_1 in inner_right_circle], z=[i_1[2] for i_1 in inner_right_circle],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_right_circle = go.Scatter3d(x=[i_1[0] for i_1 in outer_right_circle], y=[i_1[1] for i_1 in outer_right_circle], z=[i_1[2] for i_1 in outer_right_circle],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_connection_line_right_upper = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_right_upper], y=[i_1[1] for i_1 in connection_line_right_upper], z=[i_1[2] for i_1 in connection_line_right_upper],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_connection_line_right_lower = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_right_lower], y=[i_1[1] for i_1 in connection_line_right_lower], z=[i_1[2] for i_1 in connection_line_right_lower],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_connection_line_left_upper = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_left_upper], y=[i_1[1] for i_1 in connection_line_left_upper], z=[i_1[2] for i_1 in connection_line_left_upper],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_connection_line_left_lower = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_left_lower], y=[i_1[1] for i_1 in connection_line_left_lower], z=[i_1[2] for i_1 in connection_line_left_lower],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_connection_line_outer_upper = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_outer_upper], y=[i_1[1] for i_1 in connection_line_outer_upper], z=[i_1[2] for i_1 in connection_line_outer_upper],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_connection_line_outer_lower = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_outer_lower], y=[i_1[1] for i_1 in connection_line_outer_lower], z=[i_1[2] for i_1 in connection_line_outer_lower],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_connection_line_inner_upper = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_inner_upper], y=[i_1[1] for i_1 in connection_line_inner_upper], z=[i_1[2] for i_1 in connection_line_inner_upper],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_connection_line_inner_lower = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_inner_lower], y=[i_1[1] for i_1 in connection_line_inner_lower], z=[i_1[2] for i_1 in connection_line_inner_lower],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_line_to_center_upper_left = go.Scatter3d(x=[i_1[0] for i_1 in points_for_line_to_center_upper_left], y=[i_1[1] for i_1 in points_for_line_to_center_upper_left], z=[i_1[2] for i_1 in points_for_line_to_center_upper_left],
#                                 mode='lines', line=dict(color='red', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_line_to_center_upper_right = go.Scatter3d(x=[i_1[0] for i_1 in points_for_line_to_center_upper_right], y=[i_1[1] for i_1 in points_for_line_to_center_upper_right], z=[i_1[2] for i_1 in points_for_line_to_center_upper_right],
#                                 mode='lines', line=dict(color='red', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_line_to_center_lower_left = go.Scatter3d(x=[i_1[0] for i_1 in points_for_line_to_center_lower_left], y=[i_1[1] for i_1 in points_for_line_to_center_lower_left], z=[i_1[2] for i_1 in points_for_line_to_center_lower_left],
#                                 mode='lines', line=dict(color='red', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_line_to_center_lower_right = go.Scatter3d(x=[i_1[0] for i_1 in points_for_line_to_center_lower_right], y=[i_1[1] for i_1 in points_for_line_to_center_lower_right], z=[i_1[2] for i_1 in points_for_line_to_center_lower_right],
#                                 mode='lines', line=dict(color='red', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_inner_circle = go.Scatter3d(x=[i_1[0] for i_1 in points_for_inner_circle], y=[i_1[1] for i_1 in points_for_inner_circle], z=[i_1[2] for i_1 in points_for_inner_circle],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_circle = go.Scatter3d(x=[i_1[0] for i_1 in points_for_outer_circle], y=[i_1[1] for i_1 in points_for_outer_circle], z=[i_1[2] for i_1 in points_for_outer_circle],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_outer_shell_right = go.Scatter3d(x=[i_1[0] for i_1 in points_for_outer_shell_right], y=[i_1[1] for i_1 in points_for_outer_shell_right], z=[i_1[2] for i_1 in points_for_outer_shell_right],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_inner_shell_right = go.Scatter3d(x=[i_1[0] for i_1 in points_for_inner_shell_right], y=[i_1[1] for i_1 in points_for_inner_shell_right], z=[i_1[2] for i_1 in points_for_inner_shell_right],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_outer_shell_left = go.Scatter3d(x=[i_1[0] for i_1 in points_for_outer_shell_left], y=[i_1[1] for i_1 in points_for_outer_shell_left], z=[i_1[2] for i_1 in points_for_outer_shell_left],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3d_inner_shell_left = go.Scatter3d(x=[i_1[0] for i_1 in points_for_inner_shell_left], y=[i_1[1] for i_1 in points_for_inner_shell_left], z=[i_1[2] for i_1 in points_for_inner_shell_left],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_inner_left_torus = go.Scatter3d(x=[i_1[0] for i_1 in points_for_partial_inner_torus_right_shell], y=[i_1[1] for i_1 in points_for_partial_inner_torus_right_shell], z=[i_1[2] for i_1 in points_for_partial_inner_torus_right_shell],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_left_torus = go.Scatter3d(x=[i_1[0] for i_1 in points_for_partial_outer_torus_right_shell], y=[i_1[1] for i_1 in points_for_partial_outer_torus_right_shell], z=[i_1[2] for i_1 in points_for_partial_outer_torus_right_shell],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_inner_right_torus = go.Scatter3d(x=[i_1[0] for i_1 in points_for_partial_inner_torus_left_shell], y=[i_1[1] for i_1 in points_for_partial_inner_torus_left_shell], z=[i_1[2] for i_1 in points_for_partial_inner_torus_left_shell],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_outer_right_torus = go.Scatter3d(x=[i_1[0] for i_1 in points_for_partial_outer_torus_left_shell], y=[i_1[1] for i_1 in points_for_partial_outer_torus_left_shell], z=[i_1[2] for i_1 in points_for_partial_outer_torus_left_shell],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_full_torus_right_line_outer = go.Scatter3d(x=[i_1[0] for i_1 in points_full_torus_right_line_outer], y=[i_1[1] for i_1 in points_full_torus_right_line_outer], z=[i_1[2] for i_1 in points_full_torus_right_line_outer],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_full_torus_right_line_inner = go.Scatter3d(x=[i_1[0] for i_1 in points_full_torus_right_line_inner], y=[i_1[1] for i_1 in points_full_torus_right_line_inner], z=[i_1[2] for i_1 in points_full_torus_right_line_inner],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_full_torus_left_line_outer = go.Scatter3d(x=[i_1[0] for i_1 in points_full_torus_left_line_outer], y=[i_1[1] for i_1 in points_full_torus_left_line_outer], z=[i_1[2] for i_1 in points_full_torus_left_line_outer],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
# mesh3D_full_torus_left_line_inner = go.Scatter3d(x=[i_1[0] for i_1 in points_full_torus_left_line_inner], y=[i_1[1] for i_1 in points_full_torus_left_line_inner], z=[i_1[2] for i_1 in points_full_torus_left_line_inner],
#                                 mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
#
#
# mesh_curved_arrow_1 = mesh.Mesh.from_file('./meshes/Hohl_Torus.stl')
# vertices_2, I_2, J_2, K_2 = bf.stl2mesh3d(mesh_curved_arrow_1)
# x_2, y_2, z_2 = vertices_2.T
# mesh3D_base_body_3 = go.Mesh3d(x=x_2, y=y_2, z=z_2, i=I_2, j=J_2, k=K_2,
#                                  color='lightgray', opacity=0.20, showscale=False, visible=True,
#                                     contour=dict(show=True, width=16))
#
# mesh_tankshell = mesh.Mesh.from_file('./meshes/Halber_Boden.stl')
# vertices_3, I_3, J_3, K_3 = bf.stl2mesh3d(mesh_tankshell)
# x_3, y_3, z_3 = vertices_3.T
# mesh3D_base_body_4 = go.Mesh3d(x=x_3, y=y_3, z=z_3, i=I_3, j=J_3, k=K_3,
#                                  color='lightgray', opacity=0.20, showscale=False, visible=True,
#                                     contour=dict(show=True, width=16))
# mesh_torus_halfcircle = mesh.Mesh.from_file('./meshes/Halber_Torus.stl')
# vertices_4, I_4, J_4, K_4 = bf.stl2mesh3d(mesh_torus_halfcircle)
# x_4, y_4, z_4 = vertices_4.T
# mesh3D_base_body_5 = go.Mesh3d(x=x_4, y=y_4, z=z_4, i=I_4, j=J_4, k=K_4,
#                                  color='lightgray', opacity=0.20, showscale=False, visible=True,
#                                     contour=dict(show=True, width=16))
fig_2 = go.Figure(data=mesh3D_Differential_element_1)
fig_2.show()
# fig_2 = go.Figure(data=[
#                         # mesh3D_base_body_3, mesh3D_base_body_2, mesh3D_base_body_1,
#                         # mesh3D_inner_line_left,
#                         # mesh3D_outer_line_left, mesh3D_inner_line_right,
#                         # mesh3D_outer_line_right, mesh3D_inner_line_upper, mesh3D_inner_line_lower,
#                         # mesh3D_outer_line_upper, mesh3D_outer_line_lower, mesh3D_upper_left_line,
#                         # mesh3D_upper_right_line, mesh3D_lower_left_line, mesh3D_lower_right_line,
#                         # mesh3D_inner_left_circle, mesh3D_outer_left_circle,
#                         # mesh3D_inner_right_circle, mesh3D_outer_right_circle,
#                         # mesh3d_connection_line_right_upper, mesh3d_connection_line_right_lower,
#                         # mesh3d_connection_line_left_upper, mesh3d_connection_line_left_lower,
#                         # mesh3d_connection_line_outer_upper, mesh3d_connection_line_outer_lower,
#                         # mesh3d_connection_line_inner_upper, mesh3d_connection_line_inner_lower,
#                         mesh3d_line_to_center_upper_left, mesh3d_line_to_center_upper_right,
#                         mesh3d_line_to_center_lower_left, mesh3d_line_to_center_lower_right,
#                         mesh3D_inner_circle, mesh3D_outer_circle,
#                         mesh3d_outer_shell_right, mesh3d_inner_shell_right,
#                         mesh3d_outer_shell_left, mesh3d_inner_shell_left,
#                         mesh3D_inner_left_torus, mesh3D_outer_left_torus,
#                         mesh3D_inner_right_torus, mesh3D_outer_right_torus,
#                         mesh3D_base_body_4, mesh3D_base_body_5,
#                         mesh3D_full_torus_right_line_outer, mesh3D_full_torus_right_line_inner,
#                         mesh3D_full_torus_left_line_outer, mesh3D_full_torus_left_line_inner,
#                         ])
# fig_2.show()

# mesh_curved_arrow_1 = mesh.Mesh.from_file('./meshes/Hohl_Torus.stl')
# mesh3D_Arrow_1 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, -25, 0], -np.pi/2, 0, 0, '<i>F<sub>rz </sub> r d&#966; </i>')
# mesh3D_Arrow_2 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 0, 0], np.pi/2, 0, 0, '<i>p( r ) &#8729; rd&#966; &#8729; dr d&#966; </i>')
# mesh3D_Arrow_3 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 25, 0], np.pi/2, 0, 0, '<i>F<sub>rz </sub> rd&#966; + d &#8260; dr (F<sub>rz </sub> r) dr d&#966; </i>')

# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_1) # F_r r d phi
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_2) # q r e dr r d phi
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_3) # (F_r + dF_r) (r + dr) d phi
#
# mesh3D_Curved_Arrow_1 = fm.create_mesh3d_for_curved_arrow(mesh_curved_arrow_1, 0.5, [0, -50, 0], 0, 0, 0, '<i>M<sub>r </sub>&#8729;r dr</i>')
# mesh3D_Curved_Arrow_2 = fm.create_mesh3d_for_curved_arrow(mesh_curved_arrow_1, 0.5, [0, 50, 0], 0, 0, np.pi, '<i>M<sub>r </sub>&#8729;r d&#966; + d &#8260; dr(M<sub>r </sub>&#8729;r) dr d&#966;</i>')
#
# mesh3D_Curved_Arrow_3 = fm.create_mesh3d_for_curved_arrow(mesh_curved_arrow_1, 0.5, [-50, -10, 0], 0, 0, -np.pi/360*150, '<i>M<sub>&#966; </sub>dr</i>')
# mesh3D_Curved_Arrow_4 = fm.create_mesh3d_for_curved_arrow(mesh_curved_arrow_1, 0.48296291314453416, [-50, -8.3, 0], 0, 0, -np.pi/360*180, '<i>M<sub>&#966; </sub>dr cos(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr </i>', bodycolor='lightblue')
# mesh3D_Curved_Arrow_5 = fm.create_mesh3d_for_curved_arrow(mesh_curved_arrow_1, 0.12940952255126037, [-68.69805, -10, 0], 0, 0, 0, '<i>M<sub>&#966; </sub>dr sin(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr d&#966; &#8260; 2</i>', bodycolor='lightgreen')
#
# mesh3D_Curved_Arrow_6 = fm.create_mesh3d_for_curved_arrow(mesh_curved_arrow_1, 0.5, [50, -10, 0], 0, 0, np.pi/360*150, '<i>M<sub>&#966; </sub>dr</i>')
# mesh3D_Curved_Arrow_7 = fm.create_mesh3d_for_curved_arrow(mesh_curved_arrow_1, 0.48296291314453416, [50, -8.3, 0], 0, 0, np.pi/360*180, '<i>M<sub>&#966; </sub>dr cos(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr </i>', bodycolor='lightblue')
# mesh3D_Curved_Arrow_8 = fm.create_mesh3d_for_curved_arrow(mesh_curved_arrow_1, 0.12940952255126037, [68.69805, -10, 0], 0, 0, 0, '<i>M<sub>&#966; </sub>dr sin(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr d&#966; &#8260; 2</i>', bodycolor='lightgreen')
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Curved_Arrow_1)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Curved_Arrow_2)
#
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Curved_Arrow_3)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Curved_Arrow_4)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Curved_Arrow_5)
#
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Curved_Arrow_6)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Curved_Arrow_7)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Curved_Arrow_8)



# fig = go.Figure(data=mesh3D_Differential_element_1)
#
#
#
# force_annotations_all = [
#                     # Kräfte in Z Richtung
#                          dict(x=0, y=-25, z=9, text='<i>F<sub>rz </sub> r d&#966; </i>', textangle=0, ax=50, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x=0, y=0, z=6.5, text='<i>p( r ) &#8729; rd&#966; &#8729; dr d&#966; </i>', textangle=0, ax=0, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x=0, y=25, z=6.5, text='<i>F<sub>rz </sub> rd&#966; + d &#8260; dr (F<sub>rz </sub> r) dr d&#966; </i>', textangle=0, ax=-50, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                     # Momente für Gesamtmoment
#                          dict(x=-50, y=-10, z=22.64711, text='<i>M<sub>&#966; </sub>dr</i>', textangle=0, ax=50, ay=-60, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x= 50, y=-10, z=22.64711, text='<i>M<sub>&#966; </sub>dr</i>', textangle=0, ax=50, ay=-60, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                     # Momente Radial
#                          dict(x=-50, y=-8.3, z=21.87543, text='<i>M<sub>&#966; </sub>dr cos(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr </i>', textangle=0, ax=-50, ay=-50, font=dict(color="blue", size=12),
#                               arrowcolor="blue", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x= 50, y=-8.3, z=21.87543, text='<i>M<sub>&#966; </sub>dr cos(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr </i>', textangle=0, ax=-50, ay=-50, font=dict(color="blue", size=12),
#                               arrowcolor="blue", arrowsize=3, arrowwidth=1, arrowhead=0),
#                     # Momente Tangential
#                          dict(x=0, y=-50, z=22.64711, text='<i>M<sub>r </sub>&#8729;r dr</i>', textangle=0, ax=0, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x=0, y=50, z=22.64711, text='<i>M<sub>r </sub>&#8729;r d&#966; + d &#8260; dr(M<sub>r </sub>&#8729;r) dr d&#966;</i>', textangle=0, ax=0, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#
#                          dict(x=-68.69805, y=-10, z=5.861504, text='<i>M<sub>&#966; </sub>dr sin(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr d&#966; &#8260; 2</i>', textangle=0, ax=-70, ay=-20, font=dict(color="green", size=12),
#                               arrowcolor="green", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x= 68.69805, y=-10, z=5.861504, text='<i>M<sub>&#966; </sub>dr sin(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr d&#966; &#8260; 2</i>', textangle=0, ax= 70, ay=-20, font=dict(color="green", size=12),
#                               arrowcolor="green", arrowsize=3, arrowwidth=1, arrowhead=0)]
# force_annotations_z = [
#                     # Kräfte in Z Richtung
#                          dict(x=0, y=-25, z=9, text='<i>F<sub>rz </sub> r d&#966; </i>', textangle=0, ax=50, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x=0, y=0, z=6.5, text='<i>p( r ) &#8729; rd&#966; &#8729; dr d&#966; </i>', textangle=0, ax=0, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x=0, y=25, z=6.5, text='<i>F<sub>rz </sub> rd&#966; + d &#8260; dr (F<sub>rz </sub> r) dr d&#966; </i>', textangle=0, ax=-50, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),]
#
# moments_annotations_radial = [
#                     # Momente Radial
#                          dict(x=-50, y=-8.3, z=21.87543, text='<i>M<sub>&#966; </sub>dr cos(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr </i>', textangle=0, ax=-50, ay=-50, font=dict(color="blue", size=12),
#                               arrowcolor="blue", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x= 50, y=-8.3, z=21.87543, text='<i>M<sub>&#966; </sub>dr cos(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr </i>', textangle=0, ax=-50, ay=-50, font=dict(color="blue", size=12),
#                               arrowcolor="blue", arrowsize=3, arrowwidth=1, arrowhead=0),]
# moments_annotations_tangential = [
#                     # Momente Tangential
#                          dict(x=0, y=-50, z=22.64711, text='<i>M<sub>r </sub>&#8729;r dr</i>', textangle=0, ax=0, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x=0, y=50, z=22.64711, text='<i>M<sub>r </sub>&#8729;r d&#966; + d &#8260; dr(M<sub>r </sub>&#8729;r) dr d&#966;</i>', textangle=0, ax=0, ay=-50, font=dict(color="black", size=12),
#                               arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#
#                          dict(x=-68.69805, y=-10, z=5.861504, text='<i>M<sub>&#966; </sub>dr sin(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr d&#966; &#8260; 2</i>', textangle=0, ax=-70, ay=-20, font=dict(color="green", size=12),
#                               arrowcolor="green", arrowsize=3, arrowwidth=1, arrowhead=0),
#                          dict(x= 68.69805, y=-10, z=5.861504, text='<i>M<sub>&#966; </sub>dr sin(d&#966; &#8260; Z) &#8776; M<sub>&#966; </sub>dr d&#966; &#8260; 2</i>', textangle=0, ax= 70, ay=-20, font=dict(color="green", size=12),
#                               arrowcolor="green", arrowsize=3, arrowwidth=1, arrowhead=0)]
#
# geometry_annotations = [dict(  # upper front curve
#                             x=0, y=-25, z=25, text=r'$r* d\phi$', textangle=0, ax=-50, ay=-50, font=dict(color="black", size=12), arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                         dict(  # right front curve
#                             x=-25.8819, y=-28.40742, z=0, text=r'$2* \frac{e}{2}$', textangle=0, ax=50, ay=-50, font=dict(color="black", size=12), arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                         dict(  # right upper curve
#                             x=-32.35238, y=-4.259264999999999, z=25, text=r'$dr$', textangle=0,ax=50, ay=-50, font=dict(color="black", size=12), arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
#                         dict(  # right back curve
#                             x=0, y=25, z=25, text=r'$(r + dr)* d\phi$', textangle=0, ax=50, ay=-50, font=dict(color="black", size=12), arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0)]
#
#
# fig.update_layout(
#     showlegend=False,
#     updatemenus=[
#         dict(
#             active=0,
#             # type="buttons",
#             buttons=list([
#                   dict(label="Alle Kräfte", method="update", args=[{"visible": [True]*134}, {"scene.annotations": []},]),
#                   dict(label="Kräfte in \"Z\" Richtung", method="update", args=[{"visible": [True]*46+[False]*88}, {"scene.annotations": []}]),
#                   dict(label="Momente Radial", method="update", args=[{"visible": [True] * 13 + [False] * 66 + [True] * 11 + [False] * 22 + [True] * 11 + [False] * 11}, {"scene.annotations": []}]),
#                   dict(label="Momente Tangential", method="update", args=[{"visible": [True] * 13 + [False] * 33 + [True] * 22 + [False] * 22 + [True] * 11 + [False] * 22 +[True]*11}, {"scene.annotations": []}]),
#               ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.0, xanchor="left",  y=1.115, yanchor="top", font=dict(size=10)
#         ),
#         dict( active=0,
#               buttons=list([
#                   dict(label="Alle Kräfte", method="update", args=[{"visible": [True]*134}, {"scene.annotations": force_annotations_all},]),
#                   dict(label="Kräfte in \"Z\" Richtung", method="update", args=[{"visible": [True]*46+[False]*88}, {"scene.annotations": force_annotations_z}]),
#                   dict(label="Momente Radial", method="update", args=[
#                       {"visible": [True] * 13 + [False] * 66 + [True] * 11 + [False] * 22 + [True] * 11 + [False] * 11}, {"scene.annotations": moments_annotations_radial}]),
#                   dict(label="Momente Tangential", method="update", args=[
#                       {"visible": [True] * 13 + [False] * 33 + [True] * 22 + [False] * 22 + [True] * 11 + [False] * 22 +[True]*11}, {"scene.annotations": moments_annotations_tangential}]),
#               ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.0, xanchor="left", y=1.02, yanchor="top", font=dict(size=10)
#         ),
#         dict( active=0,
#               buttons=list([
#                   dict(label="Ausblenden", method="relayout", args=[{"scene.annotations": []},]),
#                   dict(label="Einblenden", method="relayout", args=[{"scene.annotations": geometry_annotations}])
#               ]), direction="down", showactive=False, pad={"r": 0, "t": 0}, x=0.55, xanchor="left", y=1.22, yanchor="top", font=dict(size=10)
#         ),
#         dict(
#             active=0,
#             buttons=list([
#                 dict(label="Reset", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.25, y=-1.25, z=1.25))}]),
#                 dict(label="links", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=0))}]),
#                 dict(label="links erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=1.7))}]),
#                 dict(label="rechts", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=0))}]),
#                 dict(label="rechts erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=1.5))}]),
#                 dict(label="Vogelperspektive", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=0, z=2.2), up=dict(x=0, y=-1, z=0),)}]),
#                 dict(label="Rückseitig", method="relayout",  args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=0))}]),
#                 dict(label="Rückseitig erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=1.7))}]),
#                 dict(label="Frontal", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=0))}]),
#                 dict(label="Frontal erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=1.7))}]),
#             ]),
#             direction="down", pad={"r": 0, "t": 0}, showactive=True, x=-0.05, xanchor="left", y=1.22, yanchor="top", font=dict(size=10)
#         )
#     ],
#     scene=dict(
#         xaxis=dict(nticks=20, range=[-75, 75], autorange=False), yaxis=dict(nticks=20, range=[-75, 75], autorange=False), zaxis=dict(nticks=15, range=[-50, 50], autorange=False),
#         aspectmode='manual', xaxis_title='Y Achse', yaxis_title='X Achse', zaxis_title='Z Achse', aspectratio=dict(x=1, y=1, z=0.8),
#         ),
#     scene_camera=dict(eye=dict(x=-1.25, y=-1.25, z=1.25)),
#     annotations=[
#         dict(text="Kräfte ohne                                                                                                                                            "
#                   "<br>Beschriftung                                                                                                                                           "
#                   "<br> "
#                   "<br>Kräfte mit                                                                                                                                             "
#                   "<br>Beschriftung                                                                                                                                           "
#                   "<br>", x=-0.18, y=1.11, showarrow=False, font=dict(size=10)),
#         dict(text=""
#                   "<br>"
#                   "<br> "
#                   "<br> Kamera                         "
#                   "<br> "
#                   "<br> "
#                   "<br> ", x=-0.19, y=1.23, showarrow=False, font=dict(size=10)),
#         dict(text=""
#                   "<br>"
#                   "<br> "
#                   "<br> Geometrie                 "
#                   "<br> "
#                   "<br> "
#                   "<br> ", x=0.53, y=1.23, showarrow=False, font=dict(size=10)),
#
#     ],
#     width=600,
#     height=600,
#     minreducedwidth=550,
#     minreducedheight=400,
#     autosize=False,
#     # paper_bgcolor='white',
# )
#
#
#
# fig.show()
# fig.write_html("./Kreisplatte_mit_Kraftzerlegung_und_Dropdown_fuer_Smartphones.html", include_plotlyjs='cdn', include_mathjax='cdn')
#
#
# fig.update_layout(
#     showlegend=False,
#     updatemenus=[
#         dict(
#             active=0,
#             # type="buttons",
#             buttons=list([
#                   dict(label="Alle Kräfte", method="update", args=[{"visible": [True]*134}, {"scene.annotations": []},]),
#                   dict(label="Kräfte in \"Z\" Richtung", method="update", args=[{"visible": [True]*46+[False]*88}, {"scene.annotations": []}]),
#                   dict(label="Momente Radial", method="update", args=[{"visible": [True] * 13 + [False] * 66 + [True] * 11 + [False] * 22 + [True] * 11 + [False] * 11}, {"scene.annotations": []}]),
#                   dict(label="Momente Tangential", method="update", args=[{"visible": [True] * 13 + [False] * 33 + [True] * 22 + [False] * 22 + [True] * 11 + [False] * 22 +[True]*11}, {"scene.annotations": []}]),
#               ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.33, xanchor="left",  y=1.115, yanchor="top", font=dict(size=10)
#         ),
#         dict( active=0,
#               buttons=list([
#                   dict(label="Alle Kräfte", method="update", args=[{"visible": [True]*134}, {"scene.annotations": force_annotations_all},]),
#                   dict(label="Kräfte in \"Z\" Richtung", method="update", args=[{"visible": [True]*46+[False]*88}, {"scene.annotations": force_annotations_z}]),
#                   dict(label="Momente Radial", method="update", args=[
#                       {"visible": [True] * 13 + [False] * 66 + [True] * 11 + [False] * 22 + [True] * 11 + [False] * 11}, {"scene.annotations": moments_annotations_radial}]),
#                   dict(label="Momente Tangential", method="update", args=[
#                       {"visible": [True] * 13 + [False] * 33 + [True] * 22 + [False] * 22 + [True] * 11 + [False] * 22 +[True]*11}, {"scene.annotations": moments_annotations_tangential}]),
#               ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.33, xanchor="left", y=1.055, yanchor="top", font=dict(size=10)
#         ),
#         dict( active=0,
#               buttons=list([
#                   dict(label="Ausblenden", method="relayout", args=[{"scene.annotations": []},]),
#                   dict(label="Einblenden", method="relayout", args=[{"scene.annotations": geometry_annotations}])
#               ]), direction="down", showactive=False, pad={"r": 0, "t": 0}, x=0.54, xanchor="left", y=1.22, yanchor="top", font=dict(size=10)
#         ),
#         dict(
#             active=0,
#             buttons=list([
#                 dict(label="Reset", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.25, y=-1.25, z=1.25))}]),
#                 dict(label="links", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=0))}]),
#                 dict(label="links erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=1.7))}]),
#                 dict(label="rechts", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=0))}]),
#                 dict(label="rechts erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=1.5))}]),
#                 dict(label="Vogelperspektive", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=0, z=2.2), up=dict(x=0, y=-1, z=0),)}]),
#                 dict(label="Rückseitig", method="relayout",  args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=0))}]),
#                 dict(label="Rückseitig erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=1.7))}]),
#                 dict(label="Frontal", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=0))}]),
#                 dict(label="Frontal erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=1.7))}]),
#             ]),
#             direction="down", pad={"r": 0, "t": 0}, showactive=True, x=0.33, xanchor="left", y=1.22, yanchor="top", font=dict(size=10)
#         )
#     ],
#     scene=dict(
#         xaxis=dict(nticks=20, range=[-75, 75], autorange=False), yaxis=dict(nticks=20, range=[-75, 75], autorange=False), zaxis=dict(nticks=15, range=[-50, 50], autorange=False),
#         aspectmode='manual', xaxis_title='Y Achse', yaxis_title='X Achse', zaxis_title='Z Achse', aspectratio=dict(x=1, y=1, z=0.8),
#         ),
#     scene_camera=dict(eye=dict(x=-1.25, y=-1.25, z=1.25)),
#     annotations=[
#         dict(text="Kräfte ohne                                                                                                                                            "
#                   "<br>Beschriftung                                                                                                                                           "
#                   "<br> "
#                   "<br>Kräfte mit                                                                                                                                             "
#                   "<br>Beschriftung                                                                                                                                           "
#                   "<br>", x=0.28, y=1.11, showarrow=False, font=dict(size=10)),
#         dict(text=""
#                   "<br>"
#                   "<br> "
#                   "<br> Kamera                         "
#                   "<br> "
#                   "<br> "
#                   "<br> ", x=0.28, y=1.23, showarrow=False, font=dict(size=10)),
#         dict(text=""
#                   "<br>"
#                   "<br> "
#                   "<br> Geometrie                 "
#                   "<br> "
#                   "<br> "
#                   "<br> ", x=0.53, y=1.23, showarrow=False, font=dict(size=10)),
#
#     ],
#     width=1800,
#     height=900,
#     minreducedwidth=550,
#     minreducedheight=600,
#     autosize=False,
#     # paper_bgcolor='white',
# )
#
#
#
# fig.show()
# fig.write_html("./Kreisplatte_mit_Kraftzerlegung_und_Dropdown_fuer_FullScreen.html", include_plotlyjs='cdn', include_mathjax='cdn')
