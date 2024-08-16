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

a_0 = [0, -75.04613, 64.22221]
a_1 = [0, -73.66031, 63.64819]
b_0 = [0, -70.71068, 70.71068]
b_1 = [0, -69.65002, 69.65002]
c_0 = [6.540701, -74.76056, 64.22221]
c_1 = [6.419919, -73.38001, 63.64819]
d_0 = [6.162842, -70.4416, 70.71068]
d_1 = [6.070399, -69.38498, 69.65002]
f_xyz = [(a_0[0] + b_0[0] + c_0[0] + d_0[0])/4, (a_0[1] + b_0[1] + c_0[1] + d_0[1])/4, (a_0[2] + b_0[2] + c_0[2] + d_0[2])/4]
b_xyz = [(a_1[0] + b_1[0] + c_1[0] + d_1[0])/4, (a_1[1] + b_1[1] + c_1[1] + d_1[1])/4, (a_1[2] + b_1[2] + c_1[2] + d_1[2])/4]
m_xyz = [(f_xyz[0] + b_xyz[0])/2, (f_xyz[1] + b_xyz[1])/2, (f_xyz[2] + b_xyz[2])/2]
r_xyz = [(c_0[0] + c_1[0] + d_0[0] + d_1[0])/4, (c_0[1] + c_1[1] + d_0[1] + d_1[1])/4, (c_0[2] + c_1[2] + d_0[2] + d_1[2])/4]
l_xyz = [(a_0[0] + a_1[0] + b_0[0] + b_1[0])/4, (a_0[1] + a_1[1] + b_0[1] + b_1[1])/4, (a_0[2] + a_1[2] + b_0[2] + b_1[2])/4]
d_xyz = [(a_0[0] + a_1[0] + c_0[0] + c_1[0])/4, (a_0[1] + a_1[1] + c_0[1] + c_1[1])/4, (a_0[2] + a_1[2] + c_0[2] + c_1[2])/4]
u_xyz = [(b_0[0] + b_1[0] + d_0[0] + d_1[0])/4, (b_0[1] + b_1[1] + d_0[1] + d_1[1])/4, (b_0[2] + b_1[2] + d_0[2] + d_1[2])/4]
shift_factor = 6
f_xyz_1 = np.array(m_xyz) + np.array([0.014, -0.25*np.cos(37.5/180), np.sin(37.5/180)])*shift_factor
b_xyz_1 = np.array(m_xyz) + np.array([-0.014, 0.20*np.cos(37.5/180), -0.6*np.sin(37.5/180)])*shift_factor
#3.109954  3.188511
#

mesh_differential_torus_element = mesh.Mesh.from_file('./meshes/Differentielles_Element_eines_Torus.stl')
mesh_torus_segment = mesh.Mesh.from_file('./meshes/Torussegment.stl')
mesh_hollow_torus = mesh.Mesh.from_file('./meshes/Hohl_Torus.stl')
mesh_half_tank_shell = mesh.Mesh.from_file('./meshes/Halber_Boden.stl')
mesh_half_torus_element = mesh.Mesh.from_file('./meshes/Halber_Torus.stl')
mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Pfeil.stl')
mesh_curved_arrow_1 = mesh.Mesh.from_file('./meshes/Momentenpfeil.stl')

mesh3D_Differential_element_1 = fge.create_mesh3d_for_torus_element([mesh_differential_torus_element, mesh_torus_segment,
                                                                    mesh_hollow_torus, mesh_half_tank_shell,
                                                                    mesh_half_torus_element],
                                                                   1, [0, 0, 0], 0, 0, 0, [])
mesh3D_Arrow_1 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.05, f_xyz_1, -np.pi*37.5/180,
                                            0, np.pi*2.5/180, '<i>F<sub>rz </sub> r d&#966; </i>')
mesh3D_Arrow_2 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.05, b_xyz_1, -np.pi*217.5/180,
                                            0, -np.pi*2.5/180, '<i>F<sub>rz </sub> r d&#966; </i>')
mesh3D_Arrow_3 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.05, l_xyz, 0,
                                            0, np.pi*270/180, '<i>F<sub>rz </sub> r d&#966; </i>')
mesh3D_Arrow_4 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.05, r_xyz, 0,
                                            0, np.pi*95/180, '<i>F<sub>rz </sub> r d&#966; </i>')
mesh3D_Arrow_5 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.05, u_xyz, -np.pi*135/180,
                                            0, np.pi*0/180, '<i>F<sub>rz </sub> r d&#966; </i>')
mesh3D_Arrow_6 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.05, d_xyz, -np.pi*-60/180,
                                            0, np.pi*0/180, '<i>F<sub>rz </sub> r d&#966; </i>')

mesh3D_Curved_Arrow_1 = fm.create_mesh3d_for_curved_arrow(mesh_curved_arrow_1, 0.5, [0, -50, 0],
                                                          0, 0, 0, '<i>M<sub>r </sub>&#8729;r dr</i>')
# [0, -75.04613, 64.22221]  [0, -73.66031, 63.64819]
# [0, -70.71068, 70.71068]  [0, -69.65002, 69.65002]
# [6.540701, -74.76056, 64.22221]  [6.419919, -73.38001, 63.64819]
# [6.162842, -704416, 70.71068]  [6.070399, -69.38498, 69.65002]

mesh3D_Differential_element_1.extend(mesh3D_Arrow_1)
mesh3D_Differential_element_1.extend(mesh3D_Arrow_2)
mesh3D_Differential_element_1.extend(mesh3D_Arrow_3)
mesh3D_Differential_element_1.extend(mesh3D_Arrow_4)
mesh3D_Differential_element_1.extend(mesh3D_Arrow_5)
mesh3D_Differential_element_1.extend(mesh3D_Arrow_6)
fig = go.Figure(data=mesh3D_Differential_element_1)
fig.update_layout(updatemenus=[
    dict(
            active=0,
            # type="buttons",
            buttons=list([
                dict(label="Tank", method="update", args=[
                    {"visible": [False]*30+[True]*10+[False]*4+[True]*1+[False]*67}, {"scene.annotations": []}]),
                dict(label="Tank mit Torus", method="update", args=[
                    {"visible": [False]*30+[True]*16+[False]*66},{"scene.annotations": []}]),
                dict(label="Torurs", method="update", args=[
                    {"visible": [False]*40+[True]*4+[False]*1+[True]*1+[False]*66}, {"scene.annotations": []}]),
                dict(label="Torus mit Seg u dif Elem", method="update", args=[
                    {"visible": [True]*30+[False]*10+[True]*4+[False]*1+[True]*1+[False]*66}, {"scene.annotations": []}]),
                dict(label="Alle geometrischen Aspekte ohne Kräfte", method="update",
                     args=[{"visible": [True]*46+[False]*66}, {"scene.annotations": []}, ]),
                dict(label="Nur Dif Elem", method="update",
                     args=[{"visible": [True]*13+[False]*99}, {"scene.annotations": []}]),
                # dict(label="Alle geometrischen Aspekte", method="update",
                #      args=[{"visible": [True] * 112}, {"scene.annotations": []}, ]),
                # dict(label="Nur Dif Elem", method="update",
                #      args=[{"visible": [True]*13+[False]*33+[True]*66}, {"scene.annotations": []}]),
            ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=-0.19, xanchor="left",
            y=1.0, yanchor="top", font=dict(size=8)),
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
        xaxis=dict(nticks=20, range=[-80, 80], autorange=False), yaxis=dict(nticks=20, range=[-80, 80], autorange=False), zaxis=dict(nticks=15, range=[0, 160], autorange=False),
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
        dict(text=""
                  "<br>"
                  "<br> "
                  "<br> Geometrischer Aspekt                 "
                  "<br> "
                  "<br> "
                  "<br> ", x=-0.18, y=1.11, showarrow=False, font=dict(size=10)),

    ],
    width=600,
    height=600,
    minreducedwidth=550,
    minreducedheight=600,
    autosize=True,
)
fig.show()
fig.write_html("./Gewoelbtes_Element_und_Dropdown_fuer_Smartphone.html", include_plotlyjs='cdn', include_mathjax='cdn')

fig.update_layout(updatemenus=[
    dict(
            active=0,
            # type="buttons",
            buttons=list([
                dict(label="Tank", method="update", args=[
                    {"visible": [False]*30+[True]*10+[False]*4+[True]*1+[False]*67}, {"scene.annotations": []}]),
                dict(label="Tank mit Torus", method="update", args=[
                    {"visible": [False]*30+[True]*16+[False]*66},{"scene.annotations": []}]),
                dict(label="Torus", method="update", args=[
                    {"visible": [False]*40+[True]*4+[False]*1+[True]*1+[False]*66}, {"scene.annotations": []}]),
                dict(label="Torus mit Seg u dif Elem", method="update", args=[
                    {"visible": [True]*30+[False]*10+[True]*4+[False]*1+[True]*1+[False]*66}, {"scene.annotations": []}]),
                dict(label="Alle geometrischen Aspekte ohne Kräfte", method="update",
                     args=[{"visible": [True]*46+[False]*66}, {"scene.annotations": []}, ]),
                dict(label="Nur Dif Elem", method="update",
                     args=[{"visible": [True]*13+[False]*99}, {"scene.annotations": []}]),
                # dict(label="Alle geometrischen Aspekte", method="update",
                #      args=[{"visible": [True] * 112}, {"scene.annotations": []}, ]),
                # dict(label="Nur Dif Elem", method="update",
                #      args=[{"visible": [True]*13+[False]*33+[True]*66}, {"scene.annotations": []}]),
            ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.28, xanchor="left",
            y=1.130, yanchor="top", font=dict(size=10)),
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
        xaxis=dict(nticks=20, range=[-80, 80], autorange=False), yaxis=dict(nticks=20, range=[-80, 80], autorange=False), zaxis=dict(nticks=15, range=[0, 160], autorange=False),
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
        dict(text=""
                  "<br>"
                  "<br> "
                  "<br> Geometrischer Aspekt                 "
                  "<br> "
                  "<br> "
                  "<br> ", x=0.28, y=1.175, showarrow=False, font=dict(size=10)),

    ],
    width=1400,
    height=900,
    minreducedwidth=550,
    minreducedheight=600,
    autosize=True,
)
fig.show()
fig.write_html("./Gewoelbtes_Element_und_Dropdown_fuer_FullScreen.html", include_plotlyjs='cdn', include_mathjax='cdn')

fig.update_layout(updatemenus=[
    dict(
            active=0,
            # type="buttons",
            buttons=list([
                dict(label="Tank", method="update", args=[
                    {"visible": [False]*30+[True]*10+[False]*4+[True]*1+[False]*67}, {"scene.annotations": []}]),
                dict(label="Tank mit Torus", method="update", args=[
                    {"visible": [False]*30+[True]*16+[False]*66},{"scene.annotations": []}]),
                dict(label="Tours", method="update", args=[
                    {"visible": [False]*40+[True]*4+[False]*1+[True]*1+[False]*66}, {"scene.annotations": []}]),
                dict(label="Tours mit Seg u dif Elem", method="update", args=[
                    {"visible": [True]*30+[False]*10+[True]*4+[False]*1+[True]*1+[False]*66}, {"scene.annotations": []}]),
                dict(label="Alle geometrischen Aspekte ohne Kräfte", method="update",
                     args=[{"visible": [True]*46+[False]*66}, {"scene.annotations": []}, ]),
                dict(label="Nur Dif Elem", method="update",
                     args=[{"visible": [True]*13+[False]*99}, {"scene.annotations": []}]),
                # dict(label="Alle geometrischen Aspekte", method="update",
                #      args=[{"visible": [True] * 112}, {"scene.annotations": []}, ]),
                # dict(label="Nur Dif Elem", method="update",
                #      args=[{"visible": [True]*13+[False]*33+[True]*66}, {"scene.annotations": []}]),
            ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.28, xanchor="left",
            y=1.130, yanchor="top", font=dict(size=10)),
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
        xaxis=dict(nticks=20, range=[-80, 80], autorange=False), yaxis=dict(nticks=20, range=[-80, 80], autorange=False), zaxis=dict(nticks=15, range=[0, 160], autorange=False),
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
        dict(text=""
                  "<br>"
                  "<br> "
                  "<br> Geometrischer Aspekt                 "
                  "<br> "
                  "<br> "
                  "<br> ", x=0.28, y=1.175, showarrow=False, font=dict(size=10)),

    ],
    width=1800,
    height=900,
    minreducedwidth=550,
    minreducedheight=600,
    autosize=True,
)
fig.show()
fig.write_html("./Gewoelbtes_Element_und_Dropdown_fuer_PopUp.html", include_plotlyjs='cdn', include_mathjax='cdn')

