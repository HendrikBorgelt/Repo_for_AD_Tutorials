import meshio
from stl import mesh
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import re

# mesh_1 = meshio.read(
#     'D:/Users/smhhborg(D_Laufwerk)/Documents/GitHub/Repo_for_AD_Tutorials/meshes/test_with_colors.vtk',  # string, os.PathLike, or a buffer/open file
    # file_format="stl",  # optional if filename is a path; inferred from extension
    # see meshio-convert -h for all possible formats
# )

# mesh_differential_element_1 = mesh.Mesh.from_file('D:/Users/smhhborg(D_Laufwerk)/Documents/GitHub/Repo_for_AD_Tutorials/meshes/Pfeil.stl')
# mesh_new = mesh.Mesh.from_file('D:/Users/smhhborg(D_Laufwerk)/Documents/GitHub/Repo_for_AD_Tutorials/meshes/test_with_colors.stl')
# p, q, r = mesh_new.vectors.shape #(p, 3, 3)
# vertices_2, ixr = np.unique(mesh_new.vectors.reshape(p*q, r), return_inverse=True, axis=0)
# I = np.take(ixr, [3*k for k in range(p)])
# J = np.take(ixr, [3*k+1 for k in range(p)])
# K = np.take(ixr, [3*k+2 for k in range(p)])
#
# x, y, z = vertices_2.T
#
# x_1 , y_1, z_1 = mesh_1.points.T
#
# test_vertices, test_ixr = np.unique(mesh_1.points, return_inverse=True, axis=0)
# # I_2 = np.take(test_ixr, [3*k_1 for k_1 in range(244759)])
# # J_2 = np.take(test_ixr, [3*k_1+1 for k_1 in range(244759)])
# # K_2 = np.take(test_ixr, [3*k_1+2 for k_1 in range(244759)])
#
# # mesh3D_base_body_1 = go.Mesh3d(x=x_1, y=y_1, z=z_1)
# mesh3D_base_body_1 = go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K)
# fig = go.Figure(data=mesh3D_base_body_1)
# fig.show()

check_for_cord = True
check_for_color = True
check_for_cord_index = True
holder_1 = []
holder_2 = []
holder_3 = []
with open('D:/Users/smhhborg(D_Laufwerk)/Documents/GitHub/Repo_for_AD_Tutorials/meshes/test.vrml', 'r') as data:
    for lines in data:
        if check_for_cord:
            if re.search("coord DEF VTKcoordinates Coordinate", lines):
                check_for_cord = False
        elif check_for_color & (not check_for_cord):
            if re.search("color DEF VTKcolors Color", lines):
                check_for_color = False
            # a = re.findall("[-0-9]{1,5}[.][0-9]{10}", lines)
            a = re.findall("[-0-9.]{1,30}[e]{0,1}[-0-9]{0,3}", lines)
            if len(a) == 3:
                holder_1.append(map(float, a))
        elif (not check_for_color) & (not check_for_cord) & check_for_cord_index:
            if re.search("coordIndex", lines):
                check_for_cord_index = False
            # b = re.findall("[-0-9]{1,5}.[0-9]{9}", lines)
            b = re.findall("[-0-9.]{1,30}[e]{0,1}[-0-9]{0,3}", lines)
            if len(b) == 3:
                holder_2.append(map(float, b))
        else:
            c = re.findall("[-0-9.]{1,30}[e]{0,1}[-0-9]{0,3}", lines)
            if len(c) == 4:
                holder_3.append(map(float, c))


holder_array_1 = np.array(holder_1)
holder_array_2 = np.array(holder_2)
#
x_0, y_0, z_0 = zip(*holder_1)
x_1, y_1, z_1 = zip(*holder_2)
i_0, j_0, k_0, l_0 = zip(*holder_3)
#
test = np.array([x_1, y_1,z_1])*255
mesh3D_base_body_1 = go.Mesh3d(x=x_0, y=y_0, z=z_0, i=i_0, j=j_0, k=k_0, vertexcolor=test.T)
fig = go.Figure(data=mesh3D_base_body_1)
fig.show()

