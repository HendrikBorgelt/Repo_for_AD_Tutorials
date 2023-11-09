# import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from stl import mesh

import Funktionen_Differentielles_Element as fd
import Funktionen_Pfeil as fp
import Funktionen_Moment as fm
import BasisFunktionen as bf


mesh_differential_element_1 = mesh.Mesh.from_file('./meshes/Differentielles_Element.stl')
mesh3D_Differential_element_1 = fd.create_mesh3d_for_dif_element(mesh_differential_element_1, 1, [0, 0, 0], 0, 0, 0)
mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Pfeil.stl')
mesh3D_Arrow_1 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, -50, 0], 0, 0, 0)
mesh3D_Arrow_2 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 0, 0], 0, 0, 0)
mesh3D_Arrow_3 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 50, 0], np.pi, 0, 0)
mesh3D_Arrow_4 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [-50, -10, 0], 0, np.pi, np.pi/360*150)
mesh3D_Arrow_5 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [50, -10, 0], 0, 0, np.pi/360*150)
mesh3D_Arrow_6 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.48296291314453416, [50, -8.3, 0], 0, 0, np.pi/360*180, bodycolor='lightblue')
mesh3D_Arrow_7 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.12940952255126037, [58.69805, -10, 0], 0, 0, 0, bodycolor='lightgreen')

mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_1)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_2)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_3)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_4)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_5)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_6)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_7)

# ([mesh3D_Arrow_1])
fig = go.Figure(data=mesh3D_Differential_element_1)
# fig = go.Figure(data=mesh3D)

force_annotations = [dict(x=0, y=-50, z=4.5,
                          text=r'$F_r * r d\phi$', textangle=0,
                          ax=0, ay=-75,
                          font=dict(color="black", size=12),
                          arrowcolor="black",
                          arrowsize=3, arrowwidth=1, arrowhead=1),
                     dict(x=-50, y=-10, z=4.5,
                          text=r'$F_\phi * dr$', textangle=0,
                          ax=0, ay=-75,
                          font=dict(color="black", size=12),
                          arrowcolor="black",
                          arrowsize=3, arrowwidth=1, arrowhead=1),
                     dict(x=50, y=-10, z=4.5,
                          text=r'$F_\phi * dr$', textangle=0,
                          ax=-50, ay=-50,
                          font=dict(color="black", size=12),
                          arrowcolor="black",
                          arrowsize=3, arrowwidth=1, arrowhead=1),
                     dict(x=50, y=-8.33, z=4.3466666,
                          text=r'$F_\phi * dr * sin\frac{d\phi}{2}$', textangle=0,
                          ax=50, ay=-50,
                          font=dict(color="blue", size=12),
                          arrowcolor="blue",
                          arrowsize=3, arrowwidth=1, arrowhead=1),
                     dict(x=58.69805, y=-10, z=1.164686,
                          text=r'$F_\phi * dr * sin\frac{d\phi}{2}$', textangle=0,
                          ax=0, ay=+75,
                          font=dict(color="green", size=12),
                          arrowcolor="green",
                          arrowsize=3, arrowwidth=1, arrowhead=1),
                     dict(x=0, y=50, z=4.5,
                          text=r'$(F_r + dF_r)(r + dr)\phi$', textangle=0,
                          ax=0, ay=-50,
                          font=dict(color="black", size=12),
                          arrowcolor="black",
                          arrowsize=3, arrowwidth=1, arrowhead=1),
                     dict(
                        x=0, y=0, z=4.5,
                        text=r'$q(r)* e*dr*rd\phi$', textangle=0,
                        ax=0, ay=-50,
                        font=dict(color="black", size=12),
                        arrowcolor="black",
                        arrowsize=3, arrowwidth=1, arrowhead=1)]

geometry_annotations = [dict(  # upper front curve
                            x=0, y=-25, z=25,
                            text=r'$r* d\phi$', textangle=0,
                            ax=0, ay=-50,
                            font=dict(color="black", size=12),
                            arrowcolor="black",
                            arrowsize=3, arrowwidth=1, arrowhead=1),
                        dict(  # right front curve
                            x=-25.8819, y=-28.40742, z=0,
                            text=r'$2* \frac{e}{2}$', textangle=0,
                            ax=0, ay=-50,
                            font=dict(color="black", size=12),
                            arrowcolor="black",
                            arrowsize=3, arrowwidth=1, arrowhead=1),
                        dict(  # right upper curve
                            x=-32.35238, y=-4.259264999999999, z=25,
                            text=r'$dr$', textangle=0,
                            ax=0, ay=-50,
                            font=dict(color="black", size=12),
                            arrowcolor="black",
                            arrowsize=3, arrowwidth=1, arrowhead=1),
                        dict(  # right back curve
                            x=0, y=25, z=25,
                            text=r'$(r + dr)* d\phi$', textangle=0,
                            ax=0, ay=-50,
                            font=dict(color="black", size=12),
                            arrowcolor="black",
                            arrowsize=3, arrowwidth=1, arrowhead=1),]

fig.update_layout(
    showlegend=False,
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="None",
                     method="relayout",
                     args=[{"scene.annotations": []}]),
                dict(label="Forces",
                     method="relayout",
                     args=[{"scene.annotations": force_annotations}]),
                dict(label="Geometry",
                     method="relayout",
                     args=[{"scene.annotations": geometry_annotations}]),
                dict(label="Both",
                     method="relayout",
                     args=[{"scene.annotations": force_annotations + geometry_annotations}]),
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.58,
            xanchor="left",
            y=1.08,
            yanchor="top"
        )
    ])

# fig.update_layout(
#     scene=dict(
#         annotations=[
#         dict(
#             x=0, y=-50, z=4.5,
#             text=r'$F_r * r d\phi$', textangle=0,
#             ax=0, ay=-75,
#             font=dict(color="black", size=12),
#             arrowcolor="black",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         dict(
#             x=-50, y=-10, z=4.5,
#             text=r'$F_\phi * dr$', textangle=0,
#             ax=0, ay=-75,
#             font=dict(color="black", size=12),
#             arrowcolor="black",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         dict(
#             x=50, y=-10, z=4.5,
#             text=r'$F_\phi * dr$', textangle=0,
#             ax=-50, ay=-50,
#             font=dict(color="black", size=12),
#             arrowcolor="black",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         dict(
#             x=50, y=-8.33, z=4.3466666,
#             text=r'$F_\phi * dr * sin\frac{d\phi}{2}$', textangle=0,
#             ax=50, ay=-50,
#             font=dict(color="blue", size=12),
#             arrowcolor="blue",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         dict(
#             x=58.69805, y=-10, z=1.164686,
#             text=r'$F_\phi * dr * sin\frac{d\phi}{2}$', textangle=0,
#             ax=0, ay=+75,
#             font=dict(color="green", size=12),
#             arrowcolor="green",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         dict(
#             x=0, y=50, z=4.5,
#             text=r'$(F_r + dF_r)(r + dr)\phi$', textangle=0,
#             ax=0, ay=-50,
#             font=dict(color="black", size=12),
#             arrowcolor="black",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         dict(
#             x=0, y=0, z=4.5,
#             text=r'$q(r)* e*dr*rd\phi$', textangle=0,
#             ax=0, ay=-50,
#             font=dict(color="black", size=12),
#             arrowcolor="black",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#
#         dict( # upper front curve
#             x=0, y=-25, z=25,
#             text=r'$r* d\phi$', textangle=0,
#             ax=0, ay=-25,
#             font=dict(color="black", size=12),
#             arrowcolor="black",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         dict( # right front curve
#             x=-25.8819, y=-28.40742, z=0,
#             text=r'$2* \frac{e}{2}$', textangle=0,
#             ax=0, ay=-25,
#             font=dict(color="black", size=12),
#             arrowcolor="black",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         dict( # right upper curve
#             x=-32.35238, y=-4.259264999999999, z=25,
#             text=r'$dr$', textangle=0,
#             ax=0, ay=-25,
#             font=dict(color="black", size=12),
#             arrowcolor="black",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         dict( # right back curve
#             x=0, y=25, z=25,
#             text=r'$(r + dr)* d\phi$', textangle=0,
#             ax=0, ay=-25,
#             font=dict(color="black", size=12),
#             arrowcolor="black",
#             arrowsize=3, arrowwidth=1, arrowhead=1),
#         ],
#     ),
# )

fig.show()
fig.write_html("./Kreisscheibe_mit_Kraftzerlegung_mit_Dropdown.html", include_plotlyjs='cdn', include_mathjax='cdn')
