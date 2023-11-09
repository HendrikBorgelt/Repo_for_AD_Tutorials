# import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from stl import mesh

import Funktionen_Differentielles_Element as fd
import Funktionen_Pfeil as fp
import Funktionen_Moment as fm
import BasisFunktionen as bf





# mesh_differential_element_1 = mesh.Mesh.from_file('./meshes/Differentielles_Element.stl')
# mesh3D_Differential_element_1 = fd.create_mesh3d_for_dif_element(mesh_differential_element_1, 1, [0, 0, 0], 0, 0, 0)
# mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Pfeil.stl')
# mesh3D_Arrow_1 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, -50, 0], 0, 0, 0)
# mesh3D_Arrow_2 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 0, 0], 0, 0, 0)
# mesh3D_Arrow_3 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 50, 0], np.pi, 0, 0)
# mesh3D_Arrow_4 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [-50, -10, 0], 0, np.pi, np.pi/360*150)
# mesh3D_Arrow_5 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [50, -10, 0], 0, 0, np.pi/360*150)
# mesh3D_Arrow_6 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.48296291314453416, [50, -8.3, 0], 0, 0, np.pi/360*180, bodycolor='lightblue')
# mesh3D_Arrow_7 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.12940952255126037, [58.69805, -10, 0], 0, 0, 0, bodycolor='lightgreen')
#
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_1)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_2)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_3)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_4)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_5)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_6)
# mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_7)

# ([mesh3D_Arrow_1])
# fig = go.Figure(data=mesh3D_Differential_element_1)
# fig = go.Figure(data=mesh3D_Differential_element_1)

# fig.show()
# fig.write_html("./file.html")

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Initialize the app
app = Dash(__name__)

mesh_differential_element_1 = mesh.Mesh.from_file('./meshes/Differentielles_Element.stl')
mesh3D_Differential_element_1 = fd.create_mesh3d_for_dif_element(mesh_differential_element_1, 1, [0, 0, 0], 0,
                                                                 0, 0)
mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Pfeil.stl')
mesh3D_Arrow_1 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, -50, 0], 0, 0, 0)
mesh3D_Arrow_2 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 0, 0], 0, 0, 0)
mesh3D_Arrow_3 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 50, 0], np.pi, 0, 0)
mesh3D_Arrow_4 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [-50, -10, 0], 0, np.pi,
                                            np.pi / 360 * 150)
mesh3D_Arrow_5 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [50, -10, 0], 0, 0, np.pi / 360 * 150)
mesh3D_Arrow_6 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.48296291314453416, [50, -8.3, 0], 0, 0,
                                            np.pi / 360 * 180, bodycolor='lightblue')
mesh3D_Arrow_7 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.12940952255126037, [58.69805, -10, 0], 0,
                                            0, 0, bodycolor='lightgreen')

mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_1)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_2)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_3)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_4)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_5)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_6)
mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_7)
fig = go.Figure(data=mesh3D_Differential_element_1)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['with', 'without'], value='without', id='controls-and-radio-item'),
    dcc.Graph(figure=fig, id='controls-and-graph')
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    # fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    if col_chosen == 'with':
        mesh_differential_element_1 = mesh.Mesh.from_file('./meshes/Differentielles_Element.stl')
        mesh3D_Differential_element_1 = fd.create_mesh3d_for_dif_element(mesh_differential_element_1, 1, [0, 0, 0], 0,
                                                                         0, 0)
        mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Pfeil.stl')
        mesh3D_Arrow_1 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, -50, 0], 0, 0, 0)
        mesh3D_Arrow_2 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 0, 0], 0, 0, 0)
        mesh3D_Arrow_3 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 50, 0], np.pi, 0, 0)
        mesh3D_Arrow_4 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [-50, -10, 0], 0, np.pi,
                                                    np.pi / 360 * 150)
        mesh3D_Arrow_5 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [50, -10, 0], 0, 0, np.pi / 360 * 150)
        mesh3D_Arrow_6 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.48296291314453416, [50, -8.3, 0], 0, 0,
                                                    np.pi / 360 * 180, bodycolor='lightblue')
        mesh3D_Arrow_7 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.12940952255126037, [58.69805, -10, 0], 0,
                                                    0, 0, bodycolor='lightgreen')

        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_1)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_2)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_3)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_4)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_5)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_6)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_7)
    else:
        mesh_differential_element_1 = mesh.Mesh.from_file('./meshes/Differentielles_Element.stl')
        mesh3D_Differential_element_1 = fd.create_mesh3d_for_dif_element(mesh_differential_element_1, 1, [0, 0, 0], 0,
                                                                         0, 0)
        mesh_straight_arrow_1 = mesh.Mesh.from_file('./meshes/Pfeil.stl')
        mesh3D_Arrow_1 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, -50, 0], 0, 0, 0)
        mesh3D_Arrow_2 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 0, 0], 0, 0, 0)
        mesh3D_Arrow_3 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [0, 50, 0], np.pi, 0, 0)
        mesh3D_Arrow_4 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [-50, -10, 0], 0, np.pi,
                                                    np.pi / 360 * 150)
        mesh3D_Arrow_5 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.5, [50, -10, 0], 0, 0, np.pi / 360 * 150)
        mesh3D_Arrow_6 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.48296291314453416, [50, -8.3, 0], 0, 0,
                                                    np.pi / 360 * 180, bodycolor='lightblue')
        mesh3D_Arrow_7 = fp.create_mesh3d_for_arrow(mesh_straight_arrow_1, 0.12940952255126037, [58.69805, -10, 0], 0,
                                                    0, 0, bodycolor='lightgreen')

        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_1)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_2)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_3)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_4)
        mesh_data = mesh3D_Differential_element_1.extend(mesh3D_Arrow_5)

    fig = go.Figure(data=mesh3D_Differential_element_1)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


# CSS color:
#                 aliceblue, antiquewhite, aqua, aquamarine, azure,
#                 beige, bisque, black, blanchedalmond, blue,
#                 blueviolet, brown, burlywood, cadetblue,
#                 chartreuse, chocolate, coral, cornflowerblue,
#                 cornsilk, crimson, cyan, darkblue, darkcyan,
#                 darkgoldenrod, darkgray, darkgrey, darkgreen,
#                 darkkhaki, darkmagenta, darkolivegreen, darkorange,
#                 darkorchid, darkred, darksalmon, darkseagreen,
#                 darkslateblue, darkslategray, darkslategrey,
#                 darkturquoise, darkviolet, deeppink, deepskyblue,
#                 dimgray, dimgrey, dodgerblue, firebrick,
#                 floralwhite, forestgreen, fuchsia, gainsboro,
#                 ghostwhite, gold, goldenrod, gray, grey, green,
#                 greenyellow, honeydew, hotpink, indianred, indigo,
#                 ivory, khaki, lavender, lavenderblush, lawngreen,
#                 lemonchiffon, lightblue, lightcoral, lightcyan,
#                 lightgoldenrodyellow, lightgray, lightgrey,
#                 lightgreen, lightpink, lightsalmon, lightseagreen,
#                 lightskyblue, lightslategray, lightslategrey,
#                 lightsteelblue, lightyellow, lime, limegreen,
#                 linen, magenta, maroon, mediumaquamarine,
#                 mediumblue, mediumorchid, mediumpurple,
#                 mediumseagreen, mediumslateblue, mediumspringgreen,
#                 mediumturquoise, mediumvioletred, midnightblue,
#                 mintcream, mistyrose, moccasin, navajowhite, navy,
#                 oldlace, olive, olivedrab, orange, orangered,
#                 orchid, palegoldenrod, palegreen, paleturquoise,
#                 palevioletred, papayawhip, peachpuff, peru, pink,
#                 plum, powderblue, purple, red, rosybrown,
#                 royalblue, saddlebrown, salmon, sandybrown,
#                 seagreen, seashell, sienna, silver, skyblue,
#                 slateblue, slategray, slategrey, snow, springgreen,
#                 steelblue, tan, teal, thistle, tomato, turquoise,
#                 violet, wheat, white, whitesmoke, yellow,
#                 yellowgreen