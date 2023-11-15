import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import numpy
from stl import mesh
import copy
import BasisFunktionen as bf

def create_mesh3d_for_curved_arrow(mesh_curved_arrow, scalingfactor, pos_vec, zeta, eta, theta, hovertext_1,
                            ptly_linewidth=2, line_color='black', bodycolor='lightgray', font_size = 16):
    vertices, I, J, K = bf.stl2mesh3d(mesh_curved_arrow)
    x, y, z = vertices.T
    arrow_tip_x = []
    arrow_tip_y = []
    arrow_tip_z = []
    arrow_end_x = []
    arrow_end_y = []
    arrow_end_z = []
    arrow_inner_ring_x = []
    arrow_inner_ring_y = []
    arrow_inner_ring_z = []
    arrow_outer_ring_x = []
    arrow_outer_ring_y = []
    arrow_outer_ring_z = []

    # rotational transformation
    alpha = 0
    beta = 0
    gamma = 0
    rotation_matrix = bf.combine_rotation_matrixes(alpha, beta, gamma)

    for x_1, y_1, z_1 in zip(x, y, z):
        if y_1 == max(y):
            arrow_tip_x.append(x_1)
            arrow_tip_y.append(y_1)
            arrow_tip_z.append(z_1)
        elif y_1 == 0:
            if (((z_1 - 37.5) ** 2 + x_1 ** 2) ** 0.5) < 7.5:
                arrow_inner_ring_x.append(x_1)
                arrow_inner_ring_y.append(y_1)
                arrow_inner_ring_z.append(z_1)
            else:
                arrow_outer_ring_x.append(x_1)
                arrow_outer_ring_y.append(y_1)
                arrow_outer_ring_z.append(z_1)
        elif -1 < y_1 < 0:
            arrow_end_x.append(x_1)
            arrow_end_y.append(y_1)
            arrow_end_z.append(z_1)

    body_right_inner_line_x = []
    body_right_inner_line_y = []
    body_right_inner_line_z = []
    body_right_outer_line_x = []
    body_right_outer_line_y = []
    body_right_outer_line_z = []
    body_right_center_line_x = []
    body_right_center_line_y = []
    body_right_center_line_z = []
    body_left_inner_line_x = []
    body_left_inner_line_y = []
    body_left_inner_line_z = []
    body_left_outer_line_x = []
    body_left_outer_line_y = []
    body_left_outer_line_z = []
    body_left_center_line_x = []
    body_left_center_line_y = []
    body_left_center_line_z = []

    for x_2, y_2, z_2 in zip(x, y, z):
        if y_2 < -1:
            if x_2 < 0:
                if (y_2 ** 2 + z_2 ** 2) ** 0.5 < 37:
                    body_right_inner_line_x.append(x_2)
                    body_right_inner_line_y.append(y_2)
                    body_right_inner_line_z.append(z_2)
                elif (y_2 ** 2 + z_2 ** 2) ** 0.5 > 38:
                    body_right_outer_line_x.append(x_2)
                    body_right_outer_line_y.append(y_2)
                    body_right_outer_line_z.append(z_2)
                else:
                    body_right_center_line_x.append(x_2)
                    body_right_center_line_y.append(y_2)
                    body_right_center_line_z.append(z_2)
            else:
                if (y_2 ** 2 + z_2 ** 2) ** 0.5 < 37:
                    body_left_inner_line_x.append(x_2)
                    body_left_inner_line_y.append(y_2)
                    body_left_inner_line_z.append(z_2)
                elif (y_2 ** 2 + z_2 ** 2) ** 0.5 > 38:
                    body_left_outer_line_x.append(x_2)
                    body_left_outer_line_y.append(y_2)
                    body_left_outer_line_z.append(z_2)
                else:
                    body_left_center_line_x.append(x_2)
                    body_left_center_line_y.append(y_2)
                    body_left_center_line_z.append(z_2)

    neg_array_inner_ring = copy.deepcopy(np.empty((0, 3), float))
    pos_array_inner_ring = copy.deepcopy(np.empty((0, 3), float))
    for i in np.array([arrow_inner_ring_x, arrow_inner_ring_y, arrow_inner_ring_z]).T:
        if i[0] <= 0:
            neg_array_inner_ring = np.append(neg_array_inner_ring, [i], axis=0)
        else:
            pos_array_inner_ring = np.append(pos_array_inner_ring, [i], axis=0)

    neg_array_outer_ring = copy.deepcopy(np.empty((0, 3), float))
    pos_array_outer_ring = copy.deepcopy(np.empty((0, 3), float))
    for i in np.array([arrow_outer_ring_x, arrow_outer_ring_y, arrow_outer_ring_z]).T:
        if i[0] <= 0:
            neg_array_outer_ring = np.append(neg_array_outer_ring, [i], axis=0)
        else:
            pos_array_outer_ring = np.append(pos_array_outer_ring, [i], axis=0)

    neg_array_end_ring = copy.deepcopy(np.empty((0, 3), float))
    pos_array_end_ring = copy.deepcopy(np.empty((0, 3), float))
    for i in np.array([arrow_end_x, arrow_end_y, arrow_end_z]).T:
        if i[0] <= 0:
            neg_array_end_ring = np.append(neg_array_end_ring, [i], axis=0)
        else:
            pos_array_end_ring = np.append(pos_array_end_ring, [i], axis=0)

    sorted_neg_array_inner_ring = neg_array_inner_ring[neg_array_inner_ring[:, 2].argsort()]
    sorted_pos_array_inner_ring = np.flip(pos_array_inner_ring[pos_array_inner_ring[:, 2].argsort()], 0)
    sorted_array_inner_ring = np.append(sorted_neg_array_inner_ring, sorted_pos_array_inner_ring, axis=0).T
    sorted_array_inner_ring = np.append(sorted_array_inner_ring.T, [[i_0 for i_0 in (sorted_array_inner_ring[:, 0])]],
                                        axis=0).T
    sorted_neg_array_outer_ring = neg_array_outer_ring[neg_array_outer_ring[:, 2].argsort()]
    sorted_pos_array_outer_ring = np.flip(pos_array_outer_ring[pos_array_outer_ring[:, 2].argsort()], 0)
    sorted_array_outer_ring = np.append(sorted_neg_array_outer_ring, sorted_pos_array_outer_ring, axis=0).T
    sorted_array_outer_ring = np.append(sorted_array_outer_ring.T, [[i_0 for i_0 in (sorted_array_outer_ring[:, 0])]],
                                        axis=0).T
    sorted_neg_array_end_ring = neg_array_end_ring[neg_array_end_ring[:, 2].argsort()]
    sorted_pos_array_end_ring = np.flip(pos_array_end_ring[pos_array_end_ring[:, 2].argsort()], 0)
    sorted_array_end_ring = np.append(sorted_neg_array_end_ring, sorted_pos_array_end_ring, axis=0).T
    sorted_array_end_ring = np.append(sorted_array_end_ring.T, [[i_0 for i_0 in (sorted_array_end_ring[:, 0])]],
                                      axis=0).T
    arrow_tip_x = np.average(arrow_tip_x)
    arrow_tip_y = np.average(arrow_tip_y)
    arrow_tip_z = np.average(arrow_tip_z)
    array_for_arrow_tip = np.ones(sorted_array_outer_ring.shape, float)
    array_for_arrow_tip[0, :] = array_for_arrow_tip[0, :] * arrow_tip_x
    array_for_arrow_tip[1, :] = array_for_arrow_tip[1, :] * arrow_tip_y
    array_for_arrow_tip[2, :] = array_for_arrow_tip[2, :] * arrow_tip_z

    center_right_line = np.array([body_right_center_line_x, body_right_center_line_y, body_right_center_line_z])
    sorted_center_right_line = center_right_line.T[center_right_line[2, :].argsort()].T
    inner_right_line = np.array([body_right_inner_line_x, body_right_inner_line_y, body_right_inner_line_z])
    sorted_inner_right_line = inner_right_line.T[inner_right_line[2, :].argsort()].T
    outer_right_line = np.array([body_right_outer_line_x, body_right_outer_line_y, body_right_outer_line_z])
    sorted_outer_right_line = outer_right_line.T[outer_right_line[2, :].argsort()].T
    center_left_line = np.array([body_left_center_line_x, body_left_center_line_y, body_left_center_line_z])
    sorted_center_left_line = center_left_line.T[center_left_line[2, :].argsort()].T
    inner_left_line = np.array([body_left_inner_line_x, body_left_inner_line_y, body_left_inner_line_z])
    sorted_inner_left_line = inner_left_line.T[inner_left_line[2, :].argsort()].T
    outer_left_line = np.array([body_left_outer_line_x, body_left_outer_line_y, body_left_outer_line_z])
    sorted_outer_left_line = outer_left_line.T[outer_left_line[2, :].argsort()].T

    line_0 = np.array([array_for_arrow_tip[:, 0], sorted_array_outer_ring[:, 0], sorted_array_inner_ring[:, 0]])
    line_0 = np.concatenate([line_0, np.flip(sorted_inner_right_line, axis=-1).T])
    line_0 = np.append(line_0, sorted_array_end_ring[:, 2].reshape(1, 3), axis=0).T
    line_1 = np.array([array_for_arrow_tip[:, 1], sorted_array_outer_ring[:, 1], sorted_array_inner_ring[:, 1]])
    line_1 = np.concatenate([line_1, np.flip(sorted_center_right_line, axis=-1).T])
    line_1 = np.append(line_1, sorted_array_end_ring[:, 1].reshape(1, 3), axis=0).T
    line_2 = np.array([array_for_arrow_tip[:, 2], sorted_array_outer_ring[:, 2], sorted_array_inner_ring[:, 2]])
    line_2 = np.concatenate([line_2, np.flip(sorted_outer_right_line, axis=-1).T])
    line_2 = np.append(line_2, sorted_array_end_ring[:, 0].reshape(1, 3), axis=0).T
    line_3 = np.array([array_for_arrow_tip[:, 3], sorted_array_outer_ring[:, 3], sorted_array_inner_ring[:, 3]])
    line_3 = np.concatenate([line_3, np.flip(sorted_outer_left_line, axis=-1).T])
    line_3 = np.append(line_3, sorted_array_end_ring[:, 5].reshape(1, 3), axis=0).T
    line_4 = np.array([array_for_arrow_tip[:, 4], sorted_array_outer_ring[:, 4], sorted_array_inner_ring[:, 4]])
    line_4 = np.concatenate([line_4, np.flip(sorted_center_left_line, axis=-1).T])
    line_4 = np.append(line_4, sorted_array_end_ring[:, 4].reshape(1, 3), axis=0).T
    line_5 = np.array([array_for_arrow_tip[:, 5], sorted_array_outer_ring[:, 5], sorted_array_inner_ring[:, 5]])
    line_5 = np.concatenate([line_5, np.flip(sorted_inner_left_line, axis=-1).T])
    line_5 = np.append(line_5, sorted_array_end_ring[:, 3].reshape(1, 3), axis=0).T

    # rotational Transformation
    vector = np.array(pos_vec)
    rotation_matrix = bf.combine_rotation_matrixes(zeta, eta, theta)
    x, y, z = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), np.array([x, y, z])) * scalingfactor
    x = x + vector[0, None]
    y = y + vector[1, None]
    z = z + vector[2, None]
    array_for_arrow_tip = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), array_for_arrow_tip) * scalingfactor + vector[:, None]
    sorted_array_inner_ring = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), sorted_array_inner_ring) * scalingfactor + vector[:, None]
    sorted_array_outer_ring = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), sorted_array_outer_ring) * scalingfactor + vector[:, None]
    sorted_array_end_ring = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), sorted_array_end_ring) * scalingfactor + vector[:, None]
    line_0 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_0) * scalingfactor + vector[:, None]
    line_1 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_1) * scalingfactor + vector[:, None]
    line_2 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_2) * scalingfactor + vector[:, None]
    line_3 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_3) * scalingfactor + vector[:, None]
    line_4 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_4) * scalingfactor + vector[:, None]
    line_5 = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), line_5) * scalingfactor + vector[:, None]


    mesh3D_base_body_2 = go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K,
                                 color=bodycolor, opacity=0.50, showscale=False, visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_inner_ring_2 = go.Scatter3d(x=sorted_array_inner_ring[0, :], y=sorted_array_inner_ring[1, :],
                                       z=sorted_array_inner_ring[2, :],
                                       mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_outer_ring_2 = go.Scatter3d(x=sorted_array_outer_ring[0, :], y=sorted_array_outer_ring[1, :],
                                       z=sorted_array_outer_ring[2, :],
                                       mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_end_2 = go.Scatter3d(x=sorted_array_end_ring[0, :], y=sorted_array_end_ring[1, :],
                                z=sorted_array_end_ring[2, :],
                                mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_Tip = go.Scatter3d(x=array_for_arrow_tip[0, :], y=array_for_arrow_tip[1, :], z=array_for_arrow_tip[2, :],
                              mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_line_0 = go.Scatter3d(x=line_0[0, :], y=line_0[1, :], z=line_0[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_line_1 = go.Scatter3d(x=line_1[0, :], y=line_1[1, :], z=line_1[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_line_2 = go.Scatter3d(x=line_2[0, :], y=line_2[1, :], z=line_2[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_line_3 = go.Scatter3d(x=line_3[0, :], y=line_3[1, :], z=line_3[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_line_4 = go.Scatter3d(x=line_4[0, :], y=line_4[1, :], z=line_4[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))
    mesh3D_line_5 = go.Scatter3d(x=line_5[0, :], y=line_5[1, :], z=line_5[2, :], mode='lines',
                                    line=dict(color=line_color, width= ptly_linewidth), visible=True)#, hoverinfo='text', hovertext=hovertext_1, hoverlabel=dict(bgcolor=bodycolor, font_size=font_size))

    mesh3D_curved_arrow = [mesh3D_base_body_2, mesh3D_inner_ring_2, mesh3D_outer_ring_2, mesh3D_Tip, mesh3D_line_0,
                   mesh3D_line_1, mesh3D_line_2,
                   mesh3D_line_3, mesh3D_line_4, mesh3D_line_5, mesh3D_end_2]

    return mesh3D_curved_arrow