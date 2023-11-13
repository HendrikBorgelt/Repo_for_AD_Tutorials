import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd

import numpy
from stl import mesh
# fig.add_trace( ... )
# fig.update_layout( ... )
import pywavefront
import copy
import BasisFunktionen as bf


def create_mesh3d_for_dif_element(mesh_differential_element, scalingfactor, pos_vec, zeta, eta, theta,
                                  plty_linewidth=2, line_color='black', bodycolor='lightgray', frame=True, font_size=16):
    vertices, I, J, K = bf.stl2mesh3d(mesh_differential_element)
    x, y, z = vertices.T
    colorscale = [[0, '#e5dee5'], [1, '#e5dee5']]

    # rotational transformation
    alpha = 0
    beta = 0
    gamma = 0
    rotation_matrix = bf.combine_rotation_matrixes(alpha, beta, gamma)
    vertices = np.dot(vertices, rotation_matrix)

    x_front_curve, y_front_curve, z_front_curve = [], [], []
    x_back_curve, y_back_curve, z_back_curve = [], [], []
    for x_1, x_2, x_3 in zip(x, y, z):
        if x_3 == 0:
            if x_2 <= 110:
                x_front_curve.append(x_1)
                y_front_curve.append(x_2)
                z_front_curve.append(x_3)
            else:
                x_back_curve.append(x_1)
                y_back_curve.append(x_2)
                z_back_curve.append(x_3)

    Corners = {'lfr': [max(x_front_curve), min(y_front_curve), 0],   # lower_front_right := lfr
               'lfl': [min(x_front_curve), min(y_front_curve), 0],   # lower_front_left := lfl
               'lbr': [max(x_back_curve), min(y_back_curve), 0],     # lower_back_right := lbr
               'lbl': [min(x_back_curve), min(y_back_curve), 0],     # lower_back_left := lbl
               'ufr': [max(x_front_curve), min(y_front_curve), 50],  # upper_front_right := ufr
               'ufl': [min(x_front_curve), min(y_front_curve), 50],  # upper_front_left := ufl
               'ubr': [max(x_back_curve), min(y_back_curve), 50],    # upper_back_right := ubr
               'ubl': [min(x_back_curve), min(y_back_curve), 50]     # upper_back_left := ubl
               }
    lower_fornt_curve = np.array([x_front_curve, y_front_curve, z_front_curve])
    lower_back_curve = np.array([x_back_curve, y_back_curve, z_back_curve])
    upper_front_curve = np.array([x_front_curve, y_front_curve, [i_1 + 50 for i_1 in z_front_curve]])
    upper_back_curve = np.array([x_back_curve, y_back_curve, [i_1 + 50 for i_1 in z_back_curve]])
    body_front_left = np.array([[Corners['lfl'][0], Corners['ufl'][0]], [Corners['lfl'][1], Corners['ufl'][1]],
                                [Corners['lfl'][2], Corners['ufl'][2]]])
    body_front_right = np.array([[Corners['lfr'][0], Corners['ufr'][0]], [Corners['lfr'][1], Corners['ufr'][1]],
                                    [Corners['lfr'][2], Corners['ufr'][2]]])
    body_back_left = np.array([[Corners['lbl'][0], Corners['ubl'][0]], [Corners['lbl'][1], Corners['ubl'][1]],
                                [Corners['lbl'][2], Corners['ubl'][2]]])
    body_back_right = np.array([[Corners['lbr'][0], Corners['ubr'][0]], [Corners['lbr'][1], Corners['ubr'][1]],
                                [Corners['lbr'][2], Corners['ubr'][2]]])
    body_upper_right = np.array([[Corners['ufl'][0], Corners['ubl'][0]], [Corners['ufl'][1], Corners['ubl'][1]],
                                [Corners['ufl'][2], Corners['ubl'][2]]])
    body_upper_left = np.array([[Corners['ufr'][0], Corners['ubr'][0]], [Corners['ufr'][1], Corners['ubr'][1]],
                                [Corners['ufr'][2], Corners['ubr'][2]]])
    body_lower_right = np.array([[Corners['lfl'][0], Corners['lbl'][0]], [Corners['lfl'][1], Corners['lbl'][1]],
                                [Corners['lfl'][2], Corners['lbl'][2]]])
    body_lower_left = np.array([[Corners['lfr'][0], Corners['lbr'][0]], [Corners['lfr'][1], Corners['lbr'][1]],
                                [Corners['lfr'][2], Corners['lbr'][2]]])


    # displacement of origin
    origin_vector = np.array([0, -125, -25])
    x = x + origin_vector[0, None]
    y = y + origin_vector[1, None]
    z = z + origin_vector[2, None]
    lower_fornt_curve = lower_fornt_curve + origin_vector[:, None]
    lower_back_curve = lower_back_curve + origin_vector[:, None]
    upper_front_curve = upper_front_curve + origin_vector[:, None]
    upper_back_curve = upper_back_curve + origin_vector[:, None]
    body_front_left = body_front_left + origin_vector[:, None]
    body_front_right = body_front_right + origin_vector[:, None]
    body_back_left = body_back_left + origin_vector[:, None]
    body_back_right = body_back_right + origin_vector[:, None]
    body_upper_right = body_upper_right + origin_vector[:, None]
    body_upper_left = body_upper_left + origin_vector[:, None]
    body_lower_right = body_lower_right + origin_vector[:, None]
    body_lower_left = body_lower_left + origin_vector[:, None]


    # rotational Transformation
    vector = np.array(pos_vec)
    rotation_matrix = bf.combine_rotation_matrixes(zeta, eta, theta)
    x, y, z = np.dot(bf.combine_rotation_matrixes(zeta, eta, theta), np.array([x, y, z])) * scalingfactor
    x = x + vector[0, None]
    y = y + vector[1, None]
    z = z + vector[2, None]
    lower_fornt_curve = np.dot(rotation_matrix, lower_fornt_curve) * scalingfactor + vector[:, None]
    lower_back_curve = np.dot(rotation_matrix, lower_back_curve) * scalingfactor + vector[:, None]
    upper_front_curve = np.dot(rotation_matrix, upper_front_curve) * scalingfactor + vector[:, None]
    upper_back_curve = np.dot(rotation_matrix, upper_back_curve) * scalingfactor + vector[:, None]
    body_front_left = np.dot(rotation_matrix, body_front_left) * scalingfactor + vector[:, None]
    body_front_right = np.dot(rotation_matrix, body_front_right) * scalingfactor + vector[:, None]
    body_back_left = np.dot(rotation_matrix, body_back_left) * scalingfactor + vector[:, None]
    body_back_right = np.dot(rotation_matrix, body_back_right) * scalingfactor + vector[:, None]
    body_upper_right = np.dot(rotation_matrix, body_upper_right) * scalingfactor + vector[:, None]
    body_upper_left = np.dot(rotation_matrix, body_upper_left) * scalingfactor + vector[:, None]
    body_lower_right = np.dot(rotation_matrix, body_lower_right) * scalingfactor + vector[:, None]
    body_lower_left = np.dot(rotation_matrix, body_lower_left) * scalingfactor + vector[:, None]


    mesh3D_base_body_1 = go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K,
                                 color=bodycolor, opacity=0.50, showscale=False, visible=True, hoverinfo='text', hovertext='Differential element', hoverlabel=dict(font_size=font_size), contour=dict(show=True, width=16))
    mesh3D_body_lower_front_curve = go.Scatter3d(x=lower_fornt_curve[0, :], y=lower_fornt_curve[1, :], z=lower_fornt_curve[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_body_lower_back_curve = go.Scatter3d(x=lower_back_curve[0, :], y=lower_back_curve[1, :], z=lower_back_curve[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_body_upper_front_curve = go.Scatter3d(x=upper_front_curve[0, :], y=upper_front_curve[1, :], z=upper_front_curve[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3D_body_upper_back_curve = go.Scatter3d(x=upper_back_curve[0, :], y=upper_back_curve[1, :], z=upper_back_curve[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_body_front_left = go.Scatter3d(x=body_front_left[0, :], y=body_front_left[1, :], z=body_front_left[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_body_front_right = go.Scatter3d(x=body_front_right[0, :], y=body_front_right[1, :], z=body_front_right[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_body_back_left = go.Scatter3d(x=body_back_left[0, :], y=body_back_left[1, :], z=body_back_left[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_body_back_right = go.Scatter3d(x=body_back_right[0, :], y=body_back_right[1, :], z=body_back_right[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_body_upper_right = go.Scatter3d(x=body_upper_right[0, :], y=body_upper_right[1, :], z=body_upper_right[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_body_upper_left = go.Scatter3d(x=body_upper_left[0, :], y=body_upper_left[1, :], z=body_upper_left[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_body_lower_right = go.Scatter3d(x=body_lower_right[0, :], y=body_lower_right[1, :], z=body_lower_right[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))
    mesh3d_body_lower_left = go.Scatter3d(x=body_lower_left[0, :], y=body_lower_left[1, :], z=body_lower_left[2, :],
                                mode='lines', line=dict(color=line_color, width=plty_linewidth), visible=True, hoverinfo='none', hoverlabel=dict(font_size=font_size))

    # mesh3D_body_lower_front_curve = go.Scatter3d(x=x_front_curve, y=y_front_curve, z=z_front_curve, mode='lines',
    #                                              line=dict(color=line_color, width=plty_linewidth))
    # mesh3D_body_lower_back_curve = go.Scatter3d(x=x_back_curve, y=y_back_curve, z=z_back_curve, mode='lines',
    #                                             line=dict(color=line_color, width=plty_linewidth))
    # mesh3D_body_upper_front_curve = go.Scatter3d(x=x_front_curve, y=y_front_curve, z=[(i_1 + 50) for i_1 in z_front_curve],
    #                                              mode='lines', line=dict(color=line_color, width=plty_linewidth))
    # mesh3D_body_upper_back_curve = go.Scatter3d(x=x_back_curve, y=y_back_curve, z=[(i_1 + 50) for i_1 in z_back_curve],
    #                                             mode='lines', line=dict(color=line_color, width=plty_linewidth))
    #
    # mesh3d_body_front_left = go.Scatter3d(x=[Corners['lfl'][0], Corners['ufl'][0]], y=[Corners['lfl'][1], Corners['ufl'][1]],
    #                                         z=[Corners['lfl'][2], Corners['ufl'][2]], mode='lines',
    #                                         line=dict(color=line_color, width=plty_linewidth))
    # mesh3d_body_front_right = go.Scatter3d(x=[Corners['lfr'][0], Corners['ufr'][0]], y=[Corners['lfr'][1], Corners['ufr'][1]],
    #                                         z=[Corners['lfr'][2], Corners['ufr'][2]], mode='lines',
    #                                         line=dict(color=line_color, width=plty_linewidth))
    # mesh3d_body_back_left = go.Scatter3d(x=[Corners['lbl'][0], Corners['ubl'][0]], y=[Corners['lbl'][1], Corners['ubl'][1]],
    #                                         z=[Corners['lbl'][2], Corners['ubl'][2]], mode='lines',
    #                                         line=dict(color=line_color, width=plty_linewidth))
    # mesh3d_body_back_right = go.Scatter3d(x=[Corners['lbr'][0], Corners['ubr'][0]], y=[Corners['lbr'][1], Corners['ubr'][1]],
    #                                         z=[Corners['lbr'][2], Corners['ubr'][2]], mode='lines',
    #                                         line=dict(color=line_color, width=plty_linewidth))
    # mesh3d_body_upper_right = go.Scatter3d(x=[Corners['ufl'][0], Corners['ubl'][0]], y=[Corners['ufl'][1], Corners['ubl'][1]],
    #                                         z=[Corners['ufl'][2], Corners['ubl'][2]], mode='lines',
    #                                         line=dict(color=line_color, width=plty_linewidth))
    # mesh3d_body_upper_left = go.Scatter3d(x=[Corners['ufr'][0], Corners['ubr'][0]], y=[Corners['ufr'][1], Corners['ubr'][1]],
    #                                         z=[Corners['ufr'][2], Corners['ubr'][2]], mode='lines',
    #                                         line=dict(color=line_color, width=plty_linewidth))
    # mesh3d_body_lower_right = go.Scatter3d(x=[Corners['lfl'][0], Corners['lbl'][0]], y=[Corners['lfl'][1], Corners['lbl'][1]],
    #                                         z=[Corners['lfl'][2], Corners['lbl'][2]], mode='lines',
    #                                         line=dict(color=line_color, width=plty_linewidth))
    # mesh3d_body_lower_left = go.Scatter3d(x=[Corners['lfr'][0], Corners['lbr'][0]], y=[Corners['lfr'][1], Corners['lbr'][1]],
    #                                         z=[Corners['lfr'][2], Corners['lbr'][2]], mode='lines',
    #                                         line=dict(color=line_color, width=plty_linewidth))

    if frame:
        mesh3D_Differential_element = [mesh3D_base_body_1,
                                       mesh3D_body_lower_front_curve,
                                       mesh3D_body_lower_back_curve,
                                       mesh3D_body_upper_front_curve,
                                       mesh3D_body_upper_back_curve,
                                       mesh3d_body_front_left,
                                       mesh3d_body_front_right,
                                       mesh3d_body_back_left,
                                       mesh3d_body_back_right,
                                       mesh3d_body_upper_left,
                                       mesh3d_body_upper_right,
                                       mesh3d_body_lower_left,
                                       mesh3d_body_lower_right,
                                       ]
    else:
        mesh3D_Differential_element = [mesh3D_body_lower_front_curve,
                                       mesh3D_body_lower_back_curve,
                                       mesh3D_body_upper_front_curve,
                                       mesh3D_body_upper_back_curve,
                                       mesh3d_body_front_left,
                                       mesh3d_body_front_right,
                                       mesh3d_body_back_left,
                                       mesh3d_body_back_right,
                                       mesh3d_body_upper_left,
                                       mesh3d_body_upper_right,
                                       mesh3d_body_lower_left,
                                       mesh3d_body_lower_right,
                                       ]
    return mesh3D_Differential_element
