import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import numpy
from stl import mesh
import copy
import BasisFunktionen as bf

def create_mesh3d_for_torus_element(meshes, scalingfactor, pos_vec, zeta, eta, theta, hovertext_1,
                            ptly_linewidth=2, line_color='black', bodycolor='lightgray', font_size = 16):

    # rotational transformation
    alpha = 0
    beta = 0
    gamma = 0
    rotation_matrix = bf.combine_rotation_matrixes(alpha, beta, gamma)

    mesh_differential_element_1 = meshes[0]

    vertices, I, J, K = bf.stl2mesh3d(mesh_differential_element_1)
    x, y, z = vertices.T

    inner_line_left = []
    outer_line_left = []
    inner_line_right = []
    outer_line_right = []
    inner_line_upper = []
    inner_line_lower = []
    outer_line_upper = []
    outer_line_lower = []
    upper_left_line = []
    upper_right_line = []
    lower_left_line = []
    lower_right_line = []

    for i_1, i_2, i_3 in zip(x, y, z):
        if i_1 == 0:
            if 19.5 ** 2 <= abs((i_2 + 56.569) ** 2 + (i_3 - 56.569) ** 2) <= 20.5 ** 2:
                outer_line_left.append([i_1, i_2, i_3])
            else:
                inner_line_left.append([i_1, i_2, i_3])

        elif 6 <= i_1 <= 7:
            if 19.5 ** 2 <= abs((i_2 + 56.569) ** 2 + (i_3 - 56.569) ** 2) <= 20.5 ** 2:
                outer_line_right.append([i_1, i_2, i_3])
            else:
                inner_line_right.append([i_1, i_2, i_3])
        # elif max(inner_line_right[2, :]) <= i_2 <= max(inner_line_left[2, :]):
        #     inner_line_upper.append([i_1, i_2, i_3])
    for i_4, i_5, i_6 in zip(x, y, z):
        if max([i_9[1] for i_9 in inner_line_left]) <= i_5 <= max([i_8[1] for i_8 in inner_line_right]):
            inner_line_upper.append([i_4, i_5, i_6])
        elif min([i_9[2] for i_9 in inner_line_left]) <= i_6 <= min([i_8[2] for i_8 in inner_line_right]):
            inner_line_lower.append([i_4, i_5, i_6])
        elif max([i_9[2] for i_9 in outer_line_left]) <= i_6 <= max([i_8[2] for i_8 in outer_line_right]):
            outer_line_upper.append([i_4, i_5, i_6])
        elif min([i_9[1] for i_9 in outer_line_left]) <= i_5 <= min(
                [i_8[1] for i_8 in outer_line_right]) and i_6 <= 64.6:
            outer_line_lower.append([i_4, i_5, i_6])
        if max([i_9[1] for i_9 in inner_line_left]) == i_5 or max([i_9[1] for i_9 in outer_line_left]) == i_5:
            upper_left_line.append([i_4, i_5, i_6])
        elif max([i_9[1] for i_9 in inner_line_right]) == i_5 or max([i_9[1] for i_9 in outer_line_right]) == i_5:
            upper_right_line.append([i_4, i_5, i_6])
        elif min([i_9[1] for i_9 in inner_line_left]) == i_5 or min([i_9[1] for i_9 in outer_line_left]) == i_5:
            lower_left_line.append([i_4, i_5, i_6])
        elif min([i_9[1] for i_9 in inner_line_right]) == i_5 or min([i_9[1] for i_9 in outer_line_right]) == i_5:
            lower_right_line.append([i_4, i_5, i_6])

    line_color = 'black'
    plty_linewidth = 2
    font_size = 16

    # mesh3D_Differential_element_1 = fdt.create_mesh3d_for_dif_element_torus(mesh_differential_element_1, 1, [0, 0, 0], 0, 0, 0, frame=True)
    mesh_torus_segment = meshes[1]
    # mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Torussegment.stl')
    # front_line_upper =
    vertices_1, I_1, J_1, K_1 = bf.stl2mesh3d(mesh_torus_segment)
    x_1, y_1, z_1 = vertices_1.T
    outer_line_left_1 = []
    inner_line_left_1 = []
    outer_line_right_1 = []
    inner_line_right_1 = []

    for i_10, i_11, i_12 in zip(x_1, y_1, z_1):
        if i_10 == 0:
            if 19.5 ** 2 <= abs((i_11 + 56.569) ** 2 + (i_12 - 56.569) ** 2) <= 20.5 ** 2:
                outer_line_left_1.append([i_10, i_11, i_12])
            else:
                inner_line_left_1.append([i_10, i_11, i_12])
        elif -11.8 <= i_11 / i_10 <= -10.4:
            if 19.5 ** 2 <= abs((i_11 + 56.569) ** 2 + (i_12 - 56.569) ** 2) <= 20.5 ** 2:
                outer_line_right_1.append([i_10, i_11, i_12])
            else:
                inner_line_right_1.append([i_10, i_11, i_12])

    inner_line_left_1_lower_inner = []
    inner_line_left_1_lower_outer = []
    inner_line_left_1_upper_inner = []
    inner_line_left_1_upper_outer = []
    inner_line_left_1_upper_outer_upper = []
    inner_line_left_1_upper_outer_lower = []

    outer_line_left_1_lower_inner = []
    outer_line_left_1_lower_outer = []
    outer_line_left_1_upper_inner = []
    outer_line_left_1_upper_outer = []
    outer_line_left_1_upper_outer_upper = []
    outer_line_left_1_upper_outer_lower = []

    inner_line_right_1_lower_inner = []
    inner_line_right_1_lower_outer = []
    inner_line_right_1_upper_inner = []
    inner_line_right_1_upper_outer = []
    inner_line_right_1_upper_outer_upper = []
    inner_line_right_1_upper_outer_lower = []

    outer_line_right_1_lower_inner = []
    outer_line_right_1_lower_outer = []
    outer_line_right_1_upper_inner = []
    outer_line_right_1_upper_outer = []
    outer_line_right_1_upper_outer_upper = []
    outer_line_right_1_upper_outer_lower = []

    for i_13, i_14, i_15 in inner_line_left_1:
        if i_14 + 56.569 <= 0:
            if i_15 - 56.569 >= 0:
                if i_15 >= 66:
                    inner_line_left_1_upper_outer_upper.append([i_13, i_14, i_15])
                else:
                    inner_line_left_1_upper_outer_lower.append([i_13, i_14, i_15])
            else:
                inner_line_left_1_lower_outer.append([i_13, i_14, i_15])

        else:
            if i_15 - 56.569 >= 0:
                inner_line_left_1_upper_inner.append([i_13, i_14, i_15])
            else:
                inner_line_left_1_lower_inner.append([i_13, i_14, i_15])

    for i_13, i_14, i_15 in outer_line_left_1:
        if i_14 + 56.569 <= 0:
            if i_15 - 56.569 >= 0:
                if i_15 >= 66:
                    outer_line_left_1_upper_outer_upper.append([i_13, i_14, i_15])
                else:
                    outer_line_left_1_upper_outer_lower.append([i_13, i_14, i_15])
            else:
                outer_line_left_1_lower_outer.append([i_13, i_14, i_15])

        else:
            if i_15 - 56.569 >= 0:
                outer_line_left_1_upper_inner.append([i_13, i_14, i_15])
            else:
                outer_line_left_1_lower_inner.append([i_13, i_14, i_15])

    for i_13, i_14, i_15 in inner_line_right_1:
        if i_14 + 56.32 <= 0:
            if i_15 - 56.32 >= 0:
                if i_15 >= 66:
                    inner_line_right_1_upper_outer_upper.append([i_13, i_14, i_15])
                else:
                    inner_line_right_1_upper_outer_lower.append([i_13, i_14, i_15])
            else:
                inner_line_right_1_lower_outer.append([i_13, i_14, i_15])

        else:
            if i_15 - 56.32 >= 0:
                inner_line_right_1_upper_inner.append([i_13, i_14, i_15])
            else:
                inner_line_right_1_lower_inner.append([i_13, i_14, i_15])

    for i_13, i_14, i_15 in outer_line_right_1:
        if i_14 + 56.32 <= 0:
            if i_15 - 56.32 >= 0:
                if i_15 >= 66:
                    outer_line_right_1_upper_outer_upper.append([i_13, i_14, i_15])
                else:
                    outer_line_right_1_upper_outer_lower.append([i_13, i_14, i_15])
            else:
                outer_line_right_1_lower_outer.append([i_13, i_14, i_15])

        else:
            if i_15 - 56.32 >= 0:
                outer_line_right_1_upper_inner.append([i_13, i_14, i_15])
            else:
                outer_line_right_1_lower_inner.append([i_13, i_14, i_15])

    inner_left_circle = (list(
        reversed(inner_line_left_1_upper_outer_lower)) + inner_line_left_1_lower_outer + inner_line_left_1_lower_inner
                         + list(reversed(inner_line_left_1_upper_inner)) + list(
                reversed(inner_line_left_1_upper_outer_upper))
                         )
    outer_left_circle = (list(
        reversed(outer_line_left_1_upper_outer_lower)) + outer_line_left_1_lower_outer + outer_line_left_1_lower_inner
                         + list(reversed(outer_line_left_1_upper_inner)) + list(
                reversed(outer_line_left_1_upper_outer_upper))
                         )
    inner_right_circle = (inner_line_right_1_upper_outer_lower + list(reversed(inner_line_right_1_lower_outer)) + list(
        reversed(inner_line_right_1_lower_inner))
                          + inner_line_right_1_upper_inner + inner_line_right_1_upper_outer_upper
                          )
    outer_right_circle = (outer_line_right_1_upper_outer_lower + list(reversed(outer_line_right_1_lower_outer)) + list(
        reversed(outer_line_right_1_lower_inner))
                          + outer_line_right_1_upper_inner + outer_line_right_1_upper_outer_upper
                          )
    connection_line_left_upper = [inner_left_circle[-1]] + [outer_left_circle[-1]]
    connection_line_left_lower = [inner_left_circle[0]] + [outer_left_circle[0]]
    connection_line_right_upper = [inner_right_circle[-1]] + [outer_right_circle[-1]]
    connection_line_right_lower = [inner_right_circle[0]] + [outer_right_circle[0]]
    connection_line_outer_lower = [outer_left_circle[0]] + [outer_right_circle[0]]
    connection_line_outer_upper = [outer_left_circle[-1]] + [outer_right_circle[-1]]
    connection_line_inner_lower = [inner_left_circle[0]] + [inner_right_circle[0]]
    connection_line_inner_upper = [inner_left_circle[-1]] + [inner_right_circle[-1]]

    points_for_line_to_center_upper_left = [connection_line_left_upper[0]] + [[0, 0, 0]]
    points_for_line_to_center_upper_right = [connection_line_right_upper[0]] + [[0, 0, 0]]
    points_for_line_to_center_lower_left = [connection_line_left_lower[0]] + [[0, -56.569, 56.569]]
    points_for_line_to_center_lower_right = [connection_line_right_lower[0]] + [[4.93, -56.353, 56.569]]

    line_for_outer_circle_in_z = np.sin(np.pi * np.linspace(45, 135, 180) / 180) * 100
    line_for_outer_circle_in_y = -np.cos(np.pi * np.linspace(45, 135, 180) / 180) * 100
    line_for_inner_circle_in_z = np.sin(np.pi * np.linspace(45, 135, 180) / 180) * 98.5
    line_for_inner_circle_in_y = -np.cos(np.pi * np.linspace(45, 135, 180) / 180) * 98.5
    points_for_outer_circle = [[i_21, i_22, i_23] for i_21, i_22, i_23 in
                               zip(np.linspace(0, 0, 180), line_for_outer_circle_in_y, line_for_outer_circle_in_z)]
    points_for_inner_circle = [[i_21, i_22, i_23] for i_21, i_22, i_23 in
                               zip(np.linspace(0, 0, 180), line_for_inner_circle_in_y, line_for_inner_circle_in_z)]

    line_for_partial_outer_torus_right_shell_in_z = np.sin(np.pi * np.linspace(0, 45, 90) / 180) * 20 + 56.569
    line_for_partial_outer_torus_right_shell_in_y = -np.cos(np.pi * np.linspace(0, 45, 90) / 180) * 20 - 56.569
    line_for_partial_inner_torus_right_shell_in_z = np.sin(np.pi * np.linspace(0, 45, 90) / 180) * 18.5 + 56.569
    line_for_partial_inner_torus_right_shell_in_y = -np.cos(np.pi * np.linspace(0, 45, 90) / 180) * 18.5 - 56.569
    points_for_partial_outer_torus_right_shell = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 90),
                                                                                                 line_for_partial_outer_torus_right_shell_in_y,
                                                                                                 line_for_partial_outer_torus_right_shell_in_z)]
    points_for_partial_inner_torus_right_shell = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 90),
                                                                                                 line_for_partial_inner_torus_right_shell_in_y,
                                                                                                 line_for_partial_inner_torus_right_shell_in_z)]

    line_for_partial_outer_torus_left_shell_in_z = np.sin(np.pi * np.linspace(135, 180, 90) / 180) * 20 + 56.569
    line_for_partial_outer_torus_left_shell_in_y = -np.cos(np.pi * np.linspace(135, 180, 90) / 180) * 20 + 56.569
    line_for_partial_inner_torus_left_shell_in_z = np.sin(np.pi * np.linspace(135, 180, 90) / 180) * 18.5 + 56.569
    line_for_partial_inner_torus_left_shell_in_y = -np.cos(np.pi * np.linspace(135, 180, 90) / 180) * 18.5 + 56.569
    points_for_partial_outer_torus_left_shell = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 90),
                                                                                                line_for_partial_outer_torus_left_shell_in_y,
                                                                                                line_for_partial_outer_torus_left_shell_in_z)]
    points_for_partial_inner_torus_left_shell = [[i_21, i_22, i_23] for i_21, i_22, i_23 in zip(np.linspace(0, 0, 90),
                                                                                                line_for_partial_inner_torus_left_shell_in_y,
                                                                                                line_for_partial_inner_torus_left_shell_in_z)]

    points_for_inner_shell_right = [[0, -75.069, 56.569], [0, -75.069, 0]]
    points_for_outer_shell_right = [[0, -76.569, 56.569], [0, -76.569, 0]]
    points_for_inner_shell_left = [[0, +75.069, 56.569], [0, +75.069, 0]]
    points_for_outer_shell_left = [[0, +76.569, 56.569], [0, +76.569, 0]]

    full_torus_right_line_outer_z = np.sin(np.pi * np.linspace(0, 360, 360) / 180) * 20 + 56.569
    full_torus_right_line_outer_y = -np.cos(np.pi * np.linspace(0, 360, 360) / 180) * 20 - 56.569
    full_torus_right_line_inner_z = np.sin(np.pi * np.linspace(0, 360, 360) / 180) * 18.5 + 56.569
    full_torus_right_line_inner_y = -np.cos(np.pi * np.linspace(0, 360, 360) / 180) * 18.5 - 56.569
    points_full_torus_right_line_outer = [[i_21, i_22, i_23] for i_21, i_22, i_23 in
                                          zip(np.linspace(0, 0, 360), full_torus_right_line_outer_y,
                                              full_torus_right_line_outer_z)]
    points_full_torus_right_line_inner = [[i_21, i_22, i_23] for i_21, i_22, i_23 in
                                          zip(np.linspace(0, 0, 360), full_torus_right_line_inner_y,
                                              full_torus_right_line_inner_z)]
    full_torus_left_line_outer_z = np.sin(np.pi * np.linspace(0, 360, 360) / 180) * 20 + 56.569
    full_torus_left_line_outer_y = -np.cos(np.pi * np.linspace(0, 360, 360) / 180) * 20 + 56.569
    full_torus_left_line_inner_z = np.sin(np.pi * np.linspace(0, 360, 360) / 180) * 18.5 + 56.569
    full_torus_left_line_inner_y = -np.cos(np.pi * np.linspace(0, 360, 360) / 180) * 18.5 + 56.569
    points_full_torus_left_line_outer = [[i_21, i_22, i_23] for i_21, i_22, i_23 in
                                         zip(np.linspace(0, 0, 360), full_torus_left_line_outer_y,
                                             full_torus_left_line_outer_z)]
    points_full_torus_left_line_inner = [[i_21, i_22, i_23] for i_21, i_22, i_23 in
                                         zip(np.linspace(0, 0, 360), full_torus_left_line_inner_y,
                                             full_torus_left_line_inner_z)]

    # line_for_torus_upper = [[0, -56.569, 56.569], [0, -56.569, 0]]
    # line_for_torus_lower = [[0, -56.569, 56.569], [0, -56.569, 0]]


    mesh_full_torus = meshes[2]
    vertices_2, I_2, J_2, K_2 = bf.stl2mesh3d(mesh_full_torus)
    x_2, y_2, z_2 = vertices_2.T

    # mesh_tankshell = mesh.Mesh.from_file('./meshes/Halber_Boden.stl')
    mesh_tankshell = meshes[3]
    vertices_3, I_3, J_3, K_3 = bf.stl2mesh3d(mesh_tankshell)
    x_3, y_3, z_3 = vertices_3.T

    # mesh_torus_halfcircle = mesh.Mesh.from_file('./meshes/Halber_Torus.stl')
    mesh_torus_halfcircle = meshes[4]
    vertices_4, I_4, J_4, K_4 = bf.stl2mesh3d(mesh_torus_halfcircle)
    x_4, y_4, z_4 = vertices_4.T

    # # rotational Transformation
    # vector = np.array(pos_vec)
    # rotation_matrix = bf.combine_rotation_matrixes(zeta, eta, theta)
    # x, y, z = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), np.array([x, y, z])) * scalingfactor
    # x = x + vector[0, None]
    # y = y + vector[1, None]
    # z = z + vector[2, None]
    # array_for_arrow_tip = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), array_for_arrow_tip) * scalingfactor + vector[:, None]
    # sorted_array_inner_ring = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), sorted_array_inner_ring) * scalingfactor + vector[:, None]
    # sorted_array_outer_ring = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), sorted_array_outer_ring) * scalingfactor + vector[:, None]
    # sorted_array_end_ring = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), sorted_array_end_ring) * scalingfactor + vector[:, None]
    # line_0 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_0) * scalingfactor + vector[:, None]
    # line_1 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_1) * scalingfactor + vector[:, None]
    # line_2 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_2) * scalingfactor + vector[:, None]
    # line_3 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_3) * scalingfactor + vector[:, None]
    # line_4 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_4) * scalingfactor + vector[:, None]
    # line_5 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_5) * scalingfactor + vector[:, None]
    #
    #
    # mesh3D_base_body_2 = go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K,
    #                              color=bodycolor, opacity=0.50, showscale=False, visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_inner_ring_2 = go.Scatter3d(x=sorted_array_inner_ring[0, :], y=sorted_array_inner_ring[1, :],
    #                                    z=sorted_array_inner_ring[2, :],
    #                                    mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_outer_ring_2 = go.Scatter3d(x=sorted_array_outer_ring[0, :], y=sorted_array_outer_ring[1, :],
    #                                    z=sorted_array_outer_ring[2, :],
    #                                    mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_end_2 = go.Scatter3d(x=sorted_array_end_ring[0, :], y=sorted_array_end_ring[1, :],
    #                             z=sorted_array_end_ring[2, :],
    #                             mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_Tip = go.Scatter3d(x=array_for_arrow_tip[0, :], y=array_for_arrow_tip[1, :], z=array_for_arrow_tip[2, :],
    #                           mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_line_0 = go.Scatter3d(x=line_0[0, :], y=line_0[1, :], z=line_0[2, :], mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_line_1 = go.Scatter3d(x=line_1[0, :], y=line_1[1, :], z=line_1[2, :], mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_line_2 = go.Scatter3d(x=line_2[0, :], y=line_2[1, :], z=line_2[2, :], mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_line_3 = go.Scatter3d(x=line_3[0, :], y=line_3[1, :], z=line_3[2, :], mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_line_4 = go.Scatter3d(x=line_4[0, :], y=line_4[1, :], z=line_4[2, :], mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    # mesh3D_line_5 = go.Scatter3d(x=line_5[0, :], y=line_5[1, :], z=line_5[2, :], mode='lines',
    #                                 line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))

    mesh3D_torus_diff_element = go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K,
                                   color='grey', opacity=0.60, showscale=False, visible=True,
                                   contour=dict(show=True, width=16))
    mesh3D_inner_line_left = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_left], y=[i_1[1] for i_1 in inner_line_left],
                                          z=[i_1[2] for i_1 in inner_line_left],
                                          mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True,
                                          hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_outer_line_left = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_left], y=[i_1[1] for i_1 in outer_line_left],
                                          z=[i_1[2] for i_1 in outer_line_left],
                                          mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True,
                                          hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_inner_line_right = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_right],
                                           y=[i_1[1] for i_1 in inner_line_right],
                                           z=[i_1[2] for i_1 in inner_line_right],
                                           mode='lines', line=dict(color=line_color, width=plty_linewidth),
                                           visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_outer_line_right = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_right],
                                           y=[i_1[1] for i_1 in outer_line_right],
                                           z=[i_1[2] for i_1 in outer_line_right],
                                           mode='lines', line=dict(color=line_color, width=plty_linewidth),
                                           visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_inner_line_upper = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_upper],
                                           y=[i_1[1] for i_1 in inner_line_upper],
                                           z=[i_1[2] for i_1 in inner_line_upper],
                                           mode='lines', line=dict(color=line_color, width=plty_linewidth),
                                           visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_inner_line_lower = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_lower],
                                           y=[i_1[1] for i_1 in inner_line_lower],
                                           z=[i_1[2] for i_1 in inner_line_lower],
                                           mode='lines', line=dict(color=line_color, width=plty_linewidth),
                                           visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_outer_line_upper = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_upper],
                                           y=[i_1[1] for i_1 in outer_line_upper],
                                           z=[i_1[2] for i_1 in outer_line_upper],
                                           mode='lines', line=dict(color=line_color, width=plty_linewidth),
                                           visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_outer_line_lower = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_lower],
                                           y=[i_1[1] for i_1 in outer_line_lower],
                                           z=[i_1[2] for i_1 in outer_line_lower],
                                           mode='lines', line=dict(color=line_color, width=plty_linewidth),
                                           visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_upper_left_line = go.Scatter3d(x=[i_1[0] for i_1 in upper_left_line], y=[i_1[1] for i_1 in upper_left_line],
                                          z=[i_1[2] for i_1 in upper_left_line],
                                          mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True,
                                          hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_upper_right_line = go.Scatter3d(x=[i_1[0] for i_1 in upper_right_line],
                                           y=[i_1[1] for i_1 in upper_right_line],
                                           z=[i_1[2] for i_1 in upper_right_line],
                                           mode='lines', line=dict(color=line_color, width=plty_linewidth),
                                           visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_lower_left_line = go.Scatter3d(x=[i_1[0] for i_1 in lower_left_line], y=[i_1[1] for i_1 in lower_left_line],
                                          z=[i_1[2] for i_1 in lower_left_line],
                                          mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True,
                                          hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_lower_right_line = go.Scatter3d(x=[i_1[0] for i_1 in lower_right_line],
                                           y=[i_1[1] for i_1 in lower_right_line],
                                           z=[i_1[2] for i_1 in lower_right_line],
                                           mode='lines', line=dict(color=line_color, width=plty_linewidth),
                                           visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_torus_segment = go.Mesh3d(x=x_1, y=y_1, z=z_1, i=I_1, j=J_1, k=K_1,
                                   color='darkgrey', opacity=0.80, showscale=False, visible=True,
                                   contour=dict(show=True, width=16))
    # mesh3d_line_to_center_upper_left = go.Scatter3d(x=[i_1[0] for i_1 in upper_left_line],
    #                                                 y=[i_1[1] for i_1 in upper_left_line],
    #                                                 z=[i_1[2] for i_1 in upper_left_line],
    #                                                 mode='lines', line=dict(color='red', width=plty_linewidth),
    #                                                 visible=True, hoverinfo='none',
    #                                                 hoverlabel=dict(font_size=font_size))
    # mesh3D_outer_line_left_1 = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_left_1],
    #                                         y=[i_1[1] for i_1 in outer_line_left_1],
    #                                         z=[i_1[2] for i_1 in outer_line_left_1],
    #                                         mode='lines', line=dict(color=line_color, width=plty_linewidth),
    #                                         visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    # mesh3D_inner_line_left_1 = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_left_1],
    #                                         y=[i_1[1] for i_1 in inner_line_left_1],
    #                                         z=[i_1[2] for i_1 in inner_line_left_1],
    #                                         mode='lines', line=dict(color=line_color, width=plty_linewidth),
    #                                         visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    # mesh3D_outer_line_right_1 = go.Scatter3d(x=[i_1[0] for i_1 in outer_line_right_1],
    #                                          y=[i_1[1] for i_1 in outer_line_right_1],
    #                                          z=[i_1[2] for i_1 in outer_line_right_1],
    #                                          mode='lines', line=dict(color=line_color, width=plty_linewidth),
    #                                          visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    # mesh3D_inner_line_right_1 = go.Scatter3d(x=[i_1[0] for i_1 in inner_line_right_1],
    #                                          y=[i_1[1] for i_1 in inner_line_right_1],
    #                                          z=[i_1[2] for i_1 in inner_line_right_1],
    #                                          mode='lines', line=dict(color=line_color, width=plty_linewidth),
    #                                          visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))

    mesh3D_inner_left_circle = go.Scatter3d(x=[i_1[0] for i_1 in inner_left_circle],
                                            y=[i_1[1] for i_1 in inner_left_circle],
                                            z=[i_1[2] for i_1 in inner_left_circle],
                                            mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                            hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_outer_left_circle = go.Scatter3d(x=[i_1[0] for i_1 in outer_left_circle],
                                            y=[i_1[1] for i_1 in outer_left_circle],
                                            z=[i_1[2] for i_1 in outer_left_circle],
                                            mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                            hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_inner_right_circle = go.Scatter3d(x=[i_1[0] for i_1 in inner_right_circle],
                                             y=[i_1[1] for i_1 in inner_right_circle],
                                             z=[i_1[2] for i_1 in inner_right_circle],
                                             mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                             hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_outer_right_circle = go.Scatter3d(x=[i_1[0] for i_1 in outer_right_circle],
                                             y=[i_1[1] for i_1 in outer_right_circle],
                                             z=[i_1[2] for i_1 in outer_right_circle],
                                             mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                             hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_connection_line_right_upper = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_right_upper],
                                                      y=[i_1[1] for i_1 in connection_line_right_upper],
                                                      z=[i_1[2] for i_1 in connection_line_right_upper],
                                                      mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                      visible=True, hoverinfo='none',
                                                      hoverlabel=dict(font_size=font_size))
    mesh3d_connection_line_right_lower = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_right_lower],
                                                      y=[i_1[1] for i_1 in connection_line_right_lower],
                                                      z=[i_1[2] for i_1 in connection_line_right_lower],
                                                      mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                      visible=True, hoverinfo='none',
                                                      hoverlabel=dict(font_size=font_size))
    mesh3d_connection_line_left_upper = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_left_upper],
                                                     y=[i_1[1] for i_1 in connection_line_left_upper],
                                                     z=[i_1[2] for i_1 in connection_line_left_upper],
                                                     mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                     visible=True, hoverinfo='none',
                                                     hoverlabel=dict(font_size=font_size))
    mesh3d_connection_line_left_lower = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_left_lower],
                                                     y=[i_1[1] for i_1 in connection_line_left_lower],
                                                     z=[i_1[2] for i_1 in connection_line_left_lower],
                                                     mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                     visible=True, hoverinfo='none',
                                                     hoverlabel=dict(font_size=font_size))
    mesh3d_connection_line_outer_upper = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_outer_upper],
                                                      y=[i_1[1] for i_1 in connection_line_outer_upper],
                                                      z=[i_1[2] for i_1 in connection_line_outer_upper],
                                                      mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                      visible=True, hoverinfo='none',
                                                      hoverlabel=dict(font_size=font_size))
    mesh3d_connection_line_outer_lower = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_outer_lower],
                                                      y=[i_1[1] for i_1 in connection_line_outer_lower],
                                                      z=[i_1[2] for i_1 in connection_line_outer_lower],
                                                      mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                      visible=True, hoverinfo='none',
                                                      hoverlabel=dict(font_size=font_size))
    mesh3d_connection_line_inner_upper = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_inner_upper],
                                                      y=[i_1[1] for i_1 in connection_line_inner_upper],
                                                      z=[i_1[2] for i_1 in connection_line_inner_upper],
                                                      mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                      visible=True, hoverinfo='none',
                                                      hoverlabel=dict(font_size=font_size))
    mesh3d_connection_line_inner_lower = go.Scatter3d(x=[i_1[0] for i_1 in connection_line_inner_lower],
                                                      y=[i_1[1] for i_1 in connection_line_inner_lower],
                                                      z=[i_1[2] for i_1 in connection_line_inner_lower],
                                                      mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                      visible=True, hoverinfo='none',
                                                      hoverlabel=dict(font_size=font_size))
    mesh3d_line_to_center_upper_left = go.Scatter3d(x=[i_1[0] for i_1 in points_for_line_to_center_upper_left],
                                                    y=[i_1[1] for i_1 in points_for_line_to_center_upper_left],
                                                    z=[i_1[2] for i_1 in points_for_line_to_center_upper_left],
                                                    mode='lines', line=dict(color='red', width=plty_linewidth),
                                                    visible=True, hoverinfo='none',
                                                    hoverlabel=dict(font_size=font_size))
    mesh3d_line_to_center_upper_right = go.Scatter3d(x=[i_1[0] for i_1 in points_for_line_to_center_upper_right],
                                                     y=[i_1[1] for i_1 in points_for_line_to_center_upper_right],
                                                     z=[i_1[2] for i_1 in points_for_line_to_center_upper_right],
                                                     mode='lines', line=dict(color='red', width=plty_linewidth),
                                                     visible=True, hoverinfo='none',
                                                     hoverlabel=dict(font_size=font_size))
    mesh3d_line_to_center_lower_left = go.Scatter3d(x=[i_1[0] for i_1 in points_for_line_to_center_lower_left],
                                                    y=[i_1[1] for i_1 in points_for_line_to_center_lower_left],
                                                    z=[i_1[2] for i_1 in points_for_line_to_center_lower_left],
                                                    mode='lines', line=dict(color='red', width=plty_linewidth),
                                                    visible=True, hoverinfo='none',
                                                    hoverlabel=dict(font_size=font_size))
    mesh3d_line_to_center_lower_right = go.Scatter3d(x=[i_1[0] for i_1 in points_for_line_to_center_lower_right],
                                                     y=[i_1[1] for i_1 in points_for_line_to_center_lower_right],
                                                     z=[i_1[2] for i_1 in points_for_line_to_center_lower_right],
                                                     mode='lines', line=dict(color='red', width=plty_linewidth),
                                                     visible=True, hoverinfo='none',
                                                     hoverlabel=dict(font_size=font_size))
    mesh3D_inner_circle = go.Scatter3d(x=[i_1[0] for i_1 in points_for_inner_circle],
                                       y=[i_1[1] for i_1 in points_for_inner_circle],
                                       z=[i_1[2] for i_1 in points_for_inner_circle],
                                       mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                       hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_outer_circle = go.Scatter3d(x=[i_1[0] for i_1 in points_for_outer_circle],
                                       y=[i_1[1] for i_1 in points_for_outer_circle],
                                       z=[i_1[2] for i_1 in points_for_outer_circle],
                                       mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                       hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_outer_shell_right = go.Scatter3d(x=[i_1[0] for i_1 in points_for_outer_shell_right],
                                            y=[i_1[1] for i_1 in points_for_outer_shell_right],
                                            z=[i_1[2] for i_1 in points_for_outer_shell_right],
                                            mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                            hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_inner_shell_right = go.Scatter3d(x=[i_1[0] for i_1 in points_for_inner_shell_right],
                                            y=[i_1[1] for i_1 in points_for_inner_shell_right],
                                            z=[i_1[2] for i_1 in points_for_inner_shell_right],
                                            mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                            hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_outer_shell_left = go.Scatter3d(x=[i_1[0] for i_1 in points_for_outer_shell_left],
                                           y=[i_1[1] for i_1 in points_for_outer_shell_left],
                                           z=[i_1[2] for i_1 in points_for_outer_shell_left],
                                           mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                           hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_inner_shell_left = go.Scatter3d(x=[i_1[0] for i_1 in points_for_inner_shell_left],
                                           y=[i_1[1] for i_1 in points_for_inner_shell_left],
                                           z=[i_1[2] for i_1 in points_for_inner_shell_left],
                                           mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                           hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_inner_left_torus = go.Scatter3d(x=[i_1[0] for i_1 in points_for_partial_inner_torus_right_shell],
                                           y=[i_1[1] for i_1 in points_for_partial_inner_torus_right_shell],
                                           z=[i_1[2] for i_1 in points_for_partial_inner_torus_right_shell],
                                           mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                           hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_outer_left_torus = go.Scatter3d(x=[i_1[0] for i_1 in points_for_partial_outer_torus_right_shell],
                                           y=[i_1[1] for i_1 in points_for_partial_outer_torus_right_shell],
                                           z=[i_1[2] for i_1 in points_for_partial_outer_torus_right_shell],
                                           mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                           hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_inner_right_torus = go.Scatter3d(x=[i_1[0] for i_1 in points_for_partial_inner_torus_left_shell],
                                            y=[i_1[1] for i_1 in points_for_partial_inner_torus_left_shell],
                                            z=[i_1[2] for i_1 in points_for_partial_inner_torus_left_shell],
                                            mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                            hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_outer_right_torus = go.Scatter3d(x=[i_1[0] for i_1 in points_for_partial_outer_torus_left_shell],
                                            y=[i_1[1] for i_1 in points_for_partial_outer_torus_left_shell],
                                            z=[i_1[2] for i_1 in points_for_partial_outer_torus_left_shell],
                                            mode='lines', line=dict(color='gray', width=plty_linewidth), visible=True,
                                            hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_full_torus_right_line_outer = go.Scatter3d(x=[i_1[0] for i_1 in points_full_torus_right_line_outer],
                                                      y=[i_1[1] for i_1 in points_full_torus_right_line_outer],
                                                      z=[i_1[2] for i_1 in points_full_torus_right_line_outer],
                                                      mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                      visible=True, hoverinfo='none',
                                                      hoverlabel=dict(font_size=font_size))
    mesh3D_full_torus_right_line_inner = go.Scatter3d(x=[i_1[0] for i_1 in points_full_torus_right_line_inner],
                                                      y=[i_1[1] for i_1 in points_full_torus_right_line_inner],
                                                      z=[i_1[2] for i_1 in points_full_torus_right_line_inner],
                                                      mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                      visible=True, hoverinfo='none',
                                                      hoverlabel=dict(font_size=font_size))
    mesh3D_full_torus_left_line_outer = go.Scatter3d(x=[i_1[0] for i_1 in points_full_torus_left_line_outer],
                                                     y=[i_1[1] for i_1 in points_full_torus_left_line_outer],
                                                     z=[i_1[2] for i_1 in points_full_torus_left_line_outer],
                                                     mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                     visible=True, hoverinfo='none',
                                                     hoverlabel=dict(font_size=font_size))
    mesh3D_full_torus_left_line_inner = go.Scatter3d(x=[i_1[0] for i_1 in points_full_torus_left_line_inner],
                                                     y=[i_1[1] for i_1 in points_full_torus_left_line_inner],
                                                     z=[i_1[2] for i_1 in points_full_torus_left_line_inner],
                                                     mode='lines', line=dict(color='gray', width=plty_linewidth),
                                                     visible=True, hoverinfo='none',
                                                     hoverlabel=dict(font_size=font_size))
    # mesh3D_torus_ring = go.Mesh3d(x=x_2, y=y_2, z=z_2, i=I_2, j=J_2, k=K_2,
    #                                color='lightgray', opacity=0.20, showscale=False, visible=True,
    #                                contour=dict(show=True, width=16))
    mesh3D_tank_shell = go.Mesh3d(x=x_3, y=y_3, z=z_3, i=I_3, j=J_3, k=K_3,
                                   color='lightgray', opacity=0.20, showscale=False, visible=True,
                                   contour=dict(show=True, width=16))
    mesh3D_half_torus = go.Mesh3d(x=x_4, y=y_4, z=z_4, i=I_4, j=J_4, k=K_4,
                                   color='lightgray', opacity=0.20, showscale=False, visible=True,
                                   contour=dict(show=True, width=16))
    mesh3D_torus_overall = [mesh3D_torus_diff_element,
                            mesh3D_inner_line_left, mesh3D_outer_line_left,
                            mesh3D_inner_line_right, mesh3D_outer_line_right, mesh3D_inner_line_upper,
                            mesh3D_inner_line_lower, mesh3D_outer_line_upper, mesh3D_outer_line_lower,
                            mesh3D_upper_left_line, mesh3D_upper_right_line, mesh3D_lower_left_line,
                            mesh3D_lower_right_line, mesh3D_torus_segment,
                            # mesh3d_line_to_center_upper_left,
                            # mesh3D_outer_line_left_1, mesh3D_inner_line_left_1, mesh3D_outer_line_right_1,
                            # mesh3D_inner_line_right_1,
                            mesh3D_inner_left_circle, mesh3D_outer_left_circle,
                            mesh3D_inner_right_circle, mesh3D_outer_right_circle, mesh3d_connection_line_right_upper,
                            mesh3d_connection_line_right_lower, mesh3d_connection_line_left_upper,
                            mesh3d_connection_line_left_lower, mesh3d_connection_line_outer_upper,
                            mesh3d_connection_line_outer_lower, mesh3d_connection_line_inner_upper,
                            mesh3d_connection_line_inner_lower, mesh3d_line_to_center_upper_left,
                            mesh3d_line_to_center_upper_right, mesh3d_line_to_center_lower_left,
                            mesh3d_line_to_center_lower_right, mesh3D_inner_circle, mesh3D_outer_circle,
                            mesh3d_outer_shell_right, mesh3d_inner_shell_right, mesh3d_outer_shell_left,
                            mesh3d_inner_shell_left, mesh3D_inner_left_torus, mesh3D_outer_left_torus,
                            mesh3D_inner_right_torus, mesh3D_outer_right_torus, mesh3D_full_torus_right_line_outer,
                            mesh3D_full_torus_right_line_inner, mesh3D_full_torus_left_line_outer,
                            mesh3D_full_torus_left_line_inner,
                            # mesh3D_torus_ring,
                            mesh3D_tank_shell, mesh3D_half_torus
                            ] # 46 elements

        # = [mesh3D_base_body_2, mesh3D_inner_ring_2, mesh3D_outer_ring_2, mesh3D_Tip, mesh3D_line_0,
        #            mesh3D_line_1, mesh3D_line_2,
        #            mesh3D_line_3, mesh3D_line_4, mesh3D_line_5, mesh3D_end_2]

    return mesh3D_torus_overall