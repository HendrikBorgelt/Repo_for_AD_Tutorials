# import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from stl import mesh

import Funktionen_Differentielles_Element as fd
import Funktionen_Pfeil as fp
import Funktionen_Moment as fm
import Funktionen_Kraftfelder as fk
import BasisFunktionen as bf


mesh_differential_element_1 = mesh.Mesh.from_file('./meshes/Differentielles_Element.stl')
mesh3D_Differential_element_1 = fd.create_mesh3d_for_dif_element(mesh_differential_element_1, 1, [0, 0, 0], 0, 0, 0, frame=True)
mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Pfeil.stl')
mesh3D_Arrow_1 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, -50, 0], 0, 0, 0, '<i>F<sub>r </sub> r d&#966; </i>')
mesh3D_Arrow_2 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 0, 0], np.pi, 0, 0, '<i>q( r ) e dr r d&#966; </i>')
mesh3D_Arrow_3 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 50, 0], np.pi, 0, 0, '<i>(F<sub>r </sub>+dF<sub>r </sub>)(r + dr)d&#966; </i>')

mesh3D_Arrow_4 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [-50, -10, 0], 0, np.pi, np.pi/360*150, '<i>F<sub>&#966; </sub>dr</i>')
mesh3D_Arrow_5 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.48296291314453416, [-50, -8.3, 0], 0, np.pi, np.pi/360*180, '<i>F<sub>&#966; </sub>dr cos(d&#966; &#8260; 2) &#8776; F<sub>&#966; </sub>dr</i>', bodycolor='lightblue')
mesh3D_Arrow_6 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.12940952255126037, [-58.69805, -10, 0], 0, np.pi, 0, '<i>F<sub>&#966; </sub>dr sin(d&#966; &#8260; 2) &#8776; F<sub>&#966; </sub>dr d&#966; &#8260; 2</i>', bodycolor='lightgreen')

mesh3D_Arrow_7 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [50, -10, 0], 0, 0, np.pi/360*150, '<i>F<sub>&#966; </sub>dr</i>')
mesh3D_Arrow_8 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.48296291314453416, [50, -8.3, 0], 0, 0, np.pi/360*180, '<i>F<sub>&#966; </sub>dr cos(d&#966; &#8260; 2) &#8776; F<sub>&#966; </sub>dr</i>', bodycolor='lightblue')
mesh3D_Arrow_9 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.12940952255126037, [58.69805, -10, 0], 0, 0, 0, '<i>F<sub>&#966; </sub>dr sin(d&#966; &#8260; 2) &#8776; F<sub>&#966; </sub>dr d&#966; &#8260; 2</i>', bodycolor='lightgreen')

mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_1) # F_r r d phi
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_2) # q r e dr r d phi
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_3) # (F_r + dF_r) (r + dr) d phi
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_4) # F_phi dr rechts
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_5) # F_phi dr cos d phi / 2
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_6) # F_phi dr sin d phi / 2
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_7) # F_phi dr links
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_8) # F_phi dr cos d phi / 2
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_9) # F_phi dr sin d phi / 2
# mesh_data = mesh3D_Differential_element_1.extend([fk.create_mesh3d_for_vectorfeld(0, 35, 25, 0, 0, 20,1, 1,8, 15)])
# mesh_data = mesh3D_Differential_element_1.extend([fk.create_mesh3d_for_vectorfeld(0, 20, -25, 0, 0, 20,-1, 1,8, 15)])

# ([mesh3D_Arrow_1])
fig = go.Figure(data=mesh3D_Differential_element_1)
# fig = go.Figure(data=mesh3D)

force_annotations_all = [dict(x=0, y=-50, z=4.5,
                              text=r'$F_r * r d\phi$', textangle=0,
                              ax=0, ay=-75,
                              font=dict(color="black", size=12),
                              arrowcolor="black",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=-50, y=-10, z=4.5,
                              text=r'$F_\phi * dr$', textangle=0,
                              ax=0, ay=-75,
                              font=dict(color="black", size=12),
                              arrowcolor="black",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=50, y=-10, z=4.5,
                              text=r'$F_\phi * dr$', textangle=0,
                              ax=-50, ay=-50,
                              font=dict(color="black", size=12),
                              arrowcolor="black",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=50, y=-8.33, z=4.3466666,
                              text=r'$F_\phi * dr * cos\frac{d\phi}{2}$', textangle=0,
                              ax=50, ay=-50,
                              font=dict(color="blue", size=12),
                              arrowcolor="blue",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=58.69805, y=-10, z=1.164686,
                              text=r'$F_\phi * dr * sin\frac{d\phi}{2}$', textangle=0,
                              ax=0, ay=+75,
                              font=dict(color="green", size=12),
                              arrowcolor="green",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=0, y=50, z=4.5,
                              text=r'$(F_r + dF_r)(r + dr)\phi$', textangle=0,
                              ax=0, ay=-50,
                              font=dict(color="black", size=12),
                              arrowcolor="black",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(
                            x=0, y=0, z=4.5,
                            text=r'$q(r)* e*dr*rd\phi$', textangle=0,
                            ax=0, ay=-50,
                            font=dict(color="black", size=12),
                            arrowcolor="black",
                            arrowsize=3, arrowwidth=1, arrowhead=0)]

force_annotations_x = [dict(x=0, y=-50, z=4.5,
                              text=r'$F_r * r d\phi$', textangle=0,
                              ax=0, ay=-75,
                              font=dict(color="black", size=12),
                              arrowcolor="black",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         # dict(x=-50, y=-10, z=4.5,
                         #      text=r'$F_\phi * dr$', textangle=0,
                         #      ax=0, ay=-75,
                         #      font=dict(color="black", size=12),
                         #      arrowcolor="black",
                         #      arrowsize=3, arrowwidth=1, arrowhead=0),
                         # dict(x=50, y=-10, z=4.5,
                         #      text=r'$F_\phi * dr$', textangle=0,
                         #      ax=-50, ay=-50,
                         #      font=dict(color="black", size=12),
                         #      arrowcolor="black",
                         #      arrowsize=3, arrowwidth=1, arrowhead=0),
                         # dict(x=50, y=-8.33, z=4.3466666,
                         #      text=r'$F_\phi * dr * cos\frac{d\phi}{2}$', textangle=0,
                         #      ax=50, ay=-50,
                         #      font=dict(color="blue", size=12),
                         #      arrowcolor="blue",
                         #      arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=58.69805, y=-10, z=1.164686,
                              text=r'$F_\phi * dr * sin\frac{d\phi}{2}$', textangle=0,
                              ax=0, ay=+75,
                              font=dict(color="green", size=12),
                              arrowcolor="green",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=-58.69805, y=-10, z=1.164686,
                              text=r'$F_\phi * dr * sin\frac{d\phi}{2}$', textangle=0,
                              ax=0, ay=+75,
                              font=dict(color="green", size=12),
                              arrowcolor="green",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=0, y=50, z=4.5,
                              text=r'$(F_r + dF_r)(r + dr)\phi$', textangle=0,
                              ax=0, ay=-50,
                              font=dict(color="black", size=12),
                              arrowcolor="black",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(
                            x=0, y=0, z=4.5,
                            text=r'$q(r)* e*dr*rd\phi$', textangle=0,
                            ax=0, ay=-50,
                            font=dict(color="black", size=12),
                            arrowcolor="black",
                            arrowsize=3, arrowwidth=1, arrowhead=0)]

force_annotations_y = [
                         # dict(x=0, y=-50, z=4.5,
                         #      text=r'$F_r * r d\phi$', textangle=0,
                         #      ax=0, ay=-75,
                         #      font=dict(color="black", size=12),
                         #      arrowcolor="black",
                         #      arrowsize=3, arrowwidth=1, arrowhead=0),
                         # dict(x=-50, y=-10, z=4.5,
                         #      text=r'$F_\phi * dr$', textangle=0,
                         #      ax=0, ay=-75,
                         #      font=dict(color="black", size=12),
                         #      arrowcolor="black",
                         #      arrowsize=3, arrowwidth=1, arrowhead=0),
                         # dict(x=50, y=-10, z=4.5,
                         #      text=r'$F_\phi * dr$', textangle=0,
                         #      ax=-50, ay=-50,
                         #      font=dict(color="black", size=12),
                         #      arrowcolor="black",
                         #      arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=50, y=-8.33, z=4.3466666,
                              text=r'$F_\phi * dr * cos\frac{d\phi}{2}$', textangle=0,
                              ax=50, ay=-50,
                              font=dict(color="blue", size=12),
                              arrowcolor="blue",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         dict(x=-50, y=-8.33, z=4.3466666,
                              text=r'$F_\phi * dr * cos\frac{d\phi}{2}$', textangle=0,
                              ax=-50, ay=-50,
                              font=dict(color="blue", size=12),
                              arrowcolor="blue",
                              arrowsize=3, arrowwidth=1, arrowhead=0),
                         # dict(x=58.69805, y=-10, z=1.164686,
                         #      text=r'$F_\phi * dr * sin\frac{d\phi}{2}$', textangle=0,
                         #      ax=0, ay=+75,
                         #      font=dict(color="green", size=12),
                         #      arrowcolor="green",
                         #      arrowsize=3, arrowwidth=1, arrowhead=0),
                         # dict(x=0, y=50, z=4.5,
                         #      text=r'$(F_r + dF_r)(r + dr)\phi$', textangle=0,
                         #      ax=0, ay=-50,
                         #      font=dict(color="black", size=12),
                         #      arrowcolor="black",
                         #      arrowsize=3, arrowwidth=1, arrowhead=0),
                         # dict(
                         #    x=0, y=0, z=4.5,
                         #    text=r'$q(r)* e*dr*rd\phi$', textangle=0,
                         #    ax=0, ay=-50,
                         #    font=dict(color="black", size=12),
                         #    arrowcolor="black",
                         #    arrowsize=3, arrowwidth=1, arrowhead=0)
]


geometry_annotations = [dict(  # upper front curve
                            x=0, y=-25, z=25, text=r'$r* d\phi$', textangle=0, ax=-50, ay=-50, font=dict(color="black", size=12), arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
                        dict(  # right front curve
                            x=-25.8819, y=-28.40742, z=0, text=r'$2* \frac{e}{2}$', textangle=0, ax=50, ay=-50, font=dict(color="black", size=12), arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
                        dict(  # right upper curve
                            x=-32.35238, y=-4.259264999999999, z=25, text=r'$dr$', textangle=0,ax=50, ay=-50, font=dict(color="black", size=12), arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0),
                        dict(  # right back curve
                            x=0, y=25, z=25, text=r'$(r + dr)* d\phi$', textangle=0, ax=50, ay=-50, font=dict(color="black", size=12), arrowcolor="black", arrowsize=3, arrowwidth=1, arrowhead=0)]


fig.update_layout(
    showlegend=False,
    updatemenus=[
        dict(
            active=0,
            # type="buttons",
            buttons=list([
                dict(label="Alle Kräfte", method="update",
                     args=[{"visible": [True] * 134}, {"scene.annotations": []}, ]),
                dict(label="Kräfte in \"X\" Richtung", method="update",
                     args=[{"visible": [True]*46+[False]*22+[True]*11+[False]*22+[True]*11}, {"scene.annotations": []}]),
                dict(label="Kräfte in \"Y\" Richtung", method="update", args=[
                    {"visible": [True]*13+[False]*44+[True]*11+[False]*22+[True]*11+[False]*11},
                    {"scene.annotations": []}]),
            ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.0, xanchor="left",
            y=1.115, yanchor="top", font=dict(size=10)
        ),
        dict(active=0,
             buttons=list([
                 dict(label="Alle Kräfte", method="update",
                      args=[{"visible": [True] * 134}, {"scene.annotations": force_annotations_all}, ]),
                 dict(label="Kräfte in \"X\" Richtung", method="update",
                      args=[{"visible": [True]*46+[False]*22+[True]*11+[False]*22+[True]*11}, {"scene.annotations": force_annotations_x}]),
                 dict(label="Kräfte in \"Y\" Richtung", method="update", args=[
                     {"visible": [True]*13+[False]*44+[True]*11+[False]*22+[True]*11+[False]*11},
                     {"scene.annotations": force_annotations_y}]),
             ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.0, xanchor="left",
             y=1.02, yanchor="top", font=dict(size=10)
             ),
        # dict(
        #     name='Beschriftung',
        #     active=0,
        #     buttons=list([
        #         dict(label="Keine Beschriftung",
        #              method="relayout",
        #              args=[{"scene.annotations": []}]),
        #         dict(label="Kräfte Beschriftet",
        #              method="relayout",
        #              args=[{"scene.annotations": force_annotations}]),
        #         dict(label="Geometry Beschriftet",
        #              method="relayout",
        #              args=[{"scene.annotations": geometry_annotations}]),
        #         dict(label="Alle Beschriftungen",
        #              method="relayout",
        #              args=[{"scene.annotations": force_annotations + geometry_annotations}]),
        #     ]),
        #     direction="down",
        #     pad={"r": 10, "t": 10},
        #     showactive=True,
        #     x=0.58,
        #     xanchor="left",
        #     y=1.08,
        #     yanchor="top"
        # ),
        dict(
            active=0,
            buttons=list([
                  dict(label="Ausblenden", method="relayout", args=[{"scene.annotations": []},]),
                  dict(label="Einblenden", method="relayout", args=[{"scene.annotations": geometry_annotations}])
              ]), direction="down", showactive=False, pad={"r": 0, "t": 0}, x=0.55, xanchor="left", y=1.22, yanchor="top", font=dict(size=10)
        ),
        # dict(
        #     name='Kräfte ohne Beschriftung',
        #     active=0,
        #     buttons=list([
        #         dict(label="Alle Kräfte",
        #              method="update",
        #              args=[{"visible": [True]*112+[False]*2},]),
        #         dict(label="F_r",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*13+[False]*11+[True]*99},{"scene.annotations": force_annotations + geometry_annotations}]),
        #         dict(label="q r",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*24+[False]*11+[True]*88},{"scene.annotations": force_annotations[:1] + force_annotations[5:] + geometry_annotations}]),
        #         dict(label="F_r + dF_r",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*35+[False]*11+[True]*77},{"scene.annotations": []}]),
        #         dict(label='F_phi rechts',
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*46+[False]*11+[True]*66},{"scene.annotations": []}]),
        #         dict(label="F_phi cos d phi / 2 rechts",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*57+[False]*11+[True]*55},{"scene.annotations": []}]),
        #         dict(label="F_phi sin d phi / 2 rechts",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*68+[False]*11+[True]*44},{"scene.annotations": []}]),
        #         dict(label="F_phi links",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*79+[False]*11+[True]*22},{"scene.annotations": []}]),
        #         dict(label="F_phi dr cos d phi / 2 links",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*90+[False]*11+[True]*11},{"scene.annotations": []}]),
        #         dict(label="F_phi dr sin d phi / 2 links",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*101+[False]*11+[True]*0},{"scene.annotations": []}]),
        #         dict(label="nur Kräfte in \"X\" Richtung",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*46+[False]*22+[True]*11+[False]*22+[True]*11},{"scene.annotations": []}]),
        #         dict(label="nur Kräfte in \"y\" Richtung",
        #              method="update", # Dif = 13, Arrow = 11 , Vector = 1
        #              args=[{"visible": [True]*13+[False]*44+[True]*11+[False]*22+[True]*11+[False]*11},{"scene.annotations": []}]),
        #     ]),
        #     direction="down",
        #     pad={"r": 10, "t": 10},
        #     showactive=True,
        #     x=0.33,
        #     xanchor="left",
        #     y=1.08,
        #     yanchor="top"
        # ),
        dict(
            active=0,
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
                dict(label="Frontal erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=1.7))}]),
            ]),
            direction="down", pad={"r": 0, "t": 0}, showactive=True, x=-0.05, xanchor="left", y=1.22, yanchor="top", font=dict(size=10)
        )
    ],
    scene=dict(
        xaxis=dict(nticks=20, range=[-75, 75], autorange=False), yaxis=dict(nticks=20, range=[-75, 75], autorange=False), zaxis=dict(nticks=15, range=[-50, 50], autorange=False),
        aspectmode='manual', xaxis_title='Y Achse', yaxis_title='X Achse', zaxis_title='Z Achse', aspectratio=dict(x=1, y=1, z=0.8),
        ),
    scene_camera=dict(eye=dict(x=-1.25, y=-1.25, z=1.25)),
    annotations=[
        dict(text="Kräfte ohne                                                                                                                                            "
                  "<br>Beschriftung                                                                                                                                           "
                  "<br> "
                  "<br>Kräfte mit                                                                                                                                             "
                  "<br>Beschriftung                                                                                                                                           "
                  "<br>", x=-0.18, y=1.11, showarrow=False, font=dict(size=10)),
        dict(text=""
                  "<br>"
                  "<br> "
                  "<br> Kamera                         "
                  "<br> "
                  "<br> "
                  "<br> ", x=-0.19, y=1.23, showarrow=False, font=dict(size=10)),
        dict(text=""
                  "<br>"
                  "<br> "
                  "<br> Geometrie                 "
                  "<br> "
                  "<br> "
                  "<br> ", x=0.53, y=1.23, showarrow=False, font=dict(size=10)),

    ],
    width=600,
    height=600,
    minreducedwidth=550,
    minreducedheight=400,
    autosize=False,
    # paper_bgcolor='white',
)

# fig.show()
fig.write_html("./Kreisscheibe_mit_Kraftzerlegung_mit_Dropdown_fuer_Smartphones.html", include_plotlyjs='cdn', include_mathjax='cdn')

fig.update_layout(
    showlegend=False,
    updatemenus=[
        dict(
            active=0,
            # type="buttons",
            buttons=list([
                dict(label="Alle Kräfte", method="update",
                     args=[{"visible": [True] * 134}, {"scene.annotations": []}, ]),
                dict(label="Kräfte in \"X\" Richtung", method="update",
                     args=[{"visible": [True]*46+[False]*22+[True]*11+[False]*22+[True]*11}, {"scene.annotations": []}]),
                dict(label="Kräfte in \"Y\" Richtung", method="update", args=[
                    {"visible": [True]*13+[False]*44+[True]*11+[False]*22+[True]*11+[False]*11},
                    {"scene.annotations": []}]),
            ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.33, xanchor="left",
            y=1.115, yanchor="top", font=dict(size=10)
        ),
        dict(active=0,
             buttons=list([
                 dict(label="Alle Kräfte", method="update",
                      args=[{"visible": [True] * 134}, {"scene.annotations": force_annotations_all}, ]),
                 dict(label="Kräfte in \"X\" Richtung", method="update",
                      args=[{"visible": [True]*46+[False]*22+[True]*11+[False]*22+[True]*11}, {"scene.annotations": force_annotations_x}]),
                 dict(label="Kräfte in \"Y\" Richtung", method="update", args=[
                     {"visible": [True]*13+[False]*44+[True]*11+[False]*22+[True]*11+[False]*11},
                     {"scene.annotations": force_annotations_y}]),
             ]), type="buttons", direction="right", showactive=False, pad={"r": 0, "t": 0}, x=0.33, xanchor="left",
             y=1.055, yanchor="top", font=dict(size=10)
             ),
        dict(
            active=0,
            buttons=list([
                  dict(label="Ausblenden", method="relayout", args=[{"scene.annotations": []},]),
                  dict(label="Einblenden", method="relayout", args=[{"scene.annotations": geometry_annotations}])
              ]), direction="down", showactive=False, pad={"r": 0, "t": 0}, x=0.54, xanchor="left", y=1.22, yanchor="top", font=dict(size=10)
        ),
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
                dict(label="Frontal erhöht", method="relayout", args=[{'scene.camera': dict(eye=dict(x=0, y=-1.7, z=1.7))}]),
            ]),
             direction="down", pad={"r": 0, "t": 0}, showactive=True, x=0.33, xanchor="left", y=1.22, yanchor="top", font=dict(size=10)
        )
    ],
    scene=dict(
        xaxis=dict(nticks=20, range=[-75, 75], autorange=False), yaxis=dict(nticks=20, range=[-75, 75], autorange=False), zaxis=dict(nticks=15, range=[-50, 50], autorange=False),
        aspectmode='manual', xaxis_title='Y Achse', yaxis_title='X Achse', zaxis_title='Z Achse', aspectratio=dict(x=1, y=1, z=0.8),
        ),
    scene_camera=dict(eye=dict(x=-1.25, y=-1.25, z=1.25)),
    annotations=[
        dict(text="Kräfte ohne                                                                                                                                            "
                  "<br>Beschriftung                                                                                                                                           "
                  "<br> "
                  "<br>Kräfte mit                                                                                                                                             "
                  "<br>Beschriftung                                                                                                                                           "
                  "<br>", x=0.28, y=1.11, showarrow=False, font=dict(size=10)),
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
                  "<br> Geometrie                 "
                  "<br> "
                  "<br> "
                  "<br> ", x=0.53, y=1.23, showarrow=False, font=dict(size=10)),

    ],
    width=1800,
    height=900,
    minreducedwidth=550,
    minreducedheight=600,
    autosize=True,
)

fig.show()
fig.write_html("./Kreisscheibe_mit_Kraftzerlegung_mit_Dropdown_fuer_FullScreen.html", include_plotlyjs='cdn', include_mathjax='cdn')






