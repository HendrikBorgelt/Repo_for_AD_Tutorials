import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import pandas as pd

import numpy
from stl import mesh
# fig.add_trace( ... )
# fig.update_layout( ... )
import pywavefront

def stl2mesh3d(stl_mesh):
    # stl_mesh is read by nympy-stl from a stl file; it is  an array of faces/triangles (i.e. three 3d points)
    # this function extracts the unique vertices and the lists I, J, K to define a Plotly mesh3d
    p, q, r = stl_mesh.vectors.shape #(p, 3, 3)
    # the array stl_mesh.vectors.reshape(p*q, r) can contain multiple copies of the same vertex;
    # extract unique vertices from all mesh triangles
    vertices_2, ixr = np.unique(stl_mesh.vectors.reshape(p*q, r), return_inverse=True, axis=0)
    I = np.take(ixr, [3*k for k in range(p)])
    J = np.take(ixr, [3*k+1 for k in range(p)])
    K = np.take(ixr, [3*k+2 for k in range(p)])
    return vertices_2, I, J, K

# def obj_data_to_mesh3d(odata):
#     # odata is the string read from an obj file
#     vertices_1 = []
#     faces_1 = []
#     lines = odata.splitlines()
#
#     for line in lines:
#         slist = line.split()
#         if slist:
#             if slist[0] == 'v':
#                 vertex = np.array(slist[1:], dtype=float)
#                 vertices_1.append(vertex)
#             elif slist[0] == 'f':
#                 face_1 = []
#                 for k in range(1, len(slist)):
#                     face_1.append([int(s) for s in slist[k].replace('//','/').split('/')])
#                 if len(face_1) > 3: # triangulate the n-polyonal face, n>3
#                     faces_1.extend([[face_1[0][0]-1, face_1[k][0]-1, face_1[k+1][0]-1] for k in range(1, len(face)-1)])
#                 else:
#                     faces_1.append([face_1[j][0]-1 for j in range(len(face_1))])
#             else: pass
#
#
#     return np.array(vertices_1), np.array(faces_1)
#
#
# scene = pywavefront.Wavefront('D:/Users/smhhborg(D_Laufwerk)/Documents/GitHub/Repo_for_AD_Tutorials/meshes/Differentielles_Element.obj', collect_faces=True)

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
fig.show()
