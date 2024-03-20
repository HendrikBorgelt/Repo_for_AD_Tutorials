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
test_2 = (np.array(x_1)*(max(x_0)-min(x_0)) + np.array(y_1)*(max(y_0)-min(y_0)) + np.array(z_1)*(max(z_0)-min(z_0)))/(max(x_0)-min(x_0)+max(y_0)-min(y_0)+max(z_0)-min(z_0))
test_3 = test_2
test_4 = (test_2 - min(test_2))/(max(test_2)-min(test_2))
lower_bound = 0.25
upper_bound = 0.9
test_5 = (np.array([min(max(i,lower_bound),upper_bound) for i in test_4])-lower_bound)/(upper_bound-lower_bound)
test = np.array([x_1, y_1, z_1])*255
mesh3D_base_body_1 = go.Mesh3d(x=x_0, y=y_0, z=z_0, i=i_0, j=j_0, k=k_0, intensity=test_5, colorscale='Turbo', showscale=False)

fig = go.Figure(data=mesh3D_base_body_1)
fig.update_layout(
    updatemenus=[
        dict(active=0, # camera
         buttons=list([
            dict(label="Reset", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.25, y=-1.25, z=1.25))}]),
            dict(label="links", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=0))}]),
            dict(label="links erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=1.7))}]),
            dict(label="rechts", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=0))}]),
            dict(label="rechts erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=1.5))}]),
            dict(label="Vogelperspektive", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=0, z=2.2), up=dict(x=0, y=-1, z=0),)}]),
            dict(label="Rückseitig", method="relayout",  args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=0))}]),
            dict(label="Rückseitig erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=1.7))}]),
            dict(label="Frontal", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=0))}]),
            dict(label="Frontal erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=1.7))}]),]),
         direction="down", pad={"r": 0, "t": 0}, showactive=True, x=-0.05, xanchor="left", y=1.22, yanchor="top", font=dict(size=10))
    ],
    scene=dict(
        xaxis=dict(nticks=20, range=[400, 1800], autorange=False), yaxis=dict(nticks=20, range=[-500, 1200], autorange=False), zaxis=dict(nticks=15, range=[-700, 700], autorange=False),
        aspectmode='manual', xaxis_title='Y Achse', yaxis_title='X Achse', zaxis_title='Z Achse', aspectratio=dict(x=1, y=1, z=0.8),
        ),
    showlegend=False,
    scene_camera=dict(eye=dict(x=-1.25, y=-1.25, z=1.25)),
    annotations=[
        dict(text=""
                  "<br>"
                  "<br> "
                  "<br> Kamera                         "
                  "<br> "
                  "<br> "
                  "<br> ", x=-0.18, y=1.23, showarrow=False, font=dict(size=10)),
    ],
    width=600,
    height=600,
    minreducedwidth=550,
    minreducedheight=600,
    autosize=True,
)
fig.show()
fig.write_html("./FEM_an_Korbbogenboden_ohne_Dropdown_fuer_Smartphone.html", include_plotlyjs='cdn', include_mathjax='cdn')
fig.update_layout(
    updatemenus=[
        dict(active=0, # camera
         buttons=list([
            dict(label="Reset", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.25, y=-1.25, z=1.25))}]),
            dict(label="links", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=0))}]),
            dict(label="links erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=1.7))}]),
            dict(label="rechts", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=0))}]),
            dict(label="rechts erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=1.5))}]),
            dict(label="Vogelperspektive", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=0, z=2.2), up=dict(x=0, y=-1, z=0),)}]),
            dict(label="Rückseitig", method="relayout",  args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=0))}]),
            dict(label="Rückseitig erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=1.7))}]),
            dict(label="Frontal", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=0))}]),
            dict(label="Frontal erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=1.7))}]),]),
         direction="down", pad={"r": 0, "t": 0}, showactive=True, x=0.33, xanchor="left", y=1.22, yanchor="top", font=dict(size=10))
    ],
    scene=dict(
        xaxis=dict(nticks=20, range=[400, 1800], autorange=False), yaxis=dict(nticks=20, range=[-500, 1200], autorange=False), zaxis=dict(nticks=15, range=[-700, 700], autorange=False),
        aspectmode='manual', xaxis_title='Y Achse', yaxis_title='X Achse', zaxis_title='Z Achse', aspectratio=dict(x=1, y=1, z=0.8),
        ),
    showlegend=False,
    scene_camera=dict(eye=dict(x=-1.25, y=-1.25, z=1.25)),
    annotations=[
        dict(text=""
                  "<br>"
                  "<br> "
                  "<br> Kamera                         "
                  "<br> "
                  "<br> "
                  "<br> ", x=0.28, y=1.23, showarrow=False, font=dict(size=10)),
    ],
    width=1400,
    height=900,
    minreducedwidth=550,
    minreducedheight=600,
    autosize=True,
)
fig.show()
fig.write_html("./FEM_an_Korbbogenboden_ohne_Dropdown_fuer_FullScreen.html", include_plotlyjs='cdn', include_mathjax='cdn')
fig.update_layout(
    updatemenus=[
        dict(active=0, # camera
         buttons=list([
            dict(label="Reset", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.25, y=-1.25, z=1.25))}]),
            dict(label="links", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=0))}]),
            dict(label="links erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=1.7, y=0, z=1.7))}]),
            dict(label="rechts", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=0))}]),
            dict(label="rechts erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=-1.7, y=0, z=1.5))}]),
            dict(label="Vogelperspektive", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=0, z=2.2), up=dict(x=0, y=-1, z=0),)}]),
            dict(label="Rückseitig", method="relayout",  args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=0))}]),
            dict(label="Rückseitig erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=1.7, z=1.7))}]),
            dict(label="Frontal", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=0))}]),
            dict(label="Frontal erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=1.7))}]),]),
         direction="down", pad={"r": 0, "t": 0}, showactive=True, x=0.33, xanchor="left", y=1.22, yanchor="top", font=dict(size=10))
    ],
    scene=dict(
        xaxis=dict(nticks=20, range=[400, 1800], autorange=False), yaxis=dict(nticks=20, range=[-500, 1200], autorange=False), zaxis=dict(nticks=15, range=[-700, 700], autorange=False),
        aspectmode='manual', xaxis_title='Y Achse', yaxis_title='X Achse', zaxis_title='Z Achse', aspectratio=dict(x=1, y=1, z=0.8),
        ),
    showlegend=False,
    scene_camera=dict(eye=dict(x=-1.25, y=-1.25, z=1.25)),
    annotations=[
        dict(text=""
                  "<br>"
                  "<br> "
                  "<br> Kamera                         "
                  "<br> "
                  "<br> "
                  "<br> ", x=0.28, y=1.23, showarrow=False, font=dict(size=10)),
    ],
    width=1800,
    height=900,
    minreducedwidth=550,
    minreducedheight=600,
    autosize=True,
)
fig.show()
fig.write_html("./FEM_an_Korbbogenboden_ohne_Dropdown_fuer_PupUp.html", include_plotlyjs='cdn', include_mathjax='cdn')



