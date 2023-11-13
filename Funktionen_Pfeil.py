import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import numpy
from stl import mesh
import copy
import BasisFunktionen as bf


def create_mesh3d_for_arrow(mesh_arrow, scalingfactor, pos_vec, zeta, eta, theta, hovertext_1,
                            ptly_linewidth=2, line_color='black', bodycolor='lightgray'):
    vertices, I, J, K = bf.stl2mesh3d(mesh_arrow)
    x, y, z = vertices.T
    colorscale = [[0, '#e5dee5'], [1, '#e5dee5']]
    arrow_tip = []
    arrow_end_x = []
    arrow_end_y = []
    arrow_end_z = []
    arrow_inner_ring_x = []
    arrow_inner_ring_y = []
    arrow_inner_ring_z = []
    arrow_outer_ring_x = []
    arrow_outer_ring_y = []
    arrow_outer_ring_z = []

    for x_1, y_1, z_1 in zip(x, y, z):
        if y_1 == min(y):
            arrow_tip = [x_1, y_1, z_1]
        elif y_1 == max(y):
            arrow_end_x.append(x_1)
            arrow_inner_ring_x.append(x_1)
            arrow_end_y.append(y_1)
            arrow_inner_ring_y.append(y_1)
            arrow_end_z.append(z_1)
            arrow_inner_ring_z.append(z_1)
        elif (y_1 == 0) & (z_1 not in arrow_inner_ring_z):
            arrow_outer_ring_x.append(x_1)
            arrow_outer_ring_y.append(y_1)
            arrow_outer_ring_z.append(z_1)

    neg_array = copy.deepcopy(np.empty((0, 3), float))
    pos_array = copy.deepcopy(np.empty((0, 3), float))
    for i in np.array([arrow_inner_ring_x, arrow_inner_ring_y, arrow_inner_ring_z]).T:
        if i[2] <= 0:
            neg_array = np.append(neg_array, [i], axis=0)
        else:
            pos_array = np.append(pos_array, [i], axis=0)

    sorted_neg_array = neg_array[neg_array[:, 0].argsort()]
    sorted_pos_array = np.flip(pos_array[pos_array[:, 0].argsort()], 0)
    sorted_array = np.append(sorted_neg_array, sorted_pos_array, axis=0).T
    sorted_array = np.append(sorted_array.T, [[i_0 for i_0 in (sorted_array[:, 0])]], axis=0).T
    array_for_inner_ring = copy.deepcopy(sorted_array)
    array_for_inner_ring[1, :] = array_for_inner_ring[1, :] * 0
    array_for_outer_ring = copy.deepcopy(array_for_inner_ring)
    array_for_outer_ring[0, :] = array_for_outer_ring[0, :] * 1.5
    array_for_outer_ring[2, :] = array_for_outer_ring[2, :] * 1.5
    array_for_arrow_tip = np.ones(array_for_inner_ring.shape, float)
    array_for_arrow_tip[0, :] = array_for_arrow_tip[0, :] * arrow_tip[0]
    array_for_arrow_tip[1, :] = array_for_arrow_tip[1, :] * arrow_tip[1]
    array_for_arrow_tip[2, :] = array_for_arrow_tip[2, :] * arrow_tip[2]
    line_0 = np.array([array_for_arrow_tip[:, 0], array_for_outer_ring[:, 0],
                       array_for_inner_ring[:, 0], sorted_array[:, 0]]).T
    line_1 = np.array([array_for_arrow_tip[:, 1], array_for_outer_ring[:, 1],
                       array_for_inner_ring[:, 1], sorted_array[:, 1]]).T
    line_2 = np.array([array_for_arrow_tip[:, 2], array_for_outer_ring[:, 2],
                       array_for_inner_ring[:, 2], sorted_array[:, 2]]).T
    line_3 = np.array([array_for_arrow_tip[:, 3], array_for_outer_ring[:, 3],
                       array_for_inner_ring[:, 3], sorted_array[:, 3]]).T
    line_4 = np.array([array_for_arrow_tip[:, 4], array_for_outer_ring[:, 4],
                       array_for_inner_ring[:, 4], sorted_array[:, 4]]).T
    line_5 = np.array([array_for_arrow_tip[:, 5], array_for_outer_ring[:, 5],
                       array_for_inner_ring[:, 5], sorted_array[:, 5]]).T

    # rotational & position & scaling Transformation
    vector = np.array(pos_vec)
    x, y, z = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), np.array([x, y, z])) * scalingfactor
    x = x + vector[0, None]
    y = y + vector[1, None]
    z = z + vector[2, None]
    array_for_arrow_tip = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), array_for_arrow_tip) * scalingfactor + vector[:, None]
    array_for_inner_ring = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), array_for_inner_ring) * scalingfactor + vector[:, None]
    array_for_outer_ring = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), array_for_outer_ring) * scalingfactor + vector[:, None]
    sorted_array = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), sorted_array) * scalingfactor + vector[:, None]
    line_0 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_0) * scalingfactor + vector[:, None]
    line_1 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_1) * scalingfactor + vector[:, None]
    line_2 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_2) * scalingfactor + vector[:, None]
    line_3 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_3) * scalingfactor + vector[:, None]
    line_4 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_4) * scalingfactor + vector[:, None]
    line_5 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_5) * scalingfactor + vector[:, None]


    mesh3D_base_body = go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K,
                                 color=bodycolor, opacity=0.50, showscale=False, visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_Tip = go.Scatter3d(x=array_for_arrow_tip[0, :], y=array_for_arrow_tip[1, :], z=array_for_arrow_tip[2, :],
                                mode='lines', line=dict(color=line_color, width=ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_inner_ring = go.Scatter3d(x=array_for_inner_ring[0, :], y=array_for_inner_ring[1, :], z=array_for_inner_ring[2, :],
                                mode='lines', line=dict(color=line_color, width=ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_outer_ring = go.Scatter3d(x=array_for_outer_ring[0, :], y=array_for_outer_ring[1, :], z=array_for_outer_ring[2, :],
                                mode='lines', line=dict(color=line_color, width=ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_end_ring = go.Scatter3d(x=sorted_array[0, :], y=sorted_array[1, :], z=sorted_array[2, :],
                                mode='lines', line=dict(color=line_color, width= ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_line_0 = go.Scatter3d(x=line_0[0, :], y=line_0[1, :], z=line_0[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_line_1 = go.Scatter3d(x=line_1[0, :], y=line_1[1, :], z=line_1[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_line_2 = go.Scatter3d(x=line_2[0, :], y=line_2[1, :], z=line_2[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_line_3 = go.Scatter3d(x=line_3[0, :], y=line_3[1, :], z=line_3[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_line_4 = go.Scatter3d(x=line_4[0, :], y=line_4[1, :], z=line_4[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_line_5 = go.Scatter3d(x=line_5[0, :], y=line_5[1, :], z=line_5[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True, hoverinfo='text', hovertext=hovertext_1)
    mesh3D_arrow = [mesh3D_base_body, mesh3D_Tip, mesh3D_inner_ring, mesh3D_outer_ring, mesh3D_end_ring, mesh3D_line_0,
                    mesh3D_line_1, mesh3D_line_2, mesh3D_line_3, mesh3D_line_4, mesh3D_line_5,]

    return mesh3D_arrow